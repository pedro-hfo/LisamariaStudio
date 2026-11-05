# language: pt
@appointments
Funcionalidade: Marcar tempo com a única profissional do estúdio
  Uma sessão dura 60 minutos e precisa de 15 minutos de preparação.
  Estes são exemplos de aprendizagem, não políticas comerciais aprovadas.

  @APT-001
  Cenário: Marcar um horário disponível
    Dado que a profissional tem a agenda vazia
    Quando peço uma marcação às "2030-01-10T10:00:00+00:00"
    Então a marcação é aceite
    E a agenda contém 1 marcação

  @APT-002
  Cenário: Recusar uma marcação sobreposta
    Dado que existe uma marcação às "2030-01-10T10:00:00+00:00"
    Quando peço uma marcação às "2030-01-10T10:30:00+00:00"
    Então o horário está indisponível
    E a agenda contém 1 marcação

  @APT-003
  Cenário: Preservar o tempo de preparação
    Dado que existe uma marcação às "2030-01-10T10:00:00+00:00"
    Quando peço uma marcação às "2030-01-10T11:00:00+00:00"
    Então o horário está indisponível

  @APT-004
  Cenário: Marcar imediatamente após a preparação
    Dado que existe uma marcação às "2030-01-10T10:00:00+00:00"
    Quando peço uma marcação às "2030-01-10T11:15:00+00:00"
    Então a marcação é aceite
    E a agenda contém 2 marcações

  @APT-005
  Cenário: Recusar um horário passado
    Dado que a profissional tem a agenda vazia
    Quando peço uma marcação às "2029-12-31T10:00:00+00:00"
    Então o pedido é inválido
