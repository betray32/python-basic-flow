from modelo.cargo import Cargo
from dao.dao_cargo import daoCargo
from utils.encoder import Encoder

class CargoDTO:
    def addCargo(self, numerocargo, nombrecargo):
        cargo = self.findCargo(numerocargo)
        if cargo is not None:
            print('Usted no puede ingresar el cargo ya que existe un registro actualmente')
            return
        else:
            print('Procediendo a ingresar el cargo...')
            daocargo = daoCargo()
            cargoValues = Cargo(numerocargo=numerocargo, nombrecargo=nombrecargo)
            resultadoAddCargo = daocargo.addCargo(cargoValues)
            if (resultadoAddCargo):
                print ('cargo ingresado ok')
            else:
                print('fallo al ingresar cargo')
                return

    def findCargo(self, numerocargo):
        cargoValues = Cargo(numerocargo=numerocargo)
        daocargo = daoCargo()
        querycargo = daocargo.findCargo(cargoValues)
        return querycargo

    def updateCargo(self, numerocargo, nombrecargo):
        cargo = self.findCargo(numerocargo)
        if cargo is None:
            print('No se puede actualizar un cargo que no existe...')
            return
        else:
            print('Procediendo a actualizar el cargo...')
            daocargo = daoCargo()
            cargoValues = Cargo(numerocargo=numerocargo, nombrecargo=nombrecargo)
            resultadoUpdateCargo = daocargo.updateCargo(cargoValues)
            if (resultadoUpdateCargo):
                print ('cargo updated ok')
            else:
                print('fallo al update cargo')
                return


    def delCargo(self,  numerocargo):
        cargo = self.findCargo(numerocargo)
        if cargo is not None:
            print('Procediendo a eliminar el cargo')
            confirmarEliminarCargo = int(input("Esta seguro que desea eliminar el cargo?, Presione 1 para confirmar: "))
            if (confirmarEliminarCargo == 1):
                daocargo = daoCargo()
                cargoValues = Cargo(numerocargo=numerocargo)
                resultadoDelCargo = daocargo.delCargo(cargoValues)
                if (resultadoDelCargo):
                    print ('cargo eliminado ok')
                else:
                    print ('el cargo no pudo ser eliminado')
            else:
                return
        else:
            print('Usted no puede eliminar el cargo ya que NO existe un registro actualmente')
            

    def findAllCargos(self,):
        daocargo = daoCargo()
        resultadoTraerCargos = daocargo.findAllCargos()
        lista = []
        if resultadoTraerCargos is not None:
            for u in resultadoTraerCargos:
                iCargo = Cargo(idcargo=u[0], numerocargo=u[1], nombrecargo=u[2])
                lista.append(iCargo)
        return lista