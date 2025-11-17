# Gerador de QR Code com FastAPI e Frontend SPA

Este projeto implementa um gerador de QR Code com backend em FastAPI (Python) e frontend estático (HTML/CSS/JS), orquestrados via Docker Compose.

## Arquitetura

- \*\*Backend (Python/FastAPI):\*\* Recebe parâmetros e gera a imagem do QR Code, com suporte a ícone personalizado.
- \*\*Frontend (SPA/Nginx):\*\* Interface simples com formulário para configurar o QR Code e preview em tempo real. O Nginx serve os arquivos estáticos e funciona como proxy reverso para a API.

## Pré-requisitos

- Docker
- Docker Compose (ou Docker Compose V2, que usa o comando \`docker compose\`)

## Como rodar

1. Navegue até o diretório raiz do projeto:
\`\`\`bash
cd qrcode-project
\`\`\`

2. Construa e inicie os contêineres:
\`\`\`bash
# Se você usa docker-compose (versão legada)
docker-compose up --build -d

# Se você usa Docker Compose V2
docker compose up --build -d
\`\`\`

3. Acesse a aplicação:
- Frontend: \`http://localhost\` (porta 80)
- API backend: \`http://localhost:8000\`

4. Parar e remover os contêineres:
\`\`\`bash
docker compose down
\`\`\`

## Endpoints da API

- \`GET /api/health\` - Healthcheck.
- \`POST /api/qrcode\` - Gera o QR Code.
  - Body: \`{ "text": "...", "size": 10, "fill_color": "#000", "icon_url": "..." }\`
  - Retorna: imagem PNG binária ou \`{ "data_url": "..." }\` se \`mode=dataurl\` for passado no body.

## Estrutura de pastas

\`\`\`
qrcode-project/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ api.py
│  │  ├─ schemas.py
│  │  └─ services/
│  │     └─ qrcode_service.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ frontend/
│  ├─ public/
│  │   ├─ index.html
│  │   ├─ style.css
│  │   └─ script.js
│  ├─ nginx.conf
│  └─ Dockerfile
├─ docker-compose.yml
└─ README.md
\`\`\`