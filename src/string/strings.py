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
        resultado = []
        anterior = ""
        for c in texto:
            if c == " " and anterior == " ":
                continue
            resultado.append(c)
            anterior = c
        return "".join(resultado)
            
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
        resultado = []
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                # desplazar dentro del alfabeto (26 letras)
                resultado.append(chr((ord(c) - base + desplazamiento) % 26 + base))
            else:
                resultado.append(c)  # deja los símbolos, números, espacios igual
        return "".join(resultado)
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        n, m = len(texto), len(subcadena)
        for i in range(n - m + 1):
            if texto[i:i + m] == subcadena:
                posiciones.append(i)
        return posiciones