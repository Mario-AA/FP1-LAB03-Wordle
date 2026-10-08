from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    for char in cadena:
        if not char.isalpha():
            return False
    if len(cadena)!=5:
        return False
    return True

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    tiempo = fin-inicio
    min = (tiempo.seconds)//60
    seg = (tiempo.seconds)%60
    return min, seg

def quitar_letra(cadena:str,caracter:str)->str:
    for char in cadena:
        if char == caracter:
            cadena = cadena.replace(char,"",1)
            return cadena
    return cadena

def marcar_verdes(cadena:str, intento:str):
    verdes = "" 
    restantes = ""
    for c in range (0, len(cadena)):
        if cadena[c] == intento[c]:
            verdes +="V"
        else:
            verdes += "_"
            restantes += cadena[c]
    return verdes,restantes


def marcar_amarillos(intento,verdes,restantes):
    colores = ""
    for c in range ( 0, len(intento)):
        if verdes[c] == "V":
            colores += "V"
        elif intento[c] in restantes:
            colores += "A"
        else:
            colores += "_"
    return colores
def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    verdes, restantes = marcar_verdes(palabra_secreta,intento)

    colores = marcar_amarillos(intento, verdes, restantes)
    
    return colores # Elimina esta línea cuando la implementes


