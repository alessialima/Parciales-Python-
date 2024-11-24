#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

# Ejercicio 1 
def ultima_aparicion(s: list[int], e: int) -> int: 
    contador: int = 0
    contador2: int = 0
    ultimo: int 

    for j in range(len(s)): # calcula cuantos e hay dentro de la lista 
        if s[j] == e: 
            contador += 1
            j += 1
        else: 
            j += 1
    contador        

# sabiendo cuantos hay en total, lo busco y devuelvo su posicion
    for i in range(len(s)):
        while contador != contador2:
            if e == s[i]:
                contador2 += 1
                i += 1
            else:
                i += 1  
        i -= 1              
        return i

print(ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1], 0))

#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

# Ejercicio 2 
    
def pertenece(elem: int, lista: list[int]) -> bool:
    i: int = 0
    for i in range(len(lista)):
        if lista[i] == elem: 
            return True 
    return False    

def eliminar_repetidos(lista: list[int]) -> list[int]:
    i: int = 0 

    while len(lista) > i:
        if lista.count(lista[i]) != 1:
            lista.remove(lista[i])
            i += 1
        else: 
            i += 1    
    return lista        

def elementos_exclusivos(s:list[int], t:list[int]) -> list[int]:
    lista_final: list[int] = [] # primero quiero eliminar los elementos repetidos en ambas listas 
    i: int = 0

    for i in range(len(s)): 
        if not(pertenece(s[i], t)):
            lista_final.append(s[i])

    for j in range(len(t)):
        if not(pertenece(t[j], s)):
            lista_final.append(t[j])        
    return eliminar_repetidos(lista_final)

print(elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1], [0,100,5,0,100,-1,5]))        

# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

# Ejercicio 3 
def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res: int = 0

    for palabra in ingles.keys(): 
        if palabra in aleman.keys() and ingles[palabra] == aleman[palabra]: 
            res += 1 
    
    return res

ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}  #escribo que corno es cada diccionario 
aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}

print("Diccionario en inglés:", ingles) # esto que no se para que es 
print("Diccionario en alemán:", aleman)

print("Cantidad de traducciones iguales:", contar_traducciones_iguales(ingles, aleman))

#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}    

# Ejercicio 4 

def cantidad_de_veces(lista: list[int], elem: int) -> int: 
 contador: int = 0
 for i in range(len(lista)):
    if lista[i] == elem: 
        contador += 1
 return contador        

def convertir_a_diccionario(lista: list[int]) -> dict: 
    diccionario: dict = {} # siempre hago aparecer un diccionario vacio como si fuera una lista

    for a in lista: # recorro 
        diccionario[a] = cantidad_de_veces(lista, a) # diccionario[coso] = valor 
    return diccionario 

print(convertir_a_diccionario([1,2,3,4,1,4,5,2]))