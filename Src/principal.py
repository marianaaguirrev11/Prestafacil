import funciones

def MostrarMenu():
    menu = """
    1. Registrar usuario
    2. Registrar Item
    3. Registrar Prestamo
    4. Registrar Devolucion
    5. Consultar Items con mas de 30 dias
    6. Consultar Articulos Prestados
    7. Administrador
    8. Salir
    """
    return menu 
ESPACIADO = 90

titulo = '''

██████╗ ██████╗ ███████╗███████╗████████╗ █████╗ ███████╗ █████╗  ██████╗██╗██╗     
██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║██║     
██████╔╝██████╔╝█████╗  ███████╗   ██║   ███████║█████╗  ███████║██║     ██║██║     
██╔═══╝ ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║██╔══╝  ██╔══██║██║     ██║██║     
██║     ██║  ██║███████╗███████║   ██║   ██║  ██║██║     ██║  ██║╚██████╗██║███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝╚══════╝
                    
'''
OPCIONES_VALIDAS = ['1','2','3','4','5','6','7','8']

usuarios= []
inventario= []
prestamos= []
ventas_realizadas = []
devoluciones_cont= 0
total_pago_ventas= 0.0
contador_items= 1 

#credenciales fijas de administración
ADMIN_USUARIO= 'admin'
ADMIN_CONTRASEÑA= 'yo12345'

#inicio del ciclo del menu
while True:
    print('*'*ESPACIADO)
    for linea in titulo.split('\n'):
        if linea.strip():
            print(linea.center(ESPACIADO))    
    print('*'*ESPACIADO)
    print('')
    print('...::Bienvenidos::...'.center(ESPACIADO))
    print('')
    print('-'*ESPACIADO)
    print('')
    print(MostrarMenu())
    opcion = input('Favor ingresar la opcion deseada --> ')
    if opcion in OPCIONES_VALIDAS:
        match opcion:
            
            case '1':
                print('\tEstás en la opción 1. Registra el usuario')
                #validacion de cedula 
                cedula = input('Querido usuario, ingrese el numero de su cédula, por favor. --> ')
                while not funciones.ValidarCedula(cedula):
                    print('Error: La cédula debe tener entre 3 y 15 dígitos numéricos.')
                    cedula = input('Intente de nuevo: ')
                #el while ayuda a que el usuario no tenga que ingresar todos los datos si se equivoca
                
                #filtro de duplicados de cedula
                usuario_duplicado= False
                for usuario in usuarios:
                    if usuario['cedula'] == cedula:
                        usuario_duplicado= True
                
                if usuario_duplicado:
                    print('¡Cuidado! Ya existe un usuario registrado con este número de cédula. Cancelando el registro.')
                    continue #Envía a menu principal
                    
                nombre = input('Ingresa tu nombre, por favor. --> ')
                while not funciones.ValidarNombreApellido(nombre):
                    print('Error: El nombre debe tener al menos 3 letras y no puede tener números.')
                    nombre = input('Intenta de nuevo: ')
                    
                apellido = input('Ingresa tu apellido, por favor. --> ')
                while not funciones.ValidarNombreApellido(apellido):
                    print('Error: El apellido debe tener al menos 3 letras y no puede tener números.')
                    apellido = input('Intenta de nuevo: ')
                    
                correo = input('Ingresa el correo, por favor. --> ')
                while not funciones.ValidarCorreo(correo): 
                    print('Error: El correo debe tener "@" y terminar en ".com" .')
                    correo= input('Intenta de nuevo: ')
                    
                #filtro de duplicados de correo
                correo_duplicado= False
                for usuario in usuarios:
                    if usuario['correo'] == correo:
                        correo_duplicado= True 
                
                if correo_duplicado:
                    print('¡Cuidado! Ya existe un usuario registrado con este correo. Cancelando el registro.')
                    continue #Envía a menu principal
                    
                print('Recuerda que los tiempos permitidos son: 5, 10, 15 y 30 días.')
                tiempo = int(input('Querido usuario, defina el tiempo de préstamo --> '))
                while not funciones.ValidarTiempoPrestamo(tiempo):
                    print('Error: Tiempo no válido. Solo se permiten 5, 10, 15 o 30 días.')
                    tiempo = int(input('Intenta de nuevo: '))
                    
                nuevo_usuario= {'cedula': cedula, 'nombre': nombre, 'apellido': apellido, 
                        'correo': correo, 'tiempo_limite': tiempo, 'cantidad_prestamos': 0}
                usuarios.append(nuevo_usuario)
                    
                print('\n')
                print('*' *ESPACIADO)
                print('¡Registro completado con éxito!'.center(ESPACIADO))
                print('¡Muchas gracias por registrarte!'.center(ESPACIADO))
                print('*'*ESPACIADO)
                
            case '2':
                
                print('\tEstás en la opción 2. Registra el ítem')
                
                print('\n[SEGURIDAD] Esta opción requiere permisos de administrador.')
                usuario_admin= input('Ingrese el usuario del administrador -->: ')
                contraseña_admin= input('Ingrese la contraseña -->: ')
                
                if usuario_admin != ADMIN_USUARIO or contraseña_admin != ADMIN_CONTRASEÑA:
                    print('ACCESO DENEGADO. Credenciales incorrectas. Regresando al menú...')
                    continue
                
                else:
                    print('ACCESO CONCEDIDO.')
                    nombre_item = input('Ingrese el nombre del ítem --> ')
                    while len(nombre_item) < 3:
                        print('El nombre debe tener al menos 3 caracteres.')
                        nombre_item = input('Ingrese el nombre del ítem --> ')
                
                    print('\nCategorías disponibles (Marque solo el número):')
                    print('1. Videojuegos')
                    print('2. Libros')
                    print('3. Música y video')
                    print('4. Herramientas')
                    print('5. Dinero')
                    print('6. Misceláneo y varios')
                
                    categoria = input('Seleccione una categoría --> ')
                    while categoria not in ['1','2','3','4','5','6']:
                        print('Categoría no válida.')
                        categoria = input('Seleccione una categoría --> ')
                
                    precio = float(input('Ingrese el precio de compra --> '))
                    while precio <= 0:
                        print('El precio debe ser mayor que cero.')
                        precio = float(input('Ingrese el precio de compra --> '))
                
                    estado = int(input('Ingrese el estado del ítem (1 a 100) --> '))
                    
                    while estado < 1 or estado > 100:
                        print('El estado debe estar entre 1 y 100.')
                        estado = int(input('Ingrese el estado del ítem (1 a 100) --> '))
                
                    if estado >= 80:
                        estado_texto = 'Excelente'
                
                    elif estado >= 50:
                        estado_texto = 'Bueno'
                
                    else:
                        estado_texto = 'Regular'
                
                    id_item = funciones.GenerarID(categoria, contador_items)
                    contador_items += 1
                
                    nuevo_item = {
                        'id': id_item,
                        'nombre': nombre_item,
                        'categoria': categoria,
                        'precio': precio,
                        'estado': estado_texto,
                        'disponible': True
                    }
                
                    inventario.append(nuevo_item)
                
                    print('Ítem registrado correctamente.')
                    print('ID asignado:', id_item)
                
                
            case '3':
                print('\tEstás en la opción 3. Registra el préstamo')
                
                cedula_buscar= input('Ingrese la cédula del usuario --> : ')
                
                #se va a validar si el usuario existe
                usuario_encontrado= None
                for i in usuarios:
                    if i['cedula'] == cedula_buscar:
                        usuario_encontrado = i
                        
                if usuario_encontrado is None:
                    print('Error. El usuario no existe. Debe registrarse primero en la opción 1. ')
                    continue
                
                #Ahora se mostrarán los ítems del inventario
                
                print('\n---- Inventario de ítems ----')
                for item in inventario:
                    if item['disponible']:
                        id_item= item['id']
                        nombre_item= item['nombre']
                        estado_item= item['estado']
                        
                        print('id:', id_item, '|', nombre_item, '-', 'Estado:', estado_item)
                
                id_solicitado= input('Ingrese el ID del ítem que desea prestar: ').upper()
                
                item_encontrado= None
                for item in inventario:
                    if item['id'] == id_solicitado and item['disponible']:
                        item_encontrado= item
                        
                if item_encontrado is None:
                    print('Ítem no disponible o no existe. ')
                else:
                    item_encontrado['disponible']= False
                    nuevo_prestamo = {
                        'id_item': item_encontrado['id'],
                        'nombre_item': item_encontrado['nombre'],
                        'precio_item': item_encontrado['precio'],
                        'cedula_usuario': usuario_encontrado['cedula'],
                        'nombre_usuario': usuario_encontrado['nombre'],
                        'dias_pactados': usuario_encontrado['tiempo_limite'],
                        'activo': True,
                        'mora': False
                        }
                    prestamos.append(nuevo_prestamo)
                    print(f'¡Éxito! Préstamo  registrado. El usuario tiene {usuario_encontrado['tiempo_limite']} días. ')
                    
                    usuario_encontrado['cantidad_prestamos'] += 1
                    
                    
            case '4':
                print('\tEstás en la opción 4. Registra la devolución')
                cedula_devolucion=input('Ingrese la cédula del usuario para la devolución -->: ') 
                tiene_prestamos= False
                
                for p in prestamos:
                    if p['cedula_usuario']==cedula_devolucion and p['activo']:
                        tiene_prestamos= True
                        prestamo_actual= p 
                if not tiene_prestamos:
                    print('El usuario no tiene préstamos activos en el sistema.')
                    continue
                dias_utilizados = int(input('¿Cuántos días tuvo el artículo prestado? --> '))

                if dias_utilizados <= prestamo_actual['dias_pactados']:
                
                    prestamo_actual['activo'] = False
                
                    for item in inventario:
                        if item['id'] == prestamo_actual['id_item']:
                            item['disponible'] = True
                
                    fecha_actual = funciones.ObtenerFechaActual()
                  
                    funciones.GenerarCertificadoDevolucion(
                      prestamo_actual['nombre_usuario'],
                      prestamo_actual['id_item'],
                      fecha_actual
                    )
                
                    devoluciones_cont += 1
                
                    print('Devolución registrada correctamente.')
                
                else:
                    prestamo_actual['mora'] = True
                    print('El usuario excedió el tiempo del préstamo.')
                    
                
            case '5':
                print('\tEstás en la opción 5. Consulta items con +30 días')
                
                hay_vencido=False
                
                for prestamo in prestamos:
                    # Si el préstamo sigue vigente y se pasó de 30 días...
                    if prestamo['activo'] and prestamo['mora']:
                        
                        # Crea factura
                        factura = funciones.GenerarFacturaVenta(
                            prestamo['nombre_usuario'], 
                            prestamo['id_item'], 
                            prestamo['nombre_item'], 
                            prestamo['precio_item']
                        )
                        
                        #Suma plata al dia 
                        total_pago_ventas += factura
                        ventas_realizadas.append({
                            'usuario': prestamo['nombre_usuario'],
                            'id_item': prestamo['id_item'],
                            'nombre_item': prestamo['nombre_item'],
                            'valor': factura
                        })
                        
                        # 3. Cierra prestamo. ya se cobro producto
                        prestamo['activo'] = False
                        
                        
                        hay_vencido= True
                        print(f"Venta forzada aplicada a {prestamo['nombre_usuario']}. Factura generada.")
                
                #si nadie debía
                if not hay_vencido:
                    print('No se encontraron usuarios en mora con préstamos mayores a 30 días.')
    
                
            case '6':
                print('\tEstás en la opción 6. Consulta el artículo prestado')
                
                for i in range(len(prestamos)):

                    for j in range(len(prestamos) - 1):

                        if prestamos[j]['dias_pactados'] > prestamos[j + 1]['dias_pactados']:

                            temporal = prestamos[j]

                            prestamos[j] = prestamos[j + 1]

                            prestamos[j + 1] = temporal

                hay_prestamos = False
            
                for prestamo in prestamos:
            
                    if prestamo['activo']:
            
                        hay_prestamos = True
            
                        print('\nID:', prestamo['id_item'])
                        print('Artículo:', prestamo['nombre_item'])
                        print('Usuario:', prestamo['nombre_usuario'])
                        print('Cédula:', prestamo['cedula_usuario'])
                        print('Días pactados:', prestamo['dias_pactados'])
            
                if not hay_prestamos:
                    print('No existen artículos prestados actualmente.')
            case '7':
                print('\tEstás en la opción 7. Entra al ítem de administrador')
              

                usuario_admin = input('Usuario administrador --> ')
                contraseña_admin = input('Contraseña --> ')
            
                if usuario_admin == ADMIN_USUARIO and contraseña_admin == ADMIN_CONTRASEÑA:
            
                    print('\n===== REPORTE ADMINISTRADOR =====')
            
                    print('Total de préstamos registrados:', len(prestamos))
                    print('Total de ítems devueltos:', devoluciones_cont)
                    print('Total de ventas realizadas:', len(ventas_realizadas))
                    print('Total pago realizado:', total_pago_ventas)
                    
                    print('\n--- Artículos vendidos ---')

                    if len(ventas_realizadas) == 0:
                    
                        print('No existen artículos vendidos.')
                    
                    else:
                    
                        for venta in ventas_realizadas:
                    
                            print('Usuario:', venta['usuario'])
                            print('ID:', venta['id_item'])
                            print('Artículo:', venta['nombre_item'])
                            print('Valor pagado:', venta['valor'])
                            print('-' * 30)
                    
                    print('\n--- Usuarios registrados ---')
            
                    for usuario in usuarios:
                        print(
                            usuario['nombre'],
                            usuario['apellido'],
                            '-',
                            usuario['cedula']
                        )
                    if len(usuarios) > 0:
                        
                        mayor = usuarios[0]
                        menor = usuarios[0]
                
                        for usuario in usuarios:
                
                            if usuario['cantidad_prestamos'] > mayor['cantidad_prestamos']:
                                mayor = usuario
                    
                            if usuario['cantidad_prestamos'] < menor['cantidad_prestamos']:
                                menor = usuario
                    
                        print('\nUsuario con mayor cantidad de préstamos:')
                        print(mayor['nombre'], mayor['apellido'])
                    
                        print('\nUsuario con menor cantidad de préstamos:')
                        print(menor['nombre'], menor['apellido'])
                        
                else:
                        print('Credenciales incorrectas.')
                    
            case '8':
                print('\tEstás en la opción 8. Puedes salir. Gracias por usar PrestaFacil. Byee :)')
                break
    
    else: 
        error ='Opcion no disponible, por favor vuelve a intentarlo'
        print(error)
        continue
