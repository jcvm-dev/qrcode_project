# Gerador de QR Code com FastAPI e Frontend SPA

Este projeto implementa um gerador de QR Code com um backend em FastAPI (Python) e um frontend estático (HTML/CSS/JS) orquestrados via Docker Compose.

## Arquitetura

- **Backend (Python/FastAPI):** Responsável por receber os parâmetros e gerar a imagem do QR Code, incluindo a funcionalidade de ícone personalizado.
- **Frontend (SPA/Nginx):** Uma interface simples com formulário para configurar o QR Code e um preview em tempo real. O Nginx atua como servidor de arquivos estáticos e proxy reverso para a API.

## Pré-requisitos

- Docker
- Docker Compose (ou Docker Compose V2, que usa o comando \`docker compose\`)

## Como Rodar

1.  **Navegue até o diretório raiz do projeto:**
    \`\`\`bash
    cd qrcode-project
    \`\`\`

2.  **Construa e inicie os contêineres:**
    \`\`\`bash
    # Se você usa docker-compose (versão antiga)
    docker-compose up --build -d

    # Se você usa docker compose (versão V2)
    docker compose up --build -d
    \`\`\`

3.  **Acesse a Aplicação:**
    O frontend estará disponível em \`http://localhost\` (porta 80).
    A API do backend estará acessível diretamente em \`http://localhost:8000\`.

4.  **Parar e Remover os Contêineres:**
    \`\`\`bash
    docker compose down
    \`\`\`

## Endpoints da API

- \`GET /api/health\` - Healthcheck.
- \`POST /api/qrcode\` - Gera o QR Code.
  - Body: \`{ "text": "...", "size": 10, "fill_color": "#000", "icon_url": "..." }\`
  - Retorna: Imagem PNG binária ou \`{ "data_url": "..." }\` se \`mode=dataurl\` for passado no body.

## Estrutura de Pastas

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
