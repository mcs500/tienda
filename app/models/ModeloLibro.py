from .entities.Autor import Autor
from .entities.Libro import Libro

class ModeloLibro():

    @classmethod
    def listar_libros(self,db):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT lib.isbn, lib.titulo, lib.anioedicion,lib.precio,
                    aut.nombres,aut.apellidos,aut.fechanacimiento
                    FROM libro lib
                    INNER JOIN autor aut on lib.autor_id=aut.id"""
            cursor.execute(sql)
            data=cursor.fetchall()
            libros=[]
            for row in data:
                aut=Autor(0, row[4], row[5])
                lib=Libro(row[0], row[1], aut, row[2], row[3])
                libros.append(lib)
            return libros
        except Exception as ex:
            raise Exception(ex)