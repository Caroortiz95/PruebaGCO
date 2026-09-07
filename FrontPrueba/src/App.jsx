import './App.css'

function App() {
  return (
    <>
      <section className="seccionPrincipal">
        <h1 className="tituloPrincipal">¡Haz parte de nuestro programa de fidelidad!</h1>
        <p className="descripcionPrincipal">
          Queremos que seas parte de nuestra comunidad. Completa tus datos, elige la marca de tu preferencia y comienza a disfrutar de todos los beneficios que tenemos para ti.
        </p>
        <form className="contenedorFormulario" action="">

          <div className="filaCampos">
            <label className="grupoFormulario" htmlFor="tipoIdentificacion">
              <span className="etiquetaCampo">Tipo de identificación</span>
              <select className="campoSelect" name="" id="tipoIdentificacion"></select>
            </label>

            <label className="grupoFormulario" htmlFor="numeroCedula">
              <span className="etiquetaCampo">Número de cédula</span>
              <input className="campoInput" type="number" id="numeroCedula" />
            </label>
          </div>

          <div className="filaCampos">
            <label className="grupoFormulario" htmlFor="nombres">
              <span className="etiquetaCampo">Nombres</span>
              <input className="campoInput" type="text" id="nombres" />
            </label>

            <label className="grupoFormulario" htmlFor="apellidos">
              <span className="etiquetaCampo">Apellidos</span>
              <input className="campoInput" type="text" id="apellidos" />
            </label>
          </div>

          <label className="grupoFormulario" htmlFor="fechaNacimiento">
            <span className="etiquetaCampo">Fecha de nacimiento</span>
            <input className="campoInput" type="date" id="fechaNacimiento" />
          </label>

          <label className="grupoFormulario" htmlFor="direccion">
            <span className="etiquetaCampo">Dirección</span>
            <input className="campoInput" type="text" id="direccion" />
          </label>

          <div className="filaCampos">
            <label className="grupoFormulario" htmlFor="ciudad">
              <span className="etiquetaCampo">Ciudad</span>
              <select className="campoSelect" name="" id="ciudad"></select>
            </label>

            <label className="grupoFormulario" htmlFor="departamento">
              <span className="etiquetaCampo">Departamento</span>
              <select className="campoSelect" name="" id="departamento"></select>
            </label>
          </div>

          <div className="filaCampos">
            <label className="grupoFormulario" htmlFor="pais">
              <span className="etiquetaCampo">País</span>
              <select className="campoSelect" name="" id="pais"></select>
            </label>

            <label className="grupoFormulario" htmlFor="marca">
              <span className="etiquetaCampo">Marca a la que deseas registrarte</span>
              <select className="campoSelect" name="" id="marca"></select>
            </label>
          </div>

          <button className="botonRegistrar" type="submit">Registrarme</button>
        </form>
      </section>
    </>
  )
}

export default App