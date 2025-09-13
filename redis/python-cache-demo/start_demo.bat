@echo off
REM Script para iniciar o demo de cache Redis

echo 🚀 Iniciando Redis Cache Demo...

REM Verificar se o Redis está rodando
echo 🔍 Verificando Redis...
docker exec redis-playground redis-cli ping >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Redis não está rodando. Iniciando...
    cd ..
    docker-compose up -d
    cd python-cache-demo
    timeout /t 5 /nobreak >nul
)

REM Verificar se as dependências estão instaladas
echo 📦 Verificando dependências...
python -c "import fastapi, redis, requests" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 Instalando dependências...
    pip install -r requirements.txt
)

REM Iniciar a API
echo 🚀 Iniciando API...
echo.
echo 🌐 API disponível em: http://localhost:8000
echo 📚 Documentação: http://localhost:8000/docs
echo.
echo Para testar performance, execute em outro terminal:
echo   python test_performance.py
echo.
echo Pressione Ctrl+C para parar a API
echo.

python app.py
