from controlador.validations import inicial, validarLogin


##### login
intentos = 1
print("Sistema Minimarket")
while intentos <= 3:
    try:
        #resu = validarLogin()
        #if resu is not None:
        if True:
            inicial()
            break
        else:
            print("Usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("Intentar nuevamente")
if intentos == 4:
    print("Excedió el límite de intentos.contraseña bloqueada")