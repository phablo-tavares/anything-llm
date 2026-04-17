#!/bin/bash
set -e

trap 'echo "Encerrando servicos..."; kill $(jobs -p) 2>/dev/null; exit 0' SIGTERM SIGINT

echo "========================================"
echo "  AnythingLLM - Ambiente de Dev Docker"
echo "========================================"
echo ""

# Garante que o diretorio de storage existe antes do Prisma criar o banco
mkdir -p /app/server/storage

echo "[1/3] Instalando dependencias do server..."
yarn --cwd /app/server install --network-timeout 100000

echo "[2/3] Instalando dependencias do collector..."
yarn --cwd /app/collector install --network-timeout 100000

echo "[3/3] Instalando dependencias do frontend..."
yarn --cwd /app/frontend install --network-timeout 100000

echo ""
echo "[DB] Gerando Prisma client e aplicando migrations..."
cd /app/server
export CHECKPOINT_DISABLE=1
npx prisma generate --schema=./prisma/schema.prisma
npx prisma migrate deploy --schema=./prisma/schema.prisma

echo ""
echo "Iniciando todos os servicos em modo desenvolvimento..."
echo ""

# Server com inspector na porta 9229 para debug
cd /app/server
NODE_ENV=development node_modules/.bin/nodemon \
  --inspect=0.0.0.0:9229 \
  --ignore documents \
  --ignore vector-cache \
  --ignore storage \
  --ignore swagger \
  --trace-warnings \
  index.js &

# Collector com inspector na porta 9230 para debug
cd /app/collector
NODE_ENV=development node_modules/.bin/nodemon \
  --inspect=0.0.0.0:9230 \
  --ignore hotdir \
  --ignore storage \
  --trace-warnings \
  index.js &

# Frontend Vite dev server (--host sobrescreve o "localhost" do vite.config.js)
cd /app/frontend
NODE_ENV=development node_modules/.bin/vite --host 0.0.0.0 --port 3000 &

echo "========================================"
echo "  Servicos rodando:"
echo "  -> Frontend:  http://localhost:3000"
echo "  -> Server:    http://localhost:3001"
echo "  -> Debug:     localhost:9229  (server)"
echo "  -> Debug:     localhost:9230  (collector)"
echo "========================================"
echo ""

wait
