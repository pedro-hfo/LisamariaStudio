import { useState } from 'react';
import type { FormEvent } from 'react';
import type { AppointmentGateway } from '../domain';
import { useAppointments } from '../application/useAppointments';

/** PT: Formulário acessível; recebe a porta por composição.
 * EN: Accessible form; receives its port through composition.
 */
export function BookingPanel({ gateway }: { gateway: AppointmentGateway }) {
  const { appointments, loading, saving, error, confirmation, book } = useAppointments(gateway);
  const [startsAt, setStartsAt] = useState('');
  const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (startsAt && Number.isFinite(Date.parse(startsAt))) {
      void book(new Date(startsAt).toISOString());
    }
  }

  return <section className="booking-panel" aria-labelledby="booking-title">
    <p className="eyebrow">01 / EXPERIMENTAR A AGENDA</p>
    <h2 id="booking-title">Um momento para ti.</h2>
    <p className="muted">Sessão de exemplo de 60 minutos, com 15 minutos de preparação entre marcações.</p>
    <form onSubmit={submit}>
      <label htmlFor="starts-at">Data e hora</label>
      <input id="starts-at" type="datetime-local" required value={startsAt}
        onChange={event => setStartsAt(event.target.value)} aria-describedby="timezone" />
      <p id="timezone" className="field-hint">Fuso horário deste dispositivo: {timezone}</p>
      <button type="submit" disabled={saving || loading}>{saving ? 'A marcar…' : 'Criar marcação de exemplo'} <span aria-hidden="true">↗</span></button>
    </form>
    {error && <p role="alert" className="feedback error">{error}</p>}
    {confirmation && <p role="status" className="feedback success">{confirmation}</p>}
    <div className="schedule">
      <h3>Agenda desta sessão <span>{appointments.length.toString().padStart(2, '0')}</span></h3>
      {loading ? <p role="status">A carregar a agenda…</p> : appointments.length === 0
        ? <p className="muted">Ainda não há marcações. Experimenta criar a primeira.</p>
        : <ul>{appointments.map(appointment => <li key={appointment.id}>
          <time dateTime={appointment.startsAt}>{new Intl.DateTimeFormat('pt-PT', {
            dateStyle: 'medium', timeStyle: 'short',
          }).format(new Date(appointment.startsAt))}</time><span>60 min</span>
        </li>)}</ul>}
    </div>
  </section>;
}
