from conex import conn
import traceback

class daoEmpleado:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "Nicolete")
            print('conexion establecida correctamente')
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    # Login
    def validarLogin(self,empleado):
        sql = "select correo from empleado where correo = %s and clave = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.correo, empleado.clave))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
        