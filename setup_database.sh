#!/bin/bash

# setup_database.sh
# Скрипт автоматической настройки базы данных для проекта "Гид по ДНР"

set -e  # Завершить скрипт при любой ошибке

echo "=== Настройка базы данных для Гид по ДНР ==="

# Параметры базы данных
DB_NAME="guide_dnr"
DB_USER="guide_user"
DB_PASSWORD="secure_password_123"

# Проверка подключения к PostgreSQL
echo "1. Проверка подключения к PostgreSQL..."
if ! psql -U postgres -c "SELECT version();" > /dev/null 2>&1; then
    echo "❌ Ошибка: Не удается подключиться к PostgreSQL"
    echo "   Убедитесь, что PostgreSQL запущен: brew services start postgresql"
    exit 1
fi
echo "   ✅ PostgreSQL доступен"

# Создание базы данных
echo "2. Создание базы данных..."
psql -U postgres -c "CREATE DATABASE $DB_NAME;" 2>/dev/null || echo "   ⚠️ База данных уже существует"

# Создание пользователя
echo "3. Создание пользователя..."
psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';" 2>/dev/null || echo "   ⚠️ Пользователь уже существует"

# Назначение прав
echo "4. Настройка прав доступа..."
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
psql -U postgres -d $DB_NAME -c "GRANT ALL ON SCHEMA public TO $DB_USER;"

# Включение расширений (если нужны)
echo "5. Включение расширений..."
psql -U postgres -d $DB_NAME -c "CREATE EXTENSION IF NOT EXISTS postgis;" 2>/dev/null || echo "   ⚠️ Расширение postgis недоступно"

# Применение оптимизационных настроек
echo "6. Применение оптимизационных настроек..."
psql -U postgres -d $DB_NAME << EOF
ALTER SYSTEM SET shared_buffers = '256MB';
ALTER SYSTEM SET effective_cache_size = '1GB';
ALTER SYSTEM SET work_mem = '16MB';
ALTER SYSTEM SET max_connections = 100;
SELECT pg_reload_conf();
EOF

echo "7. Проверка настроек..."
psql -U postgres -d $DB_NAME -c "SELECT name, setting, unit FROM pg_settings WHERE name IN ('shared_buffers', 'effective_cache_size', 'work_mem', 'max_connections');"

echo ""
echo "=== Настройка завершена! ==="
echo "База данных: $DB_NAME"
echo "Пользователь: $DB_USER"
echo "Пароль: $DB_PASSWORD"
echo ""
echo "Для применения миграций Django выполните:"
echo "python manage.py migrate"