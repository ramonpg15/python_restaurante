
import os # Para el manejo de archivos
CARPETA = 'restaurante/'
EXTENSION = '.txt'

class Platillo:
    def __init__(self, nombre,categoria,precio):
        self.nombre=nombre 
        self.categoria=categoria
        self.precio=precio
        

def app():
    print('Carga inicial')
    # Preguntar si existe una carpeta para guardar el .txt 
    if not os.path.exists(CARPETA):
        #Crea la carpeta
        os.makedirs(CARPETA)
    else:
        print('Carpeta ya existe')
    mostrar_menu()
    # Preguntamos la accion al usuario
    pregunta=True
    while(pregunta):
        opcion= input('Teclea la opción deseada:\r\n')
        opcion = int(opcion)
        if opcion == 1:
            agregar_platillo()
            pregunta=False
        elif opcion == 2:
            editar_platillo()
            pregunta=False
        elif opcion == 3:
            ver_platillos()
            pregunta=False
        elif opcion == 4:
            buscar_platillo()
            pregunta=False
        elif opcion == 5:
            eliminar_platillo()
            pregunta=False
        elif opcion == 6:
            print('ADIOS, REGRESE PRONTO!!!')
            pregunta=False
        else:
            print('Opcion incorrecta')
            pregunta=True
            
            
''' 
* @description: Funcion para mostar el menu al usuario
* @author ramon.perez
* @version 1.0.0,13/05/2022
'''

def mostrar_menu():
    print('Seleccione una opción de las siguientes')
    print('1) Agregar platillo')
    print('2) Editar platillo')
    print('3) Ver platillos')
    print('4) Buscar platillo')
    print('5) Eliminar platillo')
    print('6) Salir')


''' 
* @description: Funcion para agregar un platillo 
* @author ramon.perez
* @version 1.0.0,13/05/2022
'''

def agregar_platillo():
    print('Escribe los datos para agregar el nuevo platillo:')
    nombre_platillo=input('Nombre del platillo: \r\n')
    # Revisamos si existe el platillo o no
    existe = os.path.isfile(CARPETA+nombre_platillo+EXTENSION)
    # Aqui sabemos que no existe por eso abrimos la conexion para crear el platillo
    if not existe:
        with open(CARPETA+nombre_platillo+EXTENSION,'w') as platillos:
            categoria_platillo = input('Ingresa la categoria del platillo:\r\n')
            precio_platillo = input('Ingresa el precio del platillo: \r\n')
            #precio_platillo = int(precio_platillo)
            # Instanciamos la clase
            platillo = Platillo(nombre_platillo,categoria_platillo,precio_platillo)
            platillos.write('Nombre:' + platillo.nombre + '\r\n')
            platillos.write('Categoria:' + platillo.categoria + '\r\n')
            platillos.write('Precio:' + platillo.precio + '\r\n')
            print('Platillo creado con exito')
    else:
        print('Platillo ya existe')
    app()

''' 
* @description: Funcion para editar un platillo
* @author ramon.perez
* @version 1.0.0,13/05/2022
'''

def editar_platillo():
    print('Escribe el nombre del platillo a editar:')
    platillo_anterior = input('Nombre del platillo a editar:\r\n')
    # Preguntar si existe el platillo
    existe = existe_platillo(platillo_anterior)
    if existe:
       with open(CARPETA+platillo_anterior+EXTENSION,'w') as platillo:
        nombre_platillo = input('Escribe el nuevo nombre del platillo:\r\n')
        categoria_platillo = input('Escribe la nueva categoria del platillo:\r\n')
        precio_platillo = input('Escribe el nuevo precio del platillo:\r\n')
        platilloNuevo = Platillo(nombre_platillo,categoria_platillo,precio_platillo)
        platillo.write('Nombre:'+platilloNuevo.nombre+'\r\n')
        platillo.write('Categoria:'+platilloNuevo.categoria+'\r\n')
        platillo.write('Precio:'+platilloNuevo.precio+'\r\n')
        print('Platillo actualizado con existo')
    else:
        print('El platillo no existe')
    app()
       
''' 
* @description: Funcion para listar los platillos
* @author ramon.perez
* @version 1.0.0,13/05/2022
'''   
def ver_platillos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA+archivo) as platillo:
            for linea in platillo:
                print(linea.rstrip())
            print('\r\n')
            
''' 
* @description: Funcion para buscar un platillo 
* @author ramon.perez
* @version 1.0.0,13/05/2022
'''

def buscar_platillo():
    platillo = input('Escribe el platillo a buscar:\r\n')
    try:
        with open(CARPETA+platillo+EXTENSION) as platillo:
            print('\r\n Informacion del platillo:\r\n')
            for linea in platillo:
                print(linea.rstrip())
            print('\r\n')
    except print(0):
        print('El platillo no existe')


''' 
* @description: Funcion para eliminar un platillo
* @author ramon.perez
* @version 1.0.0,13/05/2022
'''

def eliminar_platillo():
    platillo = input('Escribe el nombre del platillo a eliminar:\r\n')
    try:
        os.remove(CARPETA+platillo+EXTENSION)
        print('Platillo eliminado correctamente')
    except print(0):
        print('No existe el platillo')
    
    
''' 
* @description: Funcion para validar si existe un platillo o no
* @author ramon.perez
* @version 1.0.0,13/05/2022
* @param: nombre_platillo que sera el que validaremos si existe
* @returns: True o False segun el nombre del platillo
'''

def existe_platillo(nombre_platillo):
    return os.path.isfile(CARPETA+nombre_platillo+EXTENSION)

app()