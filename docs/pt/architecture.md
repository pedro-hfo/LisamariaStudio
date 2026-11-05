# Arquitetura, por partes

## A ideia essencial

A regra «uma profissional não pode ter duas marcações sobrepostas» pertence ao negócio. Deve ser possível testá-la sem navegador, servidor HTTP ou base de dados.

**DDD — Domain-Driven Design** orienta o modelo a partir da linguagem e das regras do negócio. **Arquitetura hexagonal** permite ligar esse modelo a tecnologias através de contratos, chamados *ports*, e implementações, chamadas *adapters*.

```text
BookingPanel → useAppointments → AppointmentGateway
                                      ↓ HTTP adapter
                               POST /api/appointments
                                      ↓ HTTP adapter
                               BookAppointment
                                 ↓         ↓
                             domínio     ports
                                           ↑
                                  adapters concretos
```

A seta da dependência aponta para dentro: os adapters conhecem as portas e o domínio. O domínio não conhece os adapters. `bootstrap.py` faz a ligação (*composition root*).

## Padrões presentes

| Padrão | Onde | Porque existe |
|---|---|---|
| Value object | `TimeSlot` | Compara intervalos pelo valor e impede intervalos inválidos |
| Entity | `Appointment` | Mantém identidade própria através de um ID |
| Use case | `BookAppointment` | Coordena uma intenção completa do utilizador |
| Port / interface | `AppointmentRepository`, `Clock` | Define o que o caso de uso precisa |
| Adapter | memória, relógio, HTTP | Liga os contratos a tecnologias concretas |
| Dependency injection | construtores e `bootstrap.py` | Permite trocar colaboradores sem mudar regras |
| Composition | `BookingPanel` recebe `gateway` | Permite reutilizar o componente e testá-lo |
| Custom hook | `useAppointments` | Separa coordenação assíncrona da apresentação |

```{hint}
*Port* traduz-se aqui por **porta/contrato**. Não é uma porta TCP. *Adapter* pode ser lido como **adaptador**. Mantemos os nomes ingleses no código para facilitar a pesquisa na literatura.
```

## Crescer quando necessário

Começamos com um monólito modular. O módulo `appointments` é uma primeira fronteira de negócio; ainda não afirmamos que seja o bounded context definitivo. Os ficheiros de domínio e aplicação só serão divididos quando existirem conceitos que o justifiquem.

A futura persistência terá de garantir a exclusão de horários na própria transação da base de dados. O lock atual protege apenas um processo de demonstração. SIBS entrará através de uma porta de pagamentos; o domínio não deverá importar o SDK nem os payloads da SIBS.

Não há eventos de domínio, CQRS ou microserviços nesta primeira base. Serão decisões motivadas por necessidades concretas, registadas em ADRs.
