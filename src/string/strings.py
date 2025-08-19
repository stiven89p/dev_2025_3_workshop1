class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):

        texto = str(texto).lower().replace(" ", "")
        invertido = texto[::-1]
        return invertido == texto
    
    def invertir_cadena(self, texto):
        texto = str(texto)
        invertido = texto[::-1]
        return invertido
    
    def contar_vocales(self, texto):
        vocales = "aeiou"
        texto = str(texto).lower()
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        vocales = "qwrtypsdfgghjjklñzxcvbnm"
        texto = str(texto).lower()
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        texto1 = sorted(texto1.replace(" ", ""))
        texto2 = sorted(texto2.replace(" ", ""))

        return texto1 == texto2
    
    def contar_palabras(self, texto):
        separado = texto.split()
        return len(separado)
    
    def palabras_mayus(self, texto):
        return str(texto).title()
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
            
    def es_numero_entero(self, texto):
        vocales = "abcdefghijklmnñopqrstuvwxz"
        texto = str(texto).lower()
        contador = 0
        for letra in texto:
            if letra in vocales:
                return False
        separado = texto.split(".")
        return len(separado) != 2
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass