from flask_restful import Resource
from ..modelos import db, Cancion, CancionSchema
from flask import request

cancion_schema = CancionSchema()

class VistaCanciones (Resource):
    def get(self):#Me trae todas las canciones
        return [cancion_schema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],
                                minutos=request.json['minutos'],
                                segundos=request.json['segundos'],
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)#agrgar en la bd
        db.session.commit()#guardar los cambios
        return cancion_schema.dump(nueva_cancion)#retornar la nueva cancion en formato json

class VistaCancion(Resource):
    def get(self, id_cancion):
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))

    #actualizar
    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo',cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete',cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    def delete(self, id_canciones):
        cancion = Cancion.query.get_or_404(id_canciones)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operacion exitosa', 204