def inicio():
    while True:
        print("Bienvenido al supermercado 'Los Pollitos'")

        nombre_valido = False
        while not nombre_valido:
            nombre = input('Ingrese su nombre: ')
            apellido = input('Ingrese su apellido: ')
            if len(nombre) > 0 and len(apellido) > 0:
                nombre_valido = True
            else:
                print('Por favor, ingrese su nombre y apellido.')

            fecha_valida = False
            while not fecha_valida:
                dia = input('Ingrese el día (1-31): ')
                mes = input('Ingrese el mes (1-12): ')
                año = input('Ingrese el año: ')
                if dia and mes and año:  
                    dia = int(dia)
                    mes = int(mes)
                    año = int(año)
                    if 1 <= dia <= 31 and 1 <= mes <= 12 and año >= 2022: 
                        if mes == 2:  
                            if dia <= 29:
                                fecha_valida = True
                            elif dia == 30 or dia == 31:
                                print('Febrero solo tiene 28 o 29 días.')
                            else:
                                print('El día ingresado no es válido.')
                        elif mes in [4, 6, 9, 11]:
                            if dia <= 30:
                                fecha_valida = True
                            else:
                                print('El día ingresado no es válido.')
                        else:
                            fecha_valida = True
                    else:
                        print('Ingrese valores válidos para día, mes y año, asegurándose de que el año sea igual o mayor a 2022.')
                else:
                    print('Ingrese valores numéricos para día, mes y año.')  

            fecha = str(dia) + "/" + str(mes) + "/" + str(año)  


            if nombre=='':
            print("Menú de inicio")
            continue
        
        listaComedera = []
        costoTotal = 0
        
        reiniciar = True
        
        # Arreglo de nombres y precios de los articulos
        articulos = [["Caja de leche", 1200],
                     ["Pan", 1000],
                     ["Mantequilla", 510],
                     ["Arroz 4kg", 3700],
                     ["Frijoles 1kg", 1800],
                     ["Atún", 610],
                     ["Cartón de huevos", 3800],
                     ["Café", 4100],
                     ["Fideos", 640],
                     ["Salsa de tomate", 1700],
                     ["Mayonesa", 890],
                     ["Sazonador", 450],
                     ["Harina", 940],
                     ["Masa", 870],
                     ["Papaya", 490]]
        
        # Dentro de este While empieza el ciclo de compras
        while reiniciar:
            print("/*-----------------------------------------*/")
            print("1. Ingresar nueva compra")
            print("2. Salir")
            print("/*-----------------------------------------*/")
            respuesta = int(input())
            if respuesta == 1:
                lista = 0
                
                while lista != 16:
                    print("Ingrese el número de artículo que quiere comprar")
                    # Imprimir los articulos con sus precios
                    for i in range(len(articulos)):
                        print(str(i+1) + ". " + articulos[i][0] + " (¢ " + str(articulos[i][1]) + ")")
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
                        #agregar el articulo seleccionado y su cantidad a la lista de compras
                    compra = [articulos[lista-1][0], cantidad, articulos[lista-1][1]]
                    listaComedera += [compra]
                    costoTotal = costoTotal + (cantidad * articulos[lista-1][1])
            elif respuesta == 2:
                print("/*-----------------------------------------*/")
                print('----------',fecha,'----------\nCliente: ', nombre, apellido)
                print("Lista de compras:")
                for item in listaComedera:
                    print(item[0] + " x" + str(item[1]) + ": ¢" + str(item[2]*item[1]))            
                print("Total Bruto: ¢" + str(costoTotal))

                reiniciar = False
                montototal = costoTotal
                numitems = lista - 1
                #se resta 1 porque lista tiene el valor de "Terminar lista" (4) que no es un producto comprado
                # Abrir un archivo de texto para escribir la lista de compras
                nombre_archivo = nombre.replace(" ", "_") + "_" + fecha.replace("/", "-") + ".txt"
                with open(nombre_archivo, "w") as archivo:
                        # Escribir el encabezado con el nombre y la fecha
                    archivo.write("Lista de compras\n")
                    archivo.write("Cliente: " + nombre + "\n")
                    archivo.write("Fecha: " + fecha + "\n\n")
                        # Escribir cada artículo comprado con su cantidad y precio
                    for item in listaComedera:
                        archivo.write(item[0] + " x" + str(item[1]) + ": ¢" + str(item[2]*item[1]) + "\n")
                    archivo.write("\nTotal a pagar: ¢" + str(costoTotal))
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


                print("Descuento: ¢", descuento)
                print("Impuesto (13%): ¢", impuesto)
                print("Total de la compra: ¢" ,+ montoneto)
                print("¡Muchas gracias por su compra, lo esperamos pronto!")
                print("/*-----------------------------------------*/")
            else:
                print("Limpiando lista de compras. Saliendo...")

    if respuesta == 2 and cantidad >= 0:
        
        reinicio()
    #REINICIAR TODO EL SISTEMA

def reinicio():
    reiniciar = False
    if lista == 16:
        factura()
    #SE DEBE LIMPIAR LA LISTA DE ARTICULOS
        lista = 0
        listaComedera = ""

inicio()
