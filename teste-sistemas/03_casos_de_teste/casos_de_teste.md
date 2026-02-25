# Casos de Teste

## CT01 – Registrar usuário com dados válidos
* **Requisito:** RF01
* **Descrição:** Validar registro com dados corretos.
* **Pré-condição:** Email não cadastrado.
* **Entrada:** Nome João Silva, Email joao@email.com, Senha Senha123, Perfil USER.
* **Resultado Esperado:** Usuário cadastrado com sucesso. HTTP 201 Created.

## CT02 – Registrar usuário com email duplicado
* **Requisito:** RN01
* **Descrição:** Validar que email não pode ser repetido.
* **Pré-condição:** Email já existente.
* **Entrada:** Nome Maria, Email joao@email.com, Senha Maria123, Perfil USER.
* **Resultado Esperado:** Erro de duplicidade. HTTP 400 Bad Request.

## CT03 – Registrar usuário com senha inválida
* **Requisito:** RN02
* **Descrição:** Validar regra mínima de senha.
* **Pré-condição:** Nenhuma.
* **Entrada:** Nome Carlos, Email carlos@email.com, Senha abcdefg, Perfil USER.
* **Resultado Esperado:** Erro de validação de senha. HTTP 400 Bad Request.

## CT04 – Login com credenciais válidas
* **Requisito:** RF02, RF03
* **Descrição:** Validar autenticação correta.
* **Pré-condição:** Usuário previamente cadastrado.
* **Entrada:** Email joao@email.com, Senha Senha123.
* **Resultado Esperado:** Retornar token válido. HTTP 200 OK.

## CT05 – Login com senha incorreta
* **Requisito:** RF02
* **Descrição:** Validar erro de autenticação.
* **Pré-condição:** Usuário existente.
* **Entrada:** Email joao@email.com, Senha Errada123.
* **Resultado Esperado:** HTTP 401 Unauthorized.

## CT06 – Acesso sem token
* **Requisito:** RN03
* **Descrição:** Validar obrigatoriedade de autenticação.
* **Pré-condição:** Nenhuma.
* **Entrada:** GET /rooms sem header Authorization.
* **Resultado Esperado:** HTTP 401 Unauthorized.

## CT07 – ADMIN criar sala válida
* **Requisito:** RF04
* **Descrição:** Validar criação de sala por ADMIN.
* **Pré-condição:** ADMIN autenticado.
* **Entrada:** Nome Lab 01, Capacidade 30, Recursos Projetor.
* **Resultado Esperado:** Sala criada. HTTP 201 Created.

## CT08 – USER tentar criar sala
* **Requisito:** Permissões
* **Descrição:** Validar restrição para USER.
* **Pré-condição:** USER autenticado.
* **Entrada:** POST /rooms.
* **Resultado Esperado:** HTTP 403 Forbidden.

## CT09 – Criar sala com nome duplicado
* **Requisito:** RN04
* **Descrição:** Validar que não pode repetir nome da sala.
* **Pré-condição:** Lab 01 já cadastrada.
* **Entrada:** Nome Lab 01, Capacidade 20.
* **Resultado Esperado:** HTTP 400 Bad Request.

## CT10 – Criar sala com capacidade inválida
* **Requisito:** RN05
* **Descrição:** Validar capacidade maior que zero.
* **Pré-condição:** ADMIN autenticado.
* **Entrada:** Nome Lab 02, Capacidade 0.
* **Resultado Esperado:** HTTP 400 Bad Request.

## CT11 – Listar salas autenticado
* **Requisito:** RF05
* **Descrição:** Validar listagem de salas.
* **Pré-condição:** Usuário autenticado.
* **Entrada:** GET /rooms.
* **Resultado Esperado:** HTTP 200 OK com lista de salas.

## CT12 – Criar reserva válida
* **Requisito:** RF06, RF08
* **Descrição:** Validar criação sem conflito.
* **Pré-condição:** Sala existente e disponível.
* **Entrada:** ID Sala 1, Data 2026-03-10, Hora 10:00–12:00, Finalidade Aula prática.
* **Resultado Esperado:** Reserva criada com status CONFIRMED. HTTP 201 Created.

## CT13 – Hora início maior que término
* **Requisito:** RN06
* **Descrição:** Validar ordem dos horários.
* **Pré-condição:** Sala existente.
* **Entrada:** Hora 14:00–12:00.
* **Resultado Esperado:** HTTP 400 Bad Request.

## CT14 – Reserva fora do horário permitido
* **Requisito:** RN07
* **Descrição:** Validar horário entre 08:00 e 22:00.
* **Pré-condição:** Sala existente.
* **Entrada:** Hora 07:00–09:00.
* **Resultado Esperado:** HTTP 400 Bad Request.

## CT15 – Conflito de horário
* **Requisito:** RN08
* **Descrição:** Validar interseção de horários.
* **Pré-condição:** Reserva existente 10:00–12:00 mesma sala e data.
* **Entrada:** Hora 11:00–13:00.
* **Resultado Esperado:** HTTP 409 Conflict.

## CT16 – Reserva para sala inexistente
* **Requisito:** RN09
* **Descrição:** Validar existência da sala.
* **Pré-condição:** Sala ID 999 inexistente.
* **Entrada:** ID Sala 999.
* **Resultado Esperado:** HTTP 404 Not Found.

## CT17 – Listar próprias reservas
* **Requisito:** RF07
* **Descrição:** Validar retorno apenas das reservas do usuário logado.
* **Pré-condição:** Usuário com reservas cadastradas.
* **Entrada:** GET /bookings/my.
* **Resultado Esperado:** HTTP 200 OK apenas com reservas do usuário.

## CT18 – Abrir incidente válido
* **Requisito:** RF09, RF11
* **Descrição:** Validar abertura de incidente.
* **Pré-condição:** Sala existente.
* **Entrada:** ID Sala 1, Descrição com mais de 10 caracteres.
* **Resultado Esperado:** Incidente criado com status OPEN. HTTP 201 Created.

## CT19 – Abrir incidente com descrição curta
* **Requisito:** RN10
* **Descrição:** Validar tamanho mínimo da descrição.
* **Pré-condição:** Sala existente.
* **Entrada:** Descrição “Quebrou”.
* **Resultado Esperado:** HTTP 400 Bad Request.

## CT20 – USER tentar fechar incidente
* **Requisito:** RN11
* **Descrição:** Validar permissão de fechamento.
* **Pré-condição:** Incidente OPEN, usuário USER autenticado.
* **Entrada:** PATCH /incidents/1/close.
* **Resultado Esperado:** HTTP 403 Forbidden.

## CT21 – ADMIN fechar incidente aberto
* **Requisito:** RF10, RN12
* **Descrição:** Validar encerramento correto.
* **Pré-condição:** Incidente OPEN, ADMIN autenticado.
* **Entrada:** PATCH /incidents/1/close.
* **Resultado Esperado:** Status alterado para CLOSED. HTTP 200 OK.

## CT22 – Fechar incidente já fechado
* **Requisito:** RN12
* **Descrição:** Validar que não é possível fechar incidente CLOSED.
* **Pré-condição:** Incidente CLOSED.
* **Entrada:** PATCH /incidents/1/close.
* **Resultado Esperado:** HTTP 400 Bad Request.

## CT23 – Token inválido
* **Requisito:** Regras de Autenticação
* **Descrição:** Validar token malformado.
* **Pré-condição:** Nenhuma.
* **Entrada:** Authorization Bearer token_invalido.
* **Resultado Esperado:** HTTP 401 Unauthorized.

## CT24 – Token expirado
* **Requisito:** Regras de Autenticação
* **Descrição:** Validar token expirado.
* **Pré-condição:** Token expirado.
* **Entrada:** Requisição autenticada com token expirado.
* **Resultado Esperado:** HTTP 401 Unauthorized.
