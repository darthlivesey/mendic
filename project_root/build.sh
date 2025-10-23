#!/usr/bin/env bash
set -e  # Остановить при любой ошибке

echo "=== Starting Build Process ==="

# Установка зависимостей через setup.py (более надежный способ)
echo "Installing dependencies via setup.py..."
python setup.py develop

# Альтернативно: установка через pip
echo "Installing dependencies via pip..."
pip install --no-cache-dir -r requirements.txt

# Применение миграций (если manage.py существует)
if [ -f "manage.py" ]; then
    echo "Applying migrations..."
    python manage.py migrate
else
    echo "ERROR: manage.py not found!"
    echo "Current directory: $(pwd)"
    echo "Directory contents:"
    ls -la
    exit 1
fi

# Сбор статических файлов
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "=== Build completed successfully! ==="