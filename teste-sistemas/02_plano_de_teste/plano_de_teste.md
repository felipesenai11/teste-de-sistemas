# 📋 Plano de Teste – Sistema SRL

## 1. Escopo

Validação completa da API REST do Sistema de Reservas de Laboratório (SRL), incluindo:

* Autenticação
* Salas
* Reservas
* Incidentes
* Regras de Negócio
* Permissões por perfil

---

## 2. Objetivo

Garantir que:

* Todos os requisitos funcionais sejam atendidos
* Todas as regras de negócio sejam respeitadas
* O controle de acesso esteja correto
* A API retorne status HTTP adequados

---

## 3. Estratégia de Teste

### Tipos de Teste

* Teste Funcional
* Teste de Regras de Negócio
* Teste de Segurança (401 / 403)
* Teste de Validação de Dados

### Abordagem

* Testes manuais via Postman
* Testes positivos e negativos
* Validação de conflitos de reserva

---

## 4. Ambiente

* API REST
* Banco de Dados configurado
* Postman ou similar
* Datas no formato YYYY-MM-DD
* Horários no formato HH:MM

---

## 5. Critérios de Entrada

* API disponível
* Banco configurado
* Requisitos aprovados

---

## 6. Critérios de Saída

* 100% dos requisitos testados
* Nenhum erro crítico aberto
* Regras de negócio validadas

---

## 7. Responsáveis

* Testador
* Desenvolvedor
* Administrador do Sistema
