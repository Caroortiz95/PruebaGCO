from flask import jsonify, request, Blueprint
from Models import TipoID, Pais, Departamento, Ciudad, Marca, Cliente, Inscripcion
from logging import exception
from config.database import db
from datetime import date, datetime

bp = Blueprint('main', __name__)

@bp.route('/api/tipos-identificacion', methods=["GET"])
def get_tipo_id():
    try:
        tipoId = TipoID.query.all()
        toReturn = [tipo.serialize() for tipo in tipoId]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/paises', methods=["GET"])
def get_pais():
    try:
        pais = Pais.query.all()
        toReturn = [pais.serialize() for pais in pais]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/departamentos', methods=["GET"])
def get_departamento():
    try:
        consulta = Departamento.query
        pais_id = request.args.get("pais_id", type=int)
        if pais_id is not None:
            consulta = consulta.filter_by(pais_id=pais_id)
        departamentos = consulta.all()
        toReturn = [departamento.serialize() for departamento in departamentos]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/ciudades', methods=["GET"])
def get_ciudad():
    try:
        consulta = Ciudad.query
        departamento_id = request.args.get("departamento_id", type=int)
        if departamento_id is not None:
                consulta = consulta.filter_by(departamento_id=departamento_id)
        ciudades = consulta.all()
        toReturn = [ciudad.serialize() for ciudad in ciudades]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/marcas', methods=["GET"])
def get_marca():
    try:
        marca = Marca.query.all()
        toReturn = [marca.serialize() for marca in marca]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/inscripciones', methods=["POST"])
def set_inscripcion():
    datos = request.get_json()

    clienteExistente = Cliente.query.filter_by(numero_id = datos["numero_id"], tipo_identificacion_id = datos["tipo_identificacion_id"]).first()
    if clienteExistente:
        marcasAsociadasCliente = [i.marca_id for i in Inscripcion.query.filter_by(cliente_id = clienteExistente.id).all()]
        if datos["marca_id"] in marcasAsociadasCliente:
            return {
                "error": "Este usuario ya se encuentra registrado para esta marca"
            }, 409
    
    fecha_nacimiento = datetime.strptime(datos["fecha_nacimiento"], "%Y-%m-%d").date()

    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    if edad < 18:
        return {
            "error": "La edad mínima para realizar el registro es de de 18 años"
        }, 400
    
    cliente = Cliente(
        tipo_identificacion_id = datos["tipo_identificacion_id"],
        numero_id = datos["numero_id"],
        nombre = datos["nombre"],
        apellido = datos["apellido"],
        fecha_nacimiento = fecha_nacimiento,
        direccion = datos["direccion"],
        ciudad_id = datos["ciudad_id"]
    )
    db.session.add(cliente)
    db.session.flush()
    inscripcion = Inscripcion(
        cliente_id = cliente.id,
        marca_id = datos["marca_id"]
    )
    db.session.add(inscripcion)
    db.session.commit()

    return {
        "msg": "Inscripción creada correctamente",
        "inscripcion": inscripcion.serialize()
    }, 201
    