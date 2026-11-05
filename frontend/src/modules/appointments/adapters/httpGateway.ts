import type { Appointment, AppointmentGateway } from '../domain';

interface AppointmentDto {
  id: string;
  starts_at: string;
  ends_at: string;
  buffer_minutes: number;
}

function fromDto(dto: AppointmentDto): Appointment {
  if (typeof dto.id !== 'string' || typeof dto.starts_at !== 'string' ||
      typeof dto.ends_at !== 'string' || typeof dto.buffer_minutes !== 'number') {
    throw new Error('Resposta inválida da agenda.');
  }
  return { id: dto.id, startsAt: dto.starts_at, endsAt: dto.ends_at, bufferMinutes: dto.buffer_minutes };
}

async function parseResponse(response: Response): Promise<unknown> {
  if (!response.ok) {
    if (response.status === 409) throw new Error('Este horário já está ocupado. Escolhe outro.');
    if (response.status === 422) throw new Error('Escolhe uma data e hora futuras válidas.');
    throw new Error('Não foi possível contactar a agenda. Tenta novamente.');
  }
  return response.json();
}

/** PT: Adapter HTTP que converte DTOs em objetos do front-end.
 * EN: HTTP adapter converting DTOs into frontend objects.
 */
export const httpAppointmentGateway: AppointmentGateway = {
  async list(signal) {
    const data = await parseResponse(await fetch('/api/appointments', { signal }));
    if (!Array.isArray(data)) throw new Error('Resposta inválida da agenda.');
    return data.map(fromDto);
  },
  async book(startsAt) {
    const data = await parseResponse(await fetch('/api/appointments', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ starts_at: startsAt }),
    }));
    return fromDto(data as AppointmentDto);
  },
};
