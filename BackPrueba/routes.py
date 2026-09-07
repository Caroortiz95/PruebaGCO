from flask import Flask, jsonify, request, Blueprint
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

    except Exception as e:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/paises', methods=["GET"])
def get_pais():
    try:
        pais = Pais.query.all()
        toReturn = [pais.serialize() for pais in pais]
        return jsonify(toReturn), 200

    except Exception as e:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/departamentos', methods=["GET"])
def get_departamento():
    try:
        departamentos = Departamento.query.all()
        toReturn = [departamento.serialize() for departamento in departamentos]
        return jsonify(toReturn), 200

    except Exception as e:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/ciudades', methods=["GET"])
def get_pais():
    try:
        ciudad = Ciudad.query.all()
        toReturn = [ciudad.serialize() for ciudad in ciudad]
        return jsonify(toReturn), 200

    except Exception as e:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/marcas', methods=["GET"])
def get_pais():
    try:
        marca = Marca.query.all()
        toReturn = [marca.serialize() for marca in marca]
        return jsonify(toReturn), 200

    except Exception as e:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@bp.route('/api/inscripciones', methods=["POST"])
def set_inscripcion():
    datos = request.get_json()

    clienteExistente = Cliente.query.filterBy(numeroId = datos["numero_id"]).first()
    if clienteExistente:
        return {
            "error": "El cliente ya está registrado"
        }, 409
    
    fecha_nacimiento = datetime.strptime(datos["fecha-nacimiento"], "%y-%m-%d").date

    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    if edad < 18:
        return {
            "error": "El cliente debe ser mayor de 18 años"
        }, 400
    
    cliente = Cliente(
        tipo_identificacion_id = datos["tipo_identificacion_id"],
        numero_id = datos["numero_id"],
        nombre = datos["nombre"],
        apellido = datos["apellido"],
        fecha_nacimiento = datos["fecha_nacimiento"],
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
    