from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario


app = create_app ('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

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

with app.app_context():
    u = Usuario(nombre_usuario='juan', contrasena='12345')
    c = Cancion(titulo="prueba", minutos=2, segundos=25, interprete="Santiago")
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())