# Plano de Teste – Sistema SRL

## 1. Escopo
O teste abrange todas as funcionalidades descritas no Documento de Requisitos v1.0, como: Módulos de Autenticação (Login/Registro), Salas, Reservas e Incidentes; Validação das Regras de Negócio (RN01 a RN12); Verificação de segurança baseada em perfis (ADMIN vs USER).

## 2. Objetivo
Garantir que a API processe as requisições corretamente, respeite as restrições de horários e permissões, e retorne os códigos de status HTTP apropriados (ex: 201 Created, 403 Forbidden, 400 Bad Request).

## 3. Estratégia de Teste
Vamos usar o Swagger para fazer "perguntas" ao sistema e ver se a "resposta" é a correta.

Testes de Sucesso: Mandar os dados certinhos e ver se ele aceita.
Testes de Erro: Tentar quebrar as regras (tipo colocar uma senha curta) e ver se o sistema percebe e avisa o erro.


## 4. Ambiente
Ferramentas: Swagger e o Banco de Dados de teste.
Padrão de Dados: Datas em ISO (YYYY-MM-DD) e horários em HH:MM.

## 5. Critérios de Entrada
O documento de requisitos.
O código do sistema pronto.
API rodando em ambiente local.

## 6. Critérios de Saída
100% dos casos de teste executados.
Nenhum erro crítico (Bug) de segurança ou regra de negócio (ex: reserva duplicada) pendente.

## 7. Responsáveis
Desenvolvedor/Tester: Felipe Pereira Silva
Revisor: Israel de Marcos Ferreira da Silva
