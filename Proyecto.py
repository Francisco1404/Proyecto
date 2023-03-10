print("Bienvenido al supermercado 'Los Pollitos'") 
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
            
