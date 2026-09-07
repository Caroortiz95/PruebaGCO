import './App.css'
import FormularioInscripcion from './components/FormularioInscripcion'
import Presentacion from './components/Presentacion'

function App() {
  return (
    <>
      <section className="seccionPrincipal">
        <Presentacion />
        <FormularioInscripcion />
      </section>
    </>
  )
}

export default App