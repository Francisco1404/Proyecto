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
    
