import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { BookingPanel } from '../../../frontend/src/modules/appointments/ui/BookingPanel';
import type { Appointment, AppointmentGateway } from '../../../frontend/src/modules/appointments/domain';

const appointment: Appointment = {
  id: 'demo', startsAt: '2030-01-10T10:00:00Z', endsAt: '2030-01-10T11:00:00Z', bufferMinutes: 15,
};

function gateway(overrides: Partial<AppointmentGateway> = {}): AppointmentGateway {
  return { list: vi.fn().mockResolvedValue([]), book: vi.fn().mockResolvedValue(appointment), ...overrides };
}

async function completeForm() {
  await screen.findByText(/Ainda não há marcações/);
  fireEvent.change(screen.getByLabelText('Data e hora'), { target: { value: '2030-01-10T10:00' } });
  await userEvent.click(screen.getByRole('button', { name: /Criar marcação/ }));
}

describe('appointments / marcações — acceptance / aceitação', () => {
  it('[UI-001] shows confirmation after booking / mostra confirmação após marcar', async () => {
    const port = gateway();
    render(<BookingPanel gateway={port} />);
    await completeForm();
    expect(await screen.findByRole('status')).toHaveTextContent('Marcação de demonstração criada.');
    expect(port.book).toHaveBeenCalledWith(new Date('2030-01-10T10:00').toISOString());
    expect(screen.getAllByRole('listitem')).toHaveLength(1);
  });

  it('[UI-002] explains an unavailable slot / explica um horário indisponível', async () => {
    render(<BookingPanel gateway={gateway({ book: vi.fn().mockRejectedValue(new Error('Horário indisponível.')) })} />);
    await completeForm();
    expect(await screen.findByRole('alert')).toHaveTextContent('Horário indisponível.');
    expect(screen.queryByRole('listitem')).not.toBeInTheDocument();
  });

  it('[UI-003] prevents repeat submission while pending / impede repetir um pedido pendente', async () => {
    let finish!: (value: Appointment) => void;
    const port = gateway({ book: vi.fn(() => new Promise<Appointment>(resolve => { finish = resolve; })) });
    render(<BookingPanel gateway={port} />);
    await completeForm();
    expect(screen.getByRole('button', { name: /A marcar/ })).toBeDisabled();
    await userEvent.click(screen.getByRole('button', { name: /A marcar/ }));
    expect(port.book).toHaveBeenCalledTimes(1);
    finish(appointment);
    await screen.findByText('Marcação de demonstração criada.');
  });

  it('[UI-004] reports loading failure / comunica falha ao carregar', async () => {
    render(<BookingPanel gateway={gateway({ list: vi.fn().mockRejectedValue(new Error('Offline')) })} />);
    expect(await screen.findByRole('alert')).toHaveTextContent('Não foi possível carregar a agenda.');
  });
});
