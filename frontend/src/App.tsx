import { BookingPanel } from './modules/appointments/ui/BookingPanel';
import { httpAppointmentGateway } from './modules/appointments/adapters/httpGateway';

export function App() {
  const preview = import.meta.env.MODE === 'pages';
  const baseUrl = import.meta.env.BASE_URL;
  const docsUrl = preview ? `${baseUrl}docs` : `http://127.0.0.1:${Number(window.location.port || 3000) + 1}`;
  return <>
    <header className="site-header"><a className="brand" href={baseUrl}>lisamaria<span>STUDIO</span></a>
      <a href={`${docsUrl}/pt/index.html`}>Guia do projeto <span aria-hidden="true">↗</span></a></header>
    <main>
      <section className="intro" aria-labelledby="page-title">
        <p className="eyebrow">CUIDAR · RESPIRAR · RECOMEÇAR</p>
        <h1 id="page-title">O tempo<br />de <em>desacelerar.</em></h1>
        <p>Um espaço para cuidar de ti.<br />Uma agenda pensada com tempo.</p>
        <div className="studio-mark" aria-hidden="true"><span /><span /><span /></div>
        <aside className="demo-note"><strong>{preview ? 'Projeto em desenvolvimento' : 'Laboratório local'}</strong><p>Esta é uma demonstração para aprender a arquitetura. Não envia marcações reais nem cobra pagamentos.{!preview && ' A agenda reinicia com o backend.'}</p></aside>
      </section>
      {preview ? <section className="booking-panel" aria-labelledby="preview-title">
        <p className="eyebrow">01 / CONHECER O PROJETO</p>
        <h2 id="preview-title">Um momento para ti.</h2>
        <p className="muted">Estamos a construir uma agenda para um estúdio de massagens, com uma única profissional.</p>
        <p className="muted">Esta versão no GitHub Pages apresenta o projeto e a sua documentação. Para experimentar marcações de exemplo, inicia a aplicação local com o backend Python.</p>
        <p><a href={`${docsUrl}/pt/getting-started.html`}>Experimentar localmente ↗</a></p>
        <div className="schedule"><h3>Aprender, passo a passo</h3>
          <p className="muted">React e TypeScript na interface. Python, DDD, arquitetura hexagonal e BDD no backend.</p>
          <p><a href={`${docsUrl}/pt/index.html`}>Guia em português ↗</a></p>
          <p><a href={`${docsUrl}/en/index.html`} lang="en">Read the English guide ↗</a></p>
        </div>
      </section> : <BookingPanel gateway={httpAppointmentGateway} />}
    </main>
    <footer><span>LISAMARIA STUDIO</span><span>React · Python · Uma base para construir.</span>
      <a href={preview ? `${docsUrl}/pt/reference/index.html` : '/api/docs'}>{preview ? 'Referência do código' : 'Referência HTTP'} ↗</a></footer>
  </>;
}
