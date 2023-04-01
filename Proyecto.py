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
            while lista != 16:
                print("Ingrese el número de artículo que quiere comprar")
                print("1. Caja de leche (¢ 1200)")
                print("2. Pan (¢ 1000)")
                print("3. Mantequilla (¢ 510)")
                print("4. Arroz 4kg(¢ 3700)")
                print("5. Frijoles 1kg (¢ 1800)")
                print("6. Atún (¢ 610)")
                print("7. Cartón de huevos(¢ 3800)")
                print("8. Café (¢ 4100)")
                print("9. Fideos (¢ 640)")
                print("10. Salsa de tomate (¢ 1700)")
                print("11. Mayonesa (¢ 890)")
                print("12. Sazonador (¢ 450)")
                print("13. Harina (¢ 940)")
                print("14. Masa (¢ 870)")
                print("15. Papaya (¢490)")
                print("16. Terminar lista")
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

                 if lista == 1: #si se seleciona un producto te da la opcion para introduccir la candidad que quieres
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Caja(s) de Leche (¢ 1200)"
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Caja(s) de Leche (¢ 1200)" 
                        costoTotal = costoTotal + (cantidad * 1200)
                        print("Usted ha seleccionado " + str(cantidad) + " Caja(s) de Leche") #este print indica que as seleccionado
                    elif lista == 2:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Pan(es) (¢ 1000)"
                        else:
                            listaComedera =  listaComedera + ", " + str(cantidad) + " Pan(es) (¢ 1000)"
                        costoTotal = costoTotal + (cantidad * 1000)
                        print("Usted ha seleccionado " + str(cantidad) + " Pan(es)")
                    elif lista == 3:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Mantequilla(s) (¢ 510)"
                        else:
                            listaComedera =  listaComedera + ", " + str(cantidad) + " Mantequilla(s) (¢ 510)"
                        costoTotal = costoTotal + (cantidad * 510)
                        print("Usted ha seleccionado " + str(cantidad) + " Mantequilla(s)")
                    elif lista == 4:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Arroz 4kg(¢ 3700)"
                        else:
                            listaComedera =  listaComedera + ", " + str(cantidad) + " Arroz 4kg(¢ 3700)"
                        costoTotal = costoTotal + (cantidad * 3700)
                        print("Usted ha seleccionado " + str(cantidad) + " Arroz 4kg(¢ 3700)")
                    elif lista == 5:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Frijoles 1kg (¢ 1800)"
                        else:
                            listaComedera =  listaComedera + ", " + str(cantidad) + " Frijoles 1kg (¢ 1800)"
                        costoTotal = costoTotal + (cantidad * 1800)
                        print("Usted ha seleccionado " + str(cantidad) + " Frijoles 1kg (¢ 1800)")
                    elif lista == 6:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Atún (¢ 610) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Atún (¢ 610) "
                        costoTotal = costoTotal + (cantidad * 610)
                        print("Usted ha seleccionado " + str(cantidad) + " Atún (¢ 610)")
                    elif lista == 7:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Cartón de huevos(¢ 3800) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Cartón de huevos(¢ 3800) "
                        costoTotal = costoTotal + (cantidad * 3800)
                        print("Usted ha seleccionado " + str(cantidad) + " Cartón de huevos(¢ 3800) ")
                    elif lista == 8:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Café (¢ 4100) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Café (¢ 4100) "                            
                        costoTotal = costoTotal + (cantidad * 4100)
                        print("Usted ha seleccionado " + str(cantidad) + " Café (¢ 4100) ")
                    elif lista == 9:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Fideos (¢ 640) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Fideos (¢ 640) "
                        costoTotal = costoTotal + (cantidad * 640)
                        print("Usted ha seleccionado " + str(cantidad) + " Fideos (¢ 640) ")
                    elif lista == 10:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Salsa de tomate (¢ 1700) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Salsa de tomate (¢ 1700) "
                        costoTotal = costoTotal + (cantidad * 1700)
                        print("Usted ha seleccionado " + str(cantidad) + " Salsa de tomate (¢ 1700)) ")
                    elif lista == 11:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Mayonesa (¢ 890) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Mayonesa (¢ 890) "
                        costoTotal = costoTotal + (cantidad * 890)
                        print("Usted ha seleccionado " + str(cantidad) + " Mayonesa (¢ 890) ")
                    elif lista == 12:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Sazonador (¢ 450) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Sazonador (¢ 450) "
                        costoTotal = costoTotal + (cantidad * 450)
                        print("Usted ha seleccionado " + str(cantidad) + " Sazonador (¢ 450) ")
                    elif lista == 13:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Harina (¢ 940) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Harina (¢ 940) "
                        costoTotal = costoTotal + (cantidad * 940)
                        print("Usted ha seleccionado " + str(cantidad) + " Harina (¢ 940) ")
                    elif lista == 14:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Masa (¢ 870) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Masa (¢ 870) "
                        costoTotal = costoTotal + (cantidad * 870)
                        print("Usted ha seleccionado " + str(cantidad) + " Masa (¢ 870) ")
                    elif lista == 15:
                        if listaComedera == "":
                            listaComedera = str(cantidad) + " Papaya (¢490) "
                        else:
                            listaComedera = listaComedera + ", " + str(cantidad) + " Papaya (¢490) "
                        costoTotal = costoTotal + (cantidad * 490)
                        print("Usted ha seleccionado " + str(cantidad) + " Papaya (¢490) ")
                        
                 #Fin de WHILE
                    
                    # Aquí se aplica el descuento al total de la compra y se muestra la factura con el monto neto total 
                montototal = costoTotal
                numitems = lista - 1  #se resta 1 porque lista tiene el valor de "Terminar lista" (4) que no es un producto comprado
    
                    # Calcular el impuesto del 13% sobre el monto total bruto
                impuesto = montototal * 0.13
    
                    # Calcular el descuento en función del número total de productos comprados
                if numitems <= 5:
                        descuento = montototal * 0.02
                elif numitems <= 10:
                        descuento = montototal * 0.05
                else:
                        descuento = montototal * 0.07
    
                # Calcular el monto total neto de la compra después del impuesto y el descuento
                montoneto = montototal + impuesto - descuento
                    
                    print('----------',fecha,'----------\nCliente: ', nombre)
                print("El total a pagar es: ¢" ,+ montoneto)
                print("/*-----------------------------------------*/")
                print("Impuesto (13%): ¢", impuesto)
                print("Descuento: ¢", descuento)
                print("Monto Total Bruto: ¢", montototal)
                print("Esta es su lista de compras: " + str(listaComedera))
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
