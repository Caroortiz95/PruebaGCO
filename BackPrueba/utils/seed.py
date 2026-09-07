from app import app
from Models import TipoID, Pais, Departamento, Ciudad, Marca, crear_modelos
from config.database import db

with app.app_context():
    import os
    print(os.getenv("DATABASE_URL", "No existe la variable de entorno"))
    crear_modelos()

    cedulaCiudadania = TipoID(nombre = "Cédula de ciudadanía")
    cedulaExtranjeria = TipoID(nombre = "Cédula de extranjería")
    pasaporte = TipoID(nombre = "Pasaporte")

    colombia = Pais(nombre = "Colombia")
    db.session.add(colombia)
    db.session.commit()

    antioquia = Departamento(nombre = "Antioquia", pais_id = colombia.id)
    db.session.add(antioquia)
    bolivar = Departamento(nombre = "Bolívar", pais_id = colombia.id)
    db.session.add(bolivar)
    cundinamarca = Departamento(nombre = "Cundinamarca", pais_id = colombia.id)
    db.session.add(cundinamarca)
    db.session.commit()

    medellin = Ciudad(nombre = "Medellín", departamento_id = antioquia.id)
    envigado = Ciudad(nombre = "Envigado", departamento_id = antioquia.id)
    sabaneta = Ciudad(nombre = "Sabaneta", departamento_id = antioquia.id)
    itagui = Ciudad(nombre = "Itagüí", departamento_id = antioquia.id)
    bello = Ciudad(nombre = "Bello", departamento_id = antioquia.id)

    cartagena = Ciudad(nombre = "Cartagena", departamento_id = bolivar.id)
    turbaco = Ciudad(nombre = "Turbaco", departamento_id = bolivar.id)
    magangue = Ciudad(nombre = "Magangué", departamento_id = bolivar.id)

    bogota = Ciudad(nombre = "Bogotá", departamento_id = cundinamarca.id)
    zipaquira = Ciudad(nombre = "Zipaquirá", departamento_id = cundinamarca.id)
    funza = Ciudad(nombre = "Funza", departamento_id = cundinamarca.id)

    americanino = Marca(nombre = "Americanino")
    americanEagle = Marca(nombre = "American Eagle")
    chevignon = Marca(nombre = "Chevignon")
    espirit = Marca(nombre = "Espirit")
    nafNaf = Marca(nombre = "Naf Naf")
    rifle = Marca(nombre = "Rifle")

    db.session.add_all([
        cedulaCiudadania,
        cedulaExtranjeria,
        pasaporte,
        medellin,
        envigado,
        sabaneta,
        itagui,
        bello,
        cartagena,
        turbaco,
        magangue,
        bogota,
        zipaquira,
        funza,
        americanino,
        americanEagle,
        chevignon,
        espirit,
        nafNaf,
        rifle
    ])

    db.session.commit()

