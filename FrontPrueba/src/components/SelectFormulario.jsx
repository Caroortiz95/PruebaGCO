export default function SelectFormulario({ etiqueta, id, valor, opciones, onChange, invalido = false }) {
  return (
    <label className="grupoFormulario" htmlFor={id}>
      <span className="etiquetaCampo">{etiqueta}</span>
      <select
        className={`campoSelect${invalido ? ' campoInvalido' : ''}`}
        id={id}
        value={valor}
        onChange={onChange}
      >
        <option value="">Selecciona una opción</option>
        {opciones.map((opcion) => (
          <option key={opcion.id} value={opcion.id}>
            {opcion.nombre}
          </option>
        ))}
      </select>
    </label>
  )
}