import { BookingPanel } from './modules/appointments/ui/BookingPanel';
import { httpAppointmentGateway } from './modules/appointments/adapters/httpGateway';

export function App() {
  const docsUrl = `http://127.0.0.1:${Number(window.location.port || 3000) + 1}`;
  return <>
    <header className="site-header"><a className="brand" href="/">lisamaria<span>STUDIO</span></a>
      <a href={`${docsUrl}/pt/index.html`}>Guia do projeto <span aria-hidden="true">↗</span></a></header>
    <main>
      <section className="intro" aria-labelledby="page-title">
        <p className="eyebrow">CUIDAR · RESPIRAR · RECOMEÇAR</p>
        <h1 id="page-title">O tempo<br />de <em>desacelerar.</em></h1>
        <p>Um espaço para cuidar de ti.<br />Uma agenda pensada com tempo.</p>
        <div className="studio-mark" aria-hidden="true"><span /><span /><span /></div>
        <aside className="demo-note"><strong>Laboratório local</strong><p>Esta é uma demonstração para aprender a arquitetura. Não envia marcações reais nem cobra pagamentos. A agenda reinicia com o backend.</p></aside>
      </section>
      <BookingPanel gateway={httpAppointmentGateway} />
    </main>
    <footer><span>LISAMARIA STUDIO</span><span>React · Python · Uma base para construir.</span>
      <a href="/api/docs">Referência HTTP ↗</a></footer>
  </>;
}
