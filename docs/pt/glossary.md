# Linguagem ubíqua / Ubiquitous language

Usamos os mesmos conceitos na conversa, nos cenários e nos módulos. A língua do código é inglês; os guias e cenários existem em PT e EN.

| Português | English / código | Significado |
|---|---|---|
| Profissional | Practitioner | A única pessoa que presta as massagens |
| Marcação | Appointment | Reserva de um intervalo para uma sessão |
| Horário | TimeSlot | Instante de início e fim, com fuso horário |
| Sessão | Session | Tempo dedicado à massagem |
| Preparação | Preparation buffer | Tempo ocupado depois da sessão |
| Horário indisponível | SlotUnavailable | Conflito com sessão ou preparação existente |
| Marcar | BookAppointment | Intenção de criar uma marcação |
| Agenda | Schedule | Conjunto de marcações da profissional |
| Pagamento | Payment | Conceito previsto; ainda não implementado |

**Hint:** “booking” é a ação/processo de marcar; “appointment” é a marcação resultante. Evitamos “event” para uma sessão individual de massagem.

Os IDs `APT-001` e `UI-001` são estáveis entre traduções. Uma mudança de termo deve atualizar glossário, código, cenários e os dois guias.
