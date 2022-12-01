from modelo.empleado import Empleado
from dao.dao_empleado import daoEmpleado
from utils.encoder import Encoder

class EmpleadoDTO:
    def validarLogin(self, correo, clave):
        try:
            daoempleado = daoEmpleado()
            empleadoValues = Empleado(correo=correo, clave=Encoder().encode(clave))
            resultado = daoempleado.validarLogin(empleadoValues)
            return resultado
        except Exception as ex:
            print(ex)
