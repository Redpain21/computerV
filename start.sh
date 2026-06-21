#!/bin/bash

echo "🎭 Iniciando MoodMeter AI..."

# Crear entorno virtual si no existe
if [ ! -d "env" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv env
fi

# Activar entorno virtual
source env/bin/activate

echo "⬆️ Actualizando pip..."
pip install --upgrade pip

echo "📚 Instalando dependencias..."
pip install -r requirements.txt

echo "🚀 Iniciando servidor FastAPI..."

uvicorn app.main:app --reload