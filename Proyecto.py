while True:
    print("Bienvenido al supermercado 'Los Pollitos'")

    nombre_valido = False
    while not nombre_valido:
        nombre = input('Ingrese su nombre y apellido: ')
        if len(nombre) > 0:
            nombre_valido = True
        else:
            print('Por favor, ingrese su nombre y apellido.')

    fecha_valida = False
    while not fecha_valida:
        fecha = input('Ingrese la fecha (00/00/0000): ')
        if len(fecha) > 0:
            fecha_valida = True
        else:
            print('Por favor, ingrese la fecha.')

        if nombre=='':
            print("Menú de inicio")
    
    listaComedera = ""
    costoTotal = 0
    cantidad = 0
    
    reiniciar = True
    while reiniciar:
            print("/*-----------------------------------------*/")
            print("1. Ingresar nueva compra")
            print("2. Salir")
            print("/*-----------------------------------------*/")
            respuesta = int(input())
            if respuesta == 1: #apartir de este if te da las opciones para comprar
                lista = 0
            while lista != 4:
                print("Ingrese el número de artículo que quiere comprar")
                print("1. Caja de leche (¢ 1200)")
                print("2. Pan (¢ 1000)")
                print("3. Mantequilla (¢ 510)")
                print("4. Terminar lista")
                lista = int(input())
                
                    if lista > 0 and lista < 16:
                        valor_valido = False
                        while not valor_valido:
                            cantidad = input("Indique la cantidad: ")
                            if cantidad != "":
                                cantidad = int(cantidad)
                                valor_valido = True
                            else:
                                print("Por favor, ingrese una cantidad válida.")
                if lista != 4:
                    cantidad = int(input("Indique la cantidad: ")) # se solicita la cantidad al usuario

                if lista == 1:
                    if agregarSeparadorComa == 1:
                        listaComedera = listaComedera + ", " + str(cantidad) + " Caja(s) de Leche (¢ 1200)"
                    else:
                        listaComedera = listaComedera + str(cantidad) + " Caja(s) de Leche (¢ 1200)"

                    costoTotal = costoTotal + (cantidad * 1200)
                    print("Usted ha seleccionado " + str(cantidad) + " Caja(s) de Leche")

                elif lista == 2:
                    if agregarSeparadorComa == 1:
                        listaComedera = listaComedera + ", " + str(cantidad) + " Pan(es) (¢ 1000)"
                    else:
                        listaComedera =  listaComedera + str(cantidad) + " Pan(es) (¢ 1000)"

                    costoTotal = costoTotal + (cantidad * 1000)
                    print("Usted ha seleccionado " + str(cantidad) + " Pan(es)")
                elif lista == 3:
                    if agregarSeparadorComa == 1:
                        listaComedera = listaComedera + ", " + str(cantidad) + " Mantequilla(s) (¢ 510)"
                        costoTotal = costoTotal + (cantidad * 510)
                    print("Usted ha seleccionado " + str(cantidad) + " Mantequilla(s)")
                elif lista == 4:
                    print('----------',fecha,'----------\nCliente: ', nombre)
                    print("/*-----------------------------------------*/")
                    print("Esta es su lista de compras: " + listaComedera)
                    print("El total a pagar es: " ,+ costoTotal)
                    print("/*-----------------------------------------*/")
            else:
                print("Limpiando lista de compras. Saliendo...")
    
            if respuesta == 2 and cantidad >= 0:
                #REINICIAR TODO EL SISTEMA
                reiniciar = False
            elif lista == 16:
                   #SE DEBE LIMPIAR LA LISTA DE ARTICULOS
                   lista = 0
                   listaComedera = ""
