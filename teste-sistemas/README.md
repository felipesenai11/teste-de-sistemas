# 🧪 Sistema de Reservas de Laboratório (SRL)

Projeto desenvolvido como parte das disciplinas de Engenharia de Software e Teste de Sistemas.

O sistema evoluiu em duas etapas:

1. 📘 Modelagem e Documentação
2. 💻 Implementação da API REST

---

# 📌 Sobre o Sistema

O SRL (Sistema de Reservas de Laboratório) permite:

* Cadastro de usuários (ADMIN / USER)
* Cadastro de salas
* Criação de reservas
* Registro e controle de incidentes técnicos

A aplicação é uma API REST com autenticação via Bearer Token.

---

# 🏗 Estrutura do Projeto

```
.
├── 01_requisitos
├── 02_api
├── 02_plano_de_teste
├── 03_casos_de_teste
├── 04_matriz_rastreabilidade
├── 05_registro_de_falhas
│
├── main.py
├── models.py
├── schemas.py
├── auth.py
├── database.py
├── routers/
├── requirements.txt
└── README.md
```

---

# 🧩 Etapa 1 – Documentação

Inclui:

* Documento de Requisitos
* Plano de Teste
* Casos de Teste
* Matriz de Rastreabilidade
* Registro de Falhas

Objetivo: Garantir qualidade antes da implementação.

---

# 💻 Etapa 2 – Implementação da API

Tecnologias utilizadas:

* Python
* FastAPI
* SQLite
* JWT para autenticação

---

# 🚀 Como Executar a API

1. Criar ambiente virtual:
   python -m venv venv

2. Ativar ambiente:
   Windows:
   venv\Scripts\activate

   Linux/Mac:
   source venv/bin/activate

3. Instalar dependências:
   pip install -r requirements.txt

4. Executar aplicação:
   uvicorn main:app --reload

5. Acessar documentação automática:
   http://localhost:8000/docs

---

# 🔐 Autenticação

Todas as requisições protegidas exigem:

Authorization: Bearer {token}

---

# 🎯 Objetivo Acadêmico

Demonstrar aplicação prática de:

* Engenharia de Requisitos
* Planejamento de Testes
* Rastreabilidade
* Implementação de API REST
* Controle de Acesso
* Regras de Negócio

---

# 👨‍💻 Autor

Felipe Pereira, Bruno dos Anjos
Sistema SRL
