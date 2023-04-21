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
                    if 1 <= dia <= 31 and 1 <= mes <= 12 and año > 0:
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
                        print('Ingrese valores válidos para día, mes y año.')
                else:
                    print('Ingrese valores numéricos para día, mes y año.')

            fecha = str(dia) + "/" + str(mes) + "/" + str(año)
