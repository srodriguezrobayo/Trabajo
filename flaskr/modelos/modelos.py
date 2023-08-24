from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Cancion(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    titulo =db.Column(db.String(128))
    minutos = db.Column (db.Integer)
    segundos = db.Column (db.Integer)
    interprete=db.Column (db.String(128))

    def __repr__(self):
        return ("{} - {} - {} - {}".format(self.titulo,self.minutos, self.segundos,self.interprete))

    class medio(db.Model):
        id=db.Column (db.Integer , primary_key=True)
        nom_medio=db.Column (db.String(128))

    class Album(db.Model):
        id = db.Column (db.Integer , primary_key=True)
        titulo = db.Column (db.String(128))
        ano = db.Column (db.Integer)
        descripcion= db.Column (db.String(128))
        Medio = db.Column (db.medio)

        def __repr__(self):
            return ("{} - {} - {} - {}".format(self.titulo,self.ano,self.descripcion,self.Medio))

    class Ususario (db.Model):
        id= db.Column (db.Integer , primary_key=True)
        nombre_usuario= db.Column (db.String(128))
        contrasena = db.Column (db.string(128))

        def __repr__(self):
            return ("{} - {}".format(self.nombre_usuario,self.contrasena))
