from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask_cors import CORS,cross_origin
#Creación de la instancia de Flask
app = Flask(__name__)
#Configuración de CORS para que se pueda acceder desde la web.
cors = CORS(app,resources = {r"/*": {"origins": "*"}})

#Configuración de la conexión con la base de datos.
app.config["MONGO_URI"] = "mongodb+srv://ico17rg:GRauXZrWLGFMsogF@cluster0.6augu9z.mongodb.net/prueba?retryWrites=true&w=majority"
#Realizamos conexión con la base de datos.
mongo = PyMongo(app)
db =  mongo.db

@app.route("/get_all", methods=["GET"])
def get_all():
    #Obtenemos todos los alumnos de la base de datos.
    alumnos_cursor = db.alumnos.find({})
    #Creamos una lista para guardar los datos
    alumnos_list = []
    #Recorremos todos los alumnos
    for alumno in alumnos_cursor:
        #Convertimos el objectID a una cadena.
        alumno['_id'] = str(alumno['_id'])
        #Añadimos a la lista 
        alumnos_list.append(alumno)
    #Usamos la función dumps para convertir la lista a JSON
    return dumps(alumnos_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
