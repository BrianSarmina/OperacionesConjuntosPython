########################################### Programa_Conjuntos #############################################

# $Autor: Ing. Brian Sarmina, correo: brian.garsar.6@gmail.com$ #

# Programa para generar operaciones de conjuntos, conjuntos de "numeros" o "letras".

# Se definen dos clases para poder operar los conjuntos, la primera clase corresponde a la clase "ConjuntosLetras", este clase se encarga de operar los conjuntos
# que contienen caracteres o cadenas de caractertes.

class ConjuntosLetras:

    # Metodo constructor para las variables internas de la clase, como se pude notar no es necesario el paso de parametros al formar el objeto de la clase en
    # el main() ya que la clase se encargara de solicitar esa informacion y guardarla en sus variables de clase.

    def __init__(self):

        self.operacion = ''
        self.dicc_universo = {}
        self.dicc_a = {}
        self.dicc_b = {}
        self.dicc_a_union_dicc_b = {}
        self.dicc_a_interseccion_dicc_b = {}
        self.dicc_a_diferencia_dicc_b = {}
        self.dicc_a_complemento = {}
        self.dicc_b_complemento = {}

    # Funcion para solicitar los datos de los conjuntos, donde ademas se crean los diccionarios que se usaran para programar y operar los conjuntos dados,
    # ademas, esta funcion sirve como "menu" para elegir que tipo de operacion se desea realizar o si quiere realizar todas las operaciones juntas.

    def generar_conjuntos_letras(self):

        conjunto_a = input("Ingresa los elementos del conjunto A (ejemplo: a,b,c,d ; sin espacios, solo comas): ")
        conjunto_b = input("Ingresa los elementos del conjunto B (ejemplo: e,f,g,h ; sin espacios, solo comas): ")
        universo_contexto = input("Ingresa los elementos del universo de contexto (ejemplo: a,b,c,..,n ; sin espacios, solo comas): ")

        # Aqui se usa la funcion "str.split()" que sirve para realizar un parsing del string que se ingreso por consola, en este caso se realiza la separacion
        # de los elementos mediante una coma ",", que definira cuando empieza y cuando termina cada elemento.
        vals_a = conjunto_a.split(',')
        vals_b = conjunto_b.split(',')
        vals_universo = universo_contexto.split(',')

        letras_a = []
        letras_b = []
        letras_universo = []

        # Se gerean los vectores o arreglos de los elementos "puros" de cada conjunto.
        for i in vals_a:
            letras_a.append(i)
        for j in vals_b:
            letras_b.append(j)
        for k in vals_universo:
            letras_universo.append(k)

        # Generamos los diccionarios par A, B y el universo de contexto, usando los vectores de elementos "puros" ya creados.
        dicc_a = {'A': letras_a}
        dicc_b = {'B': letras_b}
        dicc_universo = {'O': letras_universo}

        
        # Se solicita que ingrese algun tipo de instruccion valida enlistada, para realizar las operacines entre conjuntos.
        tipo_operacion = input("Que tipo de operación de conjuntos con letras deseas realizar (Union de conjuntos, Interseccion de conjuntos, Diferencia de conjuntos, Complemento de conjuntos o Todas): ")

        # Almacenamos esa informacion en las variables de las clases para que las distintas funciones tengan acceso a la informacion y puedan realizar
        # operaciones con ella.
        self.operacion = tipo_operacion
        self.dicc_a = dicc_a
        self.dicc_b = dicc_b
        self.dicc_universo = dicc_universo

        
        # En caso de ingresar "Todas", se realizan todas las funciones programadas para operaciones de conjuntos.
        if self.operacion == "Todas":
            ConjuntosLetras.union_conjuntos_letras(self)
            ConjuntosLetras.interseccion_conjuntos_letras(self)
            ConjuntosLetras.diferencia_conjuntos_letras(self)
            ConjuntosLetras.complemento_conjuntos_letras(self)

        # Redirecciona a la funcion o metodo de clase "union_conjuntos_letras".
        if self.operacion == "Union de conjuntos":
            ConjuntosLetras.union_conjuntos_letras(self)
            
        # Redirecciona a la funcion o metodo de clase "interseccion_conjuntos_letras".
        if self.operacion == "Interseccion de conjuntos":
            ConjuntosLetras.interseccion_conjuntos_letras(self)

        # Redirecciona a la funcion o metodo de clase "diferencia_conjuntos_letras".
        if self.operacion == "Diferencia de conjuntos":
            ConjuntosLetras.diferencia_conjuntos_letras(self)
            
        # Redirecciona a la funcion o metodo de clase "diferencia_conjuntos_letras".
        if self.operacion == "Complemento de conjuntos":
            ConjuntosLetras.complemento_conjuntos_letras(self)

            
    # Funcion encargada de realizar la operacion de union entre los conjuntos A y B.
    def union_conjuntos_letras(self):

        print("Union de Conjuntos")
        elementos_union = []
        
        # Agregamos todos los elementos de A.
        for i in self.dicc_a['A']:
            elementos_union.append(i)
            
        # Agregamos los elementos de B, si no se encuentran ya en el vector de "elementos_union"-
        for j in self.dicc_b['B']:
            if j not in elementos_union:
                elementos_union.append(j)
            else:
                continue

        # Creamos un diccionario que contenga los elementos "puros" del vector "elementos_union".
        dicc_a_union_dicc_b = {'AUB': elementos_union}
    
        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto A U B: ", dicc_a_union_dicc_b)

        # Actualizamos el valor de la variable de clase "self.dicc_a_union_dicc_b".
        self.dicc_a_union_dicc_b = dicc_a_union_dicc_b


    # Funcion encargada de realizar la operacion de interseccion entre los conjuntos A y B
    def interseccion_conjuntos_letras(self):

            print("Intersección de conjuntos")
            elementos_interseccion = []

            # Agregamos todos los elementos de A que tambien se encuentren en B.
            for i in self.dicc_a['A']:
                if i in self.dicc_b['B']:
                    elementos_interseccion.append(i)
                else:
                    continue

            # Creamos el diccionario para contener el resultado  
            dicc_a_interseccion_dicc_b = {'A(I)B': elementos_interseccion}
        
            print("Conjunto A: ", self.dicc_a)
            print("Conjunto B: ", self.dicc_b)    
            print("Conjunto A (I) B: ", dicc_a_interseccion_dicc_b)

            # Actualizamos variable de clase "self.dicc_a_interseccion_dicc_b" con el resultado obtenido, en caso de que no exista resultado se mantiene un
            # valor de vacio [], que viene del vector "elementos_interseccion".
            self.dicc_a_interseccion_dicc_b = dicc_a_interseccion_dicc_b


    # Funcion encargada de realizar la operacion de diferencia entre conjuntos A y B (se interpreta como A-B)
    def diferencia_conjuntos_letras(self):

        print("Diferencia de conjuntos")
        elementos_diferencia = []

        # Iteramos sobre todos los elementos de A, en caso de que el elemento de A no se encuentre en B, lo agregamos al vector "elementos_diferencia".
        for i in self.dicc_a['A']:
            if i not in self.dicc_b['B']:
                elementos_diferencia.append(i)
            else:
                continue
            
        # Creamos el diccionario para almacenar el resultado obtenido.    
        dicc_a_diferencia_dicc_b = {'A-B': elementos_diferencia}
    
        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto A - B: ", dicc_a_diferencia_dicc_b)

        # Actualizamos la variable de clase "self.dicc_a_diferencia_dicc_b", en caso de que no haya elementos "compartidos" entre A y B, se interpreta que
        # el resultado = A.
        self.dicc_a_diferencia_dicc_b = dicc_a_diferencia_dicc_b


    # Funcion encargada de realizar la operacion de complemento para los conjuntos A y B (Ac y Bc).
    def complemento_conjuntos_letras(self):

        print("Complemento de conjuntos")
        elementos_complemento_a = []
        elementos_complemento_b = []

        # Iteramos sobre todos los elementos del universo de contexto, si el elemento del universo de contexto no se encuentra en A o B, es tomado como elemento
        # perteneciente al complemento de Ac o Bc respectivamente.
        for i in self.dicc_universo['O']:
            if i not in self.dicc_a['A']:
                elementos_complemento_a.append(i)
            if i not in self.dicc_b['B']:
                elementos_complemento_b.append(i)

        # Creamos los diccionarios para conterner los complementos de A y B.
        dicc_a_complemento = {'Ac': elementos_complemento_a}
        dicc_b_complemento = {'Bc': elementos_complemento_b}

        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto Ac: ", dicc_a_complemento)
        print("Conjunto Bc: ", dicc_b_complemento)

        # Actualizamos las variables de clase "self.dicc_a_complemento" (complemento de A) y "self.dicc_b_complemento" (complemento de B).
        self.dicc_a_complemento = dicc_a_complemento
        self.dicc_b_complemento = dicc_b_complemento

    

###############################################################################################################################################################


# Como segunda clase se creo "ConjuntosNumeros" que opera los conjuntos con numeros donde se especifica que por cuestiones de optimizacion, solo opera enteros
# ya que son mas faciles de almacenar y comparar.

# La mecanica de funcionamiento es igual a la clase "ConjuntosLetras".
class ConjuntosNumeros:

    def __init__(self):
        self.operacion = ''
        self.dicc_universo = {}
        self.dicc_a = {}
        self.dicc_b = {}
        self.dicc_a_union_dicc_b = {}
        self.dicc_a_interseccion_dicc_b = {}
        self.dicc_a_diferencia_dicc_b = {}
        self.dicc_a_complemento = {}
        self.dicc_b_complemento = {}
    
    def generar_conjuntos_numeros(self):

        conjunto_a = input("Ingresa los elementos del conjunto A (ejemplo: 1,2,3,4 ; sin espacios, solo comas): ")
        conjunto_b = input("Ingresa los elementos del conjunto B (ejemplo: 1,2,3,4 ; sin espacios, solo comas): ")
        universo_contexto = input("Ingresa los elementos del universo de contexto (ejemplo: 1,2,3,...,n ; sin espacios, solo comas): ") 

        vals_a = conjunto_a.split(',')
        vals_b = conjunto_b.split(',')
        vals_universo = universo_contexto.split(',')

        valores_a = []
        valores_b = []
        valores_universo = []

        # La unica diferencia con la clase "ConjuntosLetras" es que los valores "char" son convertidos a valores enteros en base 10.
        for i in vals_a:
            valores_a.append(int(i))
        for j in vals_b:
            valores_b.append(int(j))
        for k in vals_universo:
            valores_universo.append(int(k))
            
        dicc_a = {'A': valores_a}
        dicc_b = {'B': valores_b}
        dicc_universo = {'O': valores_universo}

        tipo_operacion = input("Que tipo de operación de conjuntos numericos deseas realizar (Union de conjuntos, Interseccion de conjuntos, Diferencia de conjuntos, Complemento de conjuntos o Todas): ")

        self.operacion = tipo_operacion
        self.dicc_a = dicc_a
        self.dicc_b = dicc_b
        self.dicc_universo = dicc_universo

        if self.operacion == "Todas":
            ConjuntosNumeros.union_conjuntos_numeros(self)
            ConjuntosNumeros.interseccion_conjuntos_numeros(self)
            ConjuntosNumeros.diferencia_conjuntos_numeros(self)
            ConjuntosNumeros.complemento_conjuntos_numeros(self)
            
        if self.operacion == "Union de conjuntos":
            ConjuntosNumeros.union_conjuntos_numeros(self)

        if self.operacion == "Interseccion de conjuntos":
            ConjuntosNumeros.interseccion_conjuntos_numeros(self)

        if self.operacion == "Diferencia de conjuntos":
            ConjuntosNumeros.diferencia_conjuntos_numeros(self)

        if self.operacion == "Complemento de conjuntos":
            ConjuntosNumeros.complemento_conjuntos_numeros(self)
        
    def union_conjuntos_numeros(self):    

        print("Union de Conjuntos")
        elementos_union = []

        for i in self.dicc_a['A']:
            elementos_union.append(i)
        for j in self.dicc_b['B']:

            if j not in elementos_union:
                elementos_union.append(j)
            else:
                continue
        
        dicc_a_union_dicc_b = {'AUB': elementos_union}
    
        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto A U B: ", dicc_a_union_dicc_b)

        self.dicc_a_union_dicc_b = dicc_a_union_dicc_b
        


    def interseccion_conjuntos_numeros(self):

        print("Intersección de conjuntos")
        elementos_interseccion = []

        for i in self.dicc_a['A']:
            if i in self.dicc_b['B']:
                elementos_interseccion.append(i)
            else:
                continue
            
        dicc_a_interseccion_dicc_b = {'A(I)B': elementos_interseccion}
    
        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto A (I) B: ", dicc_a_interseccion_dicc_b)

        self.dicc_a_interseccion_dicc_b = dicc_a_interseccion_dicc_b


    def diferencia_conjuntos_numeros(self):

        print("Diferencia de conjuntos")
        elementos_diferencia = []

        for i in self.dicc_a['A']:
            if i not in self.dicc_b['B']:
                elementos_diferencia.append(i)
            else:
                continue
            
        dicc_a_diferencia_dicc_b = {'A-B': elementos_diferencia}
    
        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto A - B: ", dicc_a_diferencia_dicc_b)

        self.dicc_a_diferencia_dicc_b = dicc_a_diferencia_dicc_b


    def complemento_conjuntos_numeros(self):

        print("Complemento de conjuntos")
        elementos_complemento_a = []
        elementos_complemento_b = []

        for i in self.dicc_universo['O']:
            if i not in self.dicc_a['A']:
                elementos_complemento_a.append(i)
            if i not in self.dicc_b['B']:
                elementos_complemento_b.append(i)

        dicc_a_complemento = {'Ac': elementos_complemento_a}
        dicc_b_complemento = {'Bc': elementos_complemento_b}

        print("Conjunto A: ", self.dicc_a)
        print("Conjunto B: ", self.dicc_b)    
        print("Conjunto Ac: ", dicc_a_complemento)
        print("Conjunto Bc: ", dicc_b_complemento)

        self.dicc_a_complemento = dicc_a_complemento
        self.dicc_b_complemento = dicc_b_complemento

###############################################################################################################################################################

# Funcion main(), se encarga de iniciar el programa y generar los objetos dependiendo si se busca operar conjuntos de letras o numeros (enteros), tambien detiene
# el programa al ingresar "Ninguna".
if __name__ == '__main__':

    while True:

        # Preguntamos por el tipo de conjunto que se busca operar.
        tipo_de_dato = input("Iniciando pograma, tipos de elementos en tus conjuntos (Numeros, Letras o Ninguna): ")

        # Se detiene el programa en caso de ingresar "Ninguna" via terminal.
        if tipo_de_dato == "Ninguna":
            print("Programa terminado...")
            break
        # Al ingresar "Numeros" generamos un objeto de la clase "ConjuntosNumeros" y llamamos al metodo o funcion de clase ("generar_conjuntos_numeros")
        # usando el objeto creado.
        elif tipo_de_dato == "Numeros":
            conjunto_numerico = ConjuntosNumeros()
            conjunto_numerico.generar_conjuntos_numeros()

        # Al ingresar "Letras" generamos un objeto de la clase "ConjuntosLetras" y llamamos al metodo o funcion de clase ("generar_conjuntos_letras")
        # usando el objeto creado.
        elif tipo_de_dato == "Letras":
            conjunto_letras = ConjuntosLetras()
            conjunto_letras.generar_conjuntos_letras()
        else:
            continue
            
