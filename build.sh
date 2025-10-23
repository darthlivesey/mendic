#!/usr/bin/env bash
# build.sh

echo "Starting build process..."

# Установка зависимостей
pip install -r requirements.txt

# Применение миграций
python manage.py migrate

# Сбор статических файлов
python manage.py collectstatic --noinput

echo "Build completed successfully!"