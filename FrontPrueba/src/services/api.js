const API_BASE = 'http://localhost:5000'

export async function obtenerLista(endpoint, params = {}) {
  const query = new URLSearchParams(params).toString()
  const url = `${API_BASE}/api/${endpoint}${query ? `?${query}` : ''}`
  const respuesta = await fetch(url)
  return respuesta.json()
}

export async function crearInscripcion(payload) {
  const respuesta = await fetch(`${API_BASE}/api/inscripciones`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
  const datos = await respuesta.json()
  return { ok: respuesta.ok, datos }
}