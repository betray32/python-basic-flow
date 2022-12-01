from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_cargo import CargoDTO

def volver():
    input("Presione enter para volver al menú...\n")


def validarLogin():
    correo = input("Ingrese su correo: ")
    clave = input("Ingrese su clave: ")
    resultado = EmpleadoDTO().validarLogin(correo, clave)
    return resultado

def inicial():
    while True:
        opc = menuPrincipal()
        if opc == 1:
            print('La opción 1 aun no se encuentra operativa, seleccione otra opción\n')
            volver()
        elif opc == 2:
            print('Usted ha seleccionado Cargos')
            menuCargos()
            volver()
        elif opc == 3:
            print('Usted ha seleccionado Comunas')
            menuComuna()
            volver()
        else:
            break

def menuPrincipal():
    print('*'*30, 'CRUD MIMARKET FÉNIX','*'*30,'\n')
    print('1. CRUD Empleados')
    print('2. CRUD Cargos')
    print('3. CRUD Comunas')
    print('4. Salir del sistema\n')
    
    try:
        opc = int(input("Ingrese opción: "))
        if opc >= 1 and opc <= 4:
            return opc
        else:
            print(f"\nOpción {opc} no válida\n")
            volver()
            return menuPrincipal()
    except:
        print(f"\nOpción {opc} no válida\n")
        volver()
        return menuPrincipal()

def menuCargos():
    print('*'*30, 'CRUD CARGOS','*'*30,'\n')
    print('1. Ingresar Cargo')
    print('2. Modificar Cargo')
    print('3. Eliminar Cargo')
    print('4. Mostrar todos los Cargos')
    print('5. Volver al menú principal')

    try:
        opc = int(input("Ingrese opción: "))
        if opc >= 1 and opc <= 5:
            cargoDto = CargoDTO()
            
            if opc == 1:
                validateAddCargo(cargoDto)
                print('Operacion Exitosa')
                volver()
                return menuPrincipal()
            elif opc == 2:
                print('Modificar Cargo')
                validateUpdateCargo(cargoDto)
                print('Operacion Exitosa')
                volver()
                return menuPrincipal()
            elif opc == 3:
                print('Eliminar Cargo')
                numerocargo = int(input("Ingrese identificador cargo: "))
                cargoDto.delCargo(numerocargo)
                print('Operacion Exitosa')
                volver()
                return menuPrincipal()
            elif opc == 4:
                print('Procediendo a Mostrar todos los Cargos')
                listaCargos = cargoDto.findAllCargos()
                if len(listaCargos) > 0:
                    for u in listaCargos:
                        print('Id Cargo: ' + str(u.idcargo) + " - Numero Cargo: " + str(u.numerocargo) + " - Nombre Cargo: " + u.nombrecargo)
                else:
                    print ('no hay resultados')

            elif opc == 5:
                volver()
                return menuPrincipal()
            

        else:
            print(f"\nOpción {opc} no válida\n")
            volver()
            return menuPrincipal()
    except Exception as ex:
        print(ex)
        print(f"\nOpción {opc} no válida\n")
        volver()
        return menuPrincipal()

def validateAddCargo(cargoDto):
    print('Ingresar Cargo')
    numerocargo = int(input("Ingrese identificador cargo: "))
    if numerocargo == 0:
        print("Debe ingresar un identificador de cargo valido... Abortando")
        return

    nombreCargo = input("Ingrese nombre cargo: ")
    if len(nombreCargo) == 0:
        print("Debe ingresar un nombre de cargo")
        return

    cargoDto.addCargo(numerocargo, nombreCargo)

def validateUpdateCargo(cargoDto):
    print('Update Cargo')
    numerocargo = int(input("Ingrese identificador cargo: "))
    if numerocargo == 0:
        print("Debe ingresar un identificador de cargo valido... Abortando")
        return

    nombreCargo = input("Ingrese nombre cargo: ")
    if len(nombreCargo) == 0:
        print("Debe ingresar un nombre de cargo")
        return

    cargoDto.updateCargo(numerocargo, nombreCargo)


def menuComuna():
    print('*'*30, 'CRUD COMUNAS','*'*30,'\n')
    print('1. Ingresar Comuna')
    print('2. Modificar Comuna')
    print('3. Eliminar Comuna')
    print('4. Mostrar todos los Comunas')
    print('5. Volver al menú principal')

    try:
        opc = int(input("Ingrese opción: "))
        if opc >= 1 and opc <= 5:
            
            if opc == 1:
                print('Ingresar Comuna')

                print('Operacion Exitosa')
                volver()
                return menuPrincipal()
            elif opc == 2:
                print('Modificar Comuna')
               
                print('Operacion Exitosa')
                volver()
                return menuPrincipal()
            elif opc == 3:
                print('Eliminar Comuna')
                
                print('Operacion Exitosa')
                volver()
                return menuPrincipal()
            elif opc == 4:
                print('Mostrar todas las Comuna(s)')

            elif opc == 5:
                volver()
                return menuPrincipal()
            

        else:
            print(f"\nOpción {opc} no válida\n")
            volver()
            return menuPrincipal()
    except:
        print(f"\nOpción {opc} no válida\n")
        volver()
        return menuPrincipal()
