#!/bin/bash
set -e

cd /app/chatbot/model

if [ ! -f "training_data" ] || [ ! -f "model.tflearn.index" ]; then
  echo "==> Training model (first run only, may take several minutes)..."
  python bot.py
  echo "==> Training complete."
else
  echo "==> Model files found, skipping training."
fi

cd /app
python manage.py migrate --noinput
echo "==> Starting Django on http://0.0.0.0:8000"
exec python manage.py runserver 0.0.0.0:8000
