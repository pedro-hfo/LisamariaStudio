import { useCallback, useEffect, useRef, useState } from 'react';
import type { Appointment, AppointmentGateway } from '../domain';

/** PT: Custom hook: gere estado assíncrono e coordena a porta da agenda.
 * EN: Custom hook: manages asynchronous state and coordinates the schedule port.
 */
export function useAppointments(gateway: AppointmentGateway) {
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [confirmation, setConfirmation] = useState('');
  const saveInProgress = useRef(false);
  const revision = useRef(0);

  useEffect(() => {
    const controller = new AbortController();
    const currentRevision = revision.current;
    gateway.list(controller.signal)
      .then(data => {
        if (!controller.signal.aborted && revision.current === currentRevision) {
          setAppointments(data);
        }
      })
      .catch(() => {
        if (!controller.signal.aborted) setError('Não foi possível carregar a agenda.');
      })
      .finally(() => { if (!controller.signal.aborted) setLoading(false); });
    return () => controller.abort();
  }, [gateway]);

  const book = useCallback(async (startsAt: string) => {
    if (saveInProgress.current) return;
    saveInProgress.current = true;
    setSaving(true);
    setError('');
    setConfirmation('');
    try {
      const appointment = await gateway.book(startsAt);
      revision.current += 1;
      setAppointments(current => [...current, appointment].sort((a, b) =>
        Date.parse(a.startsAt) - Date.parse(b.startsAt)));
      setConfirmation('Marcação de demonstração criada.');
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : 'Não foi possível criar a marcação.');
    } finally {
      saveInProgress.current = false;
      setSaving(false);
    }
  }, [gateway]);

  return { appointments, loading, saving, error, confirmation, book };
}
