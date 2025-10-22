#!/bin/bash

# backup_database.sh
# Скрипт резервного копирования базы данных

DB_NAME="guide_dnr"
BACKUP_DIR="./backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

echo "Создание резервной копии базы данных $DB_NAME..."
pg_dump -U guide_user -h localhost $DB_NAME > $BACKUP_DIR/backup_$TIMESTAMP.sql

echo "Резервная копия создана: $BACKUP_DIR/backup_$TIMESTAMP.sql"

# Автоудаление старых бэкапов (старше 7 дней)
find $BACKUP_DIR -name "backup_*.sql" -mtime +7 -delete