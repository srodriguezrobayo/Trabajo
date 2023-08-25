from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio
from flask_restful import Api
from .vistas import VistaCanciones

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCanciones, '/canciones/<int:id_cancion>')

#with app.app_context():
    #Album_Schema = AlbumSchema()
    #A = Album(titulo='Prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #db.session.add(A)
    #db.session.commit()
    #print([Album_Schema.dumps(album) for album in Album.query.all()])

#with app.app_context():
    #u = Usuario(nombre='Juan', contrasenia='12345')
    #c = Cancion(titulo="prueba", minutos=2, segundos=25, interprete="Haaland")
    #a = Album(titulo='XD', anio=1999, descripcion='POP', medio=Medio.CD)
    #u.albumes.append(a)
    #a.canciones.append(c)
    #db.session.add(u)
    #db.session.add(c)
    #db.session.commit()
    #print(Album.query.all())
    #print(Album.query.all()[0].canciones)
    #db.session.delete(a)
    #print(Album.query.all())
    #print(Cancion.query.all())

#prueba
#with app.app_context():
    #c= Cancion(titulo='prueba', minutos=2, segundos=25, interprete='Haaland')
    #db.session.add(c)
    #db.session.commit()
    #print(Cancion.query.all())
    #a = Album(titulo='XD', anio=2002, descripcion='POP', medio=3)
    #db.session.add(a)
    #db.session.commit()
    #print(Album.query.all())
    #u = Usuario(nombre_usuario='Cristiano', contrasena=1234)
    #db.session.add(u)
    #db.session.commit()
    #print(Usuario.query.all())

#with app.app_context():
    #u = Usuario(nombre='Juan', contrasena='12345')
    #a = Album(tiulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #u.albumes.append(a)
    #db.session.add(u)
    #db.session.commit()
    #print(Usuario.query.all())
    #print(Usuario.query.all()[0].albumes)
    #db.session.delete(u)
    #print(Usuario.query.all())
    #print(Album.query.all())