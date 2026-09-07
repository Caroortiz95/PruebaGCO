export default function CampoFormulario({ etiqueta, id, tipo = 'text', valor, onChange, invalido = false }) {
  return (
    <label className="grupoFormulario" htmlFor={id}>
      <span className="etiquetaCampo">{etiqueta}</span>
      <input
        className={`campoInput${invalido ? ' campoInvalido' : ''}`}
        type={tipo}
        id={id}
        value={valor}
        onChange={onChange}
      />
    </label>
  )
}