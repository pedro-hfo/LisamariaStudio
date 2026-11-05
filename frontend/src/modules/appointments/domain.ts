/** PT: Entidade de marcação recebida pelo front-end.
 * EN: Appointment entity received by the frontend.
 */
export interface Appointment {
  id: string;
  startsAt: string;
  endsAt: string;
  bufferMinutes: number;
}

/** PT: Porta de acesso à agenda; a interface não conhece fetch.
 * EN: Schedule access port; the UI does not know about fetch.
 */
export interface AppointmentGateway {
  list(signal?: AbortSignal): Promise<Appointment[]>;
  book(startsAt: string): Promise<Appointment>;
}
