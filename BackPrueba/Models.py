from config.database import db
from datetime import date

class TipoID(db.Model):
    __tablename__ = "tipos_id"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return "nombre: {}".format(
            self.nombre
        )

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Pais(db.Model):
    __tablename__ = "paises"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    def __str__(self):
        return "nombre: {}".format(
            self.nombre
        )
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Departamento(db.Model):
    __tablename__ = "departamentos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    pais_id = db.Column(
        db.Integer,
        db.ForeignKey("paises.id"),
        nullable=False
    )

    def __str__(self):
        return "nombre: {}".format(
            self.nombre
        )
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Ciudad(db.Model):
    __tablename__ = "ciudades"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    departamento_id = db.Column(
        db.Integer,
        db.ForeignKey("departamentos.id"),
        nullable=False
    )

    def __str__(self):
        return "nombre: {}".format(
            self.nombre
        )
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Marca(db.Model):
    __tablename__ = "marcas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return "nombre: {}".format(
            self.nombre
        )
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    tipo_identificacion_id = db.Column(
            db.Integer,
            db.ForeignKey("tipos_id.id"),
            nullable=False
        )
    numero_id = db.Column(db.String(30), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    ciudad_id = db.Column(
        db.Integer,
        db.ForeignKey("ciudades.id"),
        nullable=False
    )

    def __str__(self):
        return "numero_id: {}. nombre: {}. apellido: {}. fecha_nacimiento: {}. direccion: {}".format(
            self.numero_id,
            self.nombre,
            self.apellido,
            self.fecha_nacimiento,
            self.direccion
        )
    
    def serialize(self):
        return {
            "id": self.id,
            "numero_id": self.numero_id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_nacimiento": self.fecha_nacimiento,
            "direccion": self.direccion
        }

class Inscripcion(db.Model):
    __tablename__ = "inscripciones"
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False
    )
    marca_id = db.Column(
            db.Integer,
            db.ForeignKey("marcas.id"),
            nullable=False
        )
    fecha_inscripcion = db.Column(db.Date, nullable=False, default=date.today)
    
    def serialize(self):
        return {
            "id": self.id,
        }
    
def crear_modelos():
    db.create_all()