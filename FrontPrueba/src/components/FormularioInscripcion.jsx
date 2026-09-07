import { useFormularioInscripcion } from '../hooks/useFormularioInscripcion'
import CampoFormulario from './CampoFormulario'
import SelectFormulario from './SelectFormulario'

export default function FormularioInscripcion() {
  const {
    listaTiposId,
    listaPaises,
    listaMarcas,
    listaDepartamentos,
    listaCiudades,
    form,
    errores,
    mensaje,
    enviando,
    manejarCambio,
    manejarEnvio,
  } = useFormularioInscripcion()

  return (
    <form className="contenedorFormulario" onSubmit={manejarEnvio} noValidate>
        <div className="filaCampos">
          <SelectFormulario
            etiqueta="Tipo de identificación"
            id="tipoIdentificacion"
            valor={form.tipoIdentificacion}
            opciones={listaTiposId}
            onChange={manejarCambio}
            invalido={errores.tipoIdentificacion}
          />
          <CampoFormulario
            etiqueta="Número de cédula"
            id="numeroCedula"
            tipo="number"
            valor={form.numeroCedula}
            onChange={manejarCambio}
            invalido={errores.numeroCedula}
          />
        </div>

        <div className="filaCampos">
          <CampoFormulario
            etiqueta="Nombres"
            id="nombres"
            valor={form.nombres}
            onChange={manejarCambio}
            invalido={errores.nombres}
          />
          <CampoFormulario
            etiqueta="Apellidos"
            id="apellidos"
            valor={form.apellidos}
            onChange={manejarCambio}
            invalido={errores.apellidos}
          />
        </div>

        <CampoFormulario
          etiqueta="Fecha de nacimiento"
          id="fechaNacimiento"
          tipo="date"
          valor={form.fechaNacimiento}
          onChange={manejarCambio}
          invalido={errores.fechaNacimiento}
        />

        <CampoFormulario
          etiqueta="Dirección"
          id="direccion"
          valor={form.direccion}
          onChange={manejarCambio}
          invalido={errores.direccion}
        />

        <div className="filaCampos">
          <SelectFormulario
            etiqueta="País"
            id="pais"
            valor={form.pais}
            opciones={listaPaises}
            onChange={manejarCambio}
            invalido={errores.pais}
          />
          <SelectFormulario
            etiqueta="Departamento"
            id="departamento"
            valor={form.departamento}
            opciones={listaDepartamentos}
            onChange={manejarCambio}
            invalido={errores.departamento}
          />
        </div>

        <div className="filaCampos">
          <SelectFormulario
            etiqueta="Ciudad"
            id="ciudad"
            valor={form.ciudad}
            opciones={listaCiudades}
            onChange={manejarCambio}
            invalido={errores.ciudad}
          />
          <SelectFormulario
            etiqueta="Marca a la que deseas registrarte"
            id="marca"
            valor={form.marca}
            opciones={listaMarcas}
            onChange={manejarCambio}
            invalido={errores.marca}
          />
        </div>

        <button className="botonRegistrar" type="submit" disabled={enviando}>
          {enviando ? 'Registrando...' : 'Registrarme'}
        </button>

        {mensaje && (
          <div className={`mensaje ${mensaje.tipo === 'exito' ? 'mensajeExito' : 'mensajeError'}`}>
            {mensaje.texto}
          </div>
        )}
      </form>
  )
}