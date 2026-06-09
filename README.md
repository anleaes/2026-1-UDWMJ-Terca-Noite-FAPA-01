# 2026-1-UDWJM-Terca-Noite-FAPA-01

# ClinicApp — Sistema de Gestão de Clínica Médica

Sistema web para gerenciamento de clínica médica, desenvolvido com Django no back-end e Vue.js no front-end.

## Tecnologias Utilizadas

- **Python** 3.x
- **Django** 5.2.8
- **Django REST Framework** 3.17.1
- **Django CORS Headers** 4.9.0
- **Oracle Database** (oracledb 4.0.1)
- **python-decouple** 3.8 — gerenciamento de variáveis de ambiente
- **Vue.js** — front-end (repositório separado)

## Funcionalidades

- Cadastro de pacientes com histórico médico automático
- Cadastro de médicos com CRM e especialidade
- Agendamento e gestão de consultas com múltiplos diagnósticos (CID-10)
- Solicitação e acompanhamento de exames
- Emissão de receitas com múltiplos medicamentos
- API REST completa para consumo pelo front-end Vue.js

## Estrutura dos Apps

| App | Descrição |
|-----|-----------|
| `core` | Página inicial |
| `persons` | Model base de pessoa (herdado por paciente e médico) |
| `patients` | Gestão de pacientes |
| `doctors` | Gestão de médicos |
| `consults` | Gestão de consultas |
| `exams` | Gestão de exames |
| `prescriptions` | Gestão de receitas |
| `prescriptionitems` | Itens de cada receita |
| `cids` | Cadastro de CIDs (CID-10) |
| `medications` | Cadastro de medicamentos |
| `medicalhistories` | Histórico médico dos pacientes |

## Como Rodar o Projeto

### 1. Clonar o repositório

git clone <url-do-repositorio>
cd 2026-1-UDWMJ-Terca-Noite-FAPA-01

### 2. Instalar as dependências

pip install -r requirements.txt

### 3. Configurar variáveis de ambiente

Crie um arquivo .env na raiz do projeto com as credenciais do banco Oracle:

DB_HOST=seu_host
DB_PORT=sua_porta
DB_SERVICE=seu_service
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

### 4. Rodar as migrations

python manage.py migrate

### 5. Iniciar o servidor

python manage.py runserver

O sistema estará disponível em http://localhost:8000

## Endpoints da API

Base URL: /api/

| Endpoint | Descrição |
|----------|-----------|
| /api/patients/ | CRUD de pacientes |
| /api/doctors/ | CRUD de médicos |
| /api/consults/ | CRUD de consultas |
| /api/exams/ | CRUD de exames |
| /api/prescriptions/ | CRUD de receitas |
| /api/prescriptionitems/ | CRUD de itens de receita |
| /api/cids/ | CRUD de CIDs |
| /api/medications/ | CRUD de medicamentos |
| /api/medicalhistories/ | CRUD de históricos médicos |

Todos os endpoints suportam os métodos: GET, POST, PUT, PATCH, DELETE

## Integrantes

-Milena Alves de Lima
-Lucas Veras Amui