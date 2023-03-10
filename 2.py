print("Bienvenido al supermercado 'Los Pollitos'")
nombre=(input('Ingrese su nombre y apellido \n-'))
fecha=(input('Ingrese la fecha (00/00/0000)\n-'))
if nombre=='':
    print("Menú de inicio") 

listaComedera = ""
costoTotal = 0

#Esta variable es para controlar si se debe agregar un separador cada vez que 
#se agrega un artículo a la lista que guardamos en la variable listaComedera.
agregarSeparadorComa = 0

while True: 
        print("/*-----------------------------------------*/") 
        print("1. Ingresar nueva compra") 
        print("2. Salir") 
        print("/*-----------------------------------------*/") 
        respuesta = int(input()) 
    
        if respuesta == 1: 
            lista = 0
            while lista != 4:
                print("Ingrese el número de artículo que quiere comprar") 
                print("1. Caja de leche (¢ 1200)") 
                print("2. Pan (¢ 1000)") 
                print("3. Mantequilla (¢ 510)") 
                print("4. Terminar lista") 
                lista = int(input())
            
                if listaComedera != "":
                    agregarSeparadorComa = 1
            
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
                    else: 
                        listaComedera =  listaComedera + str(cantidad) + " Mantequilla(s) (¢ 510)"
                    
                    costoTotal = costoTotal + (cantidad * 510) 
                    print("Usted ha seleccionado " + str(cantidad) + " Mantequilla(s)") 
                elif lista == 4:
                    print('----------',fecha,'----------\nCliente: ', nombre)
                    print("/*-----------------------------------------*/") 
                    print("Esta es su lista de compras: " + listaComedera)
                    print("El total a pagar es: " ,+ costoTotal)
                    print("/*-----------------------------------------*/") 
                else: 
                    print("Opción inválida") 
        else: 
            print("Limpiando lista de compras. Saliendo...")
