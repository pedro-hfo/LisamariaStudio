# Módulo: marcações

## Responsabilidade

Reservar tempo da única profissional, rejeitando sobreposições. Este exemplo não gere horários de abertura, clientes ou pagamentos.

| Ficheiro em `backend/src/lisamaria/modules/appointments/` | Responsabilidade |
|---|---|
| `domain.py` | Intervalos válidos, entidade e erro de conflito |
| `application.py` | Caso de uso `BookAppointment` |
| `ports.py` | Contratos do repositório e relógio |
| `adapters/memory.py` | Verificação e gravação atómicas em memória |
| `adapters/system_clock.py` | Relógio UTC |
| `adapters/http.py` | Validação de entrada e tradução para HTTP |

## Caminho de leitura

1. Lê `TimeSlot.overlaps`: dois intervalos adjacentes são válidos.
2. Lê `Appointment.occupied_slot`: acrescenta o tempo de preparação.
3. Lê `BookAppointment.execute`: valida e pede uma gravação atómica.
4. Lê `add_if_available`: o teste de conflito e a gravação usam o mesmo lock.
5. Lê o cenário `APT-003`: uma marcação no período de preparação é rejeitada.

A regra é aplicada no servidor. Desativar um botão na interface melhora a experiência, mas não impede pedidos concorrentes.

## Contrato

`POST /api/appointments` recebe `starts_at` em ISO 8601 com fuso horário. Devolve `201` quando aceite, `409` em conflito e `422` em pedidos inválidos. `GET /api/appointments` devolve a agenda de demonstração.

Os testes estão em `backend/tests/modules/appointments/` e `acceptance/backend/appointments/`. A referência é gerada pelo Sphinx a partir das docstrings deste módulo.
