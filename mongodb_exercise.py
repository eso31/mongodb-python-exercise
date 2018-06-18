from pymongo import MongoClient
from datetime import datetime as dt
from bson import json_util
import json


# Connection
mongo = MongoClient()
# Select database
db = mongo.techshop

# Object to test
person = {
    '_id': 1,
    'nombre': 'Dilan Armando',
    'apellido_paterno': "Coss",
    'apellido_materno': "Mingo",
    'telefono': '1234567890',
    'estado': 'Mexico',
    'ordenes': [
        {
            'pago': 12850,
            'metodo_pago': 'tarjeta',
            'fecha': dt.utcnow(),
            'empleado': {
                'nombre': 'Juan',
                'apellido_paterno': "Solis",
                'apellido_materno': "Salazar",
                'telefono': '1234567890',
                'turno': 'tarde',
                'correo': 'jsolis@techshop.com'
            },
            'productos': [
                {
                    'nombre': 'Laptop DELL',
                    'descripcion': '15 pulgadas',
                    'cantidad': 1,
                    'precio': 12500
                },
                {
                    'nombre': 'Mouse Compaq',
                    'descripcion': 'color negro',
                    'cantidad': 1,
                    'precio': 350
                }
            ]
        }
    ]
}


def main():
    print("Insert person")
    db.cliente.insert_one(person)
    c = db.cliente.find_one({"_id": 1})
    print(json.dumps(c, default=json_util.default, indent=4))

    print("Data before update")
    c = db.cliente.find_one({"_id": 1})
    print(json.dumps(c['ordenes'][0]['productos'], indent=4))

    print("Update a document")
    db.cliente.update_one({'_id': 1}, {'$set': {'ordenes.0.productos.1.nombre': 'Mouse Logitech'}})
    c = db.cliente.find_one({"_id": 1})
    print(json.dumps(c['ordenes'][0]['productos'], indent=4))


if __name__ == '__main__':
    main()
