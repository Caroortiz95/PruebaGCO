import { useEffect, useState } from 'react'
import { crearInscripcion, obtenerLista } from '../services/api'

const formInicial = {
  tipoIdentificacion: '',
  numeroCedula: '',
  nombres: '',
  apellidos: '',
  fechaNacimiento: '',
  direccion: '',
  ciudad: '',
  departamento: '',
  pais: '',
  marca: '',
}

const camposObligatorios = [
  'tipoIdentificacion',
  'numeroCedula',
  'nombres',
  'apellidos',
  'fechaNacimiento',
  'direccion',
  'pais',
  'departamento',
  'ciudad',
  'marca',
]

function construirPayload(form) {
  return {
    tipo_identificacion_id: Number(form.tipoIdentificacion),
    numero_id: form.numeroCedula,
    nombre: form.nombres,
    apellido: form.apellidos,
    fecha_nacimiento: form.fechaNacimiento,
    direccion: form.direccion,
    ciudad_id: Number(form.ciudad),
    marca_id: Number(form.marca),
  }
}

export function useFormularioInscripcion() {
  const [listaTiposId, setListaTiposId] = useState([])
  const [listaPaises, setListaPaises] = useState([])
  const [listaMarcas, setListaMarcas] = useState([])
  const [listaDepartamentos, setListaDepartamentos] = useState([])
  const [listaCiudades, setListaCiudades] = useState([])

  const [form, setForm] = useState(formInicial)
  const [errores, setErrores] = useState({})
  const [mensaje, setMensaje] = useState(null)
  const [enviando, setEnviando] = useState(false)

  useEffect(() => {
    let activo = true
    async function cargarDatosIniciales() {
      try {
        const [tiposId, paises, marcas] = await Promise.all([
          obtenerLista('tipos-identificacion'),
          obtenerLista('paises'),
          obtenerLista('marcas'),
        ])
        if (!activo) return
        setListaTiposId(tiposId)
        setListaPaises(paises)
        setListaMarcas(marcas)
      } catch {
        if (activo) setMensaje({ tipo: 'error', texto: 'No se pudieron cargar los datos del servidor.' })
      }
    }
    cargarDatosIniciales()
    return () => {
      activo = false
    }
  }, [])

  async function cargarDepartamentos(paisId) {
    setListaDepartamentos([])
    setListaCiudades([])
    if (!paisId) return
    try {
      const departamentos = await obtenerLista('departamentos', { pais_id: paisId })
      setListaDepartamentos(departamentos)
    } catch {
      setMensaje({ tipo: 'error', texto: 'No se pudieron cargar los departamentos.' })
    }
  }

  async function cargarCiudades(departamentoId) {
    setListaCiudades([])
    if (!departamentoId) return
    try {
      const ciudades = await obtenerLista('ciudades', { departamento_id: departamentoId })
      setListaCiudades(ciudades)
    } catch {
      setMensaje({ tipo: 'error', texto: 'No se pudieron cargar las ciudades.' })
    }
  }

  function manejarCambio(e) {
    const { id, value } = e.target
    setMensaje(null)
    setErrores((prev) => ({ ...prev, [id]: false }))
    setForm((prev) => ({ ...prev, [id]: value }))

    if (id === 'pais') {
      setForm((prev) => ({ ...prev, departamento: '', ciudad: '' }))
      cargarDepartamentos(value)
    }
    if (id === 'departamento') {
      setForm((prev) => ({ ...prev, ciudad: '' }))
      cargarCiudades(value)
    }
  }

  async function manejarEnvio(e) {
    e.preventDefault()
    setMensaje(null)

    const nuevosErrores = {}
    for (const campo of camposObligatorios) {
      if (!form[campo]) nuevosErrores[campo] = true
    }

    if (Object.keys(nuevosErrores).length > 0) {
      setErrores(nuevosErrores)
      setMensaje({ tipo: 'error', texto: 'Todos los campos son obligatorios.' })
      return
    }

    setEnviando(true)
    try {
      const { ok, datos } = await crearInscripcion(construirPayload(form))
      if (ok) {
        setMensaje({ tipo: 'exito', texto: datos.msg || 'Inscripción creada correctamente.' })
        setForm(formInicial)
        setListaDepartamentos([])
        setListaCiudades([])
        setErrores({})
      } else {
        setMensaje({ tipo: 'error', texto: datos.error || 'Ha ocurrido un error.' })
      }
    } catch {
      setMensaje({ tipo: 'error', texto: 'No se pudo conectar con el servidor.' })
    } finally {
      setEnviando(false)
    }
  }

  return {
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
  }
}