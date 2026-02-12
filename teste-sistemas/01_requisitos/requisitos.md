# Sistema de Reservas de Laboratório (SRL)
## Documento de Requisitos – Versão 1.0

# 1. Contexto do Sistema

A faculdade necessita de um sistema para gerenciar:

- Cadastro de usuários
- Cadastro de salas de laboratório
- Reservas de salas
- Registro de incidentes técnicos

O sistema será disponibilizado como API REST e será utilizado por:

- Administradores
- Professores
- Alunos

A autenticação será obrigatória para todas as operações, exceto registro e login.


# 2. Perfis de Usuário

O sistema possui dois perfis:

- **ADMIN**
- **USER**

## Permissões

| Operação | ADMIN | USER |
|----------|--------|------|
| Registrar usuário | ✔ | ✔ |
| Criar sala | ✔ | ✖ |
| Listar salas | ✔ | ✔ |
| Criar reserva | ✔ | ✔ |
| Listar próprias reservas | ✔ | ✔ |
| Abrir incidente | ✔ | ✔ |
| Fechar incidente | ✔ | ✖ |

---

# 3. Requisitos Funcionais (RF)

## Módulo 1 – Autenticação

**RF01** – O sistema deve permitir registrar usuário informando:
- Nome
- Email
- Senha
- Perfil (ADMIN ou USER)

**RF02** – O sistema deve permitir login com email e senha válidos.

**RF03** – O sistema deve retornar token de autenticação válido após login bem-sucedido.

---

## Módulo 2 – Salas

**RF04** – O sistema deve permitir que ADMIN cadastre sala contendo:
- Nome
- Capacidade
- Lista de recursos (ex: projetor, ar-condicionado)

**RF05** – O sistema deve permitir listar todas as salas cadastradas.

---

## Módulo 3 – Reservas

**RF06** – O sistema deve permitir que usuário autenticado crie reserva informando:
- ID da sala
- Data
- Hora de início
- Hora de término
- Finalidade da reserva

**RF07** – O sistema deve permitir que o usuário visualize suas próprias reservas.

**RF08** – Ao criar reserva válida, o sistema deve registrar status como CONFIRMED.

---

## Módulo 4 – Incidentes

**RF09** – O sistema deve permitir abrir incidente vinculado a uma sala.

**RF10** – O sistema deve permitir que ADMIN finalize incidente aberto.

**RF11** – Ao abrir incidente, o status deve ser OPEN.

**RF12** – Ao finalizar incidente, o status deve ser alterado para CLOSED.

---

# 4. Regras de Negócio (RN)

## Autenticação

**RN01** – O email do usuário deve ser único no sistema.

**RN02** – A senha deve possuir no mínimo 8 caracteres contendo pelo menos:
- 1 letra
- 1 número

**RN03** – Token é obrigatório para acesso aos módulos Salas, Reservas e Incidentes.

---

## Salas

**RN04** – Nome da sala não pode ser duplicado.

**RN05** – Capacidade da sala deve ser maior que 0.

---

## Reservas

**RN06** – Hora de início deve ser menor que hora de término.

**RN07** – Reservas só podem ser feitas entre 08:00 e 22:00.

**RN08** – Não pode haver conflito de horário para a mesma sala na mesma data.

(Conflito ocorre quando há interseção parcial ou total entre intervalos.)

**RN09** – A sala deve existir para que a reserva seja criada.

---

## Incidentes

**RN10** – Descrição do incidente deve possuir no mínimo 10 caracteres.

**RN11** – Apenas ADMIN pode finalizar incidente.

**RN12** – Incidente só pode ser finalizado se estiver com status OPEN.

---

# 5. Endpoints da API

## Autenticação

POST /auth/register  
POST /auth/login  

---

## Salas

POST /rooms  
GET /rooms  

---

## Reservas

POST /bookings  
GET /bookings/my  

---

## Incidentes

POST /incidents  
PATCH /incidents/{id}/close  

---

# 6. Regras de Autenticação

- O token deve ser enviado no header:

Authorization: Bearer {token}

- Requisições sem token devem retornar 401.
- Usuário sem permissão adequada deve retornar 403.

---

# 7. Considerações Gerais

- Todas as respostas devem retornar status HTTP adequado.
- Em caso de erro, o sistema deve retornar mensagem descritiva.
- O sistema não possui interface gráfica, apenas API REST.
- Todas as datas devem seguir padrão ISO (YYYY-MM-DD).
- Horários devem seguir formato HH:MM (24h).

---

# Fim do Documento