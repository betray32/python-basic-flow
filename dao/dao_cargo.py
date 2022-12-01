from conex import conn
import traceback

class daoCargo:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "my_db")
            print('conexion establecida correctamente')
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    # Login
    def findCargo(self,cargo):
        sql = "select idcargo, numerocargo, nombrecargo from cargo where numerocargo = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.numerocargo,))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def addCargo(self, cargo):
        sql = "insert into cargo (numerocargo, nombrecargo) values (%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.numerocargo, cargo.nombrecargo))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
                return True
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return False
    
    def updateCargo(self, cargo):
        sql = "update cargo set nombrecargo = %s where numerocargo = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.nombrecargo, cargo.numerocargo))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
                return True
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return False
        return

    def delCargo(self, cargo):
        sql = "delete from cargo where numerocargo = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.numerocargo,))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos eliminados satisfactoriamente"
                return True
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return False
    
    def findAllCargos(self, ):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select idcargo, numerocargo, nombrecargo from cargo")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result