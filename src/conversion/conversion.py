class Conversion:
    def celsius_a_fahrenheit(self, celsius):

        Fahrenheit = (celsius * 9/5) + 32
        return Fahrenheit
    
    def fahrenheit_a_celsius(self, fahrenheit):

        celsius = (fahrenheit - 32) * 5/9
        return celsius
        
    def metros_a_pies(self, metros):

        pies = metros * 3.28084
        return pies
    
    def pies_a_metros(self, pies):

        metros = pies * 0.3048
        return metros
    
    def decimal_a_binario(self, decimal):
        
        binario = bin(int(decimal))[2:]
        return binario
    
    def binario_a_decimal(self, binario):

        decimal = int(binario,base=2)
        return decimal
        
    def decimal_a_romano(self, numero):


        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        pass
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    def texto_a_morse(self, texto):

        morse = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','_':'..--.-', '(':'-.--.', ')':'-.--.-'}
        traducido=[]

        texto_mayusculas = texto.upper()

        for letra in texto_mayusculas:
            traducido.append(morse[letra])

        texto_a_morse = " ".join(traducido)
        return texto_a_morse
    
    def morse_a_texto(self, morse):

        cod_morse = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H','..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P','--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X','-.--':'Y', '--..':'Z','.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9', '-----':'0','--..--':',', '.-.-.-':'.', '..--..':'?', '-..-.':'/', '-....-':'-', '..--.-':'_','-.--.':'(', '-.--.-':')', ' ':''}
        traducido=[]

        separado = morse.split()

        for letra in separado:
            traducido.append(cod_morse[letra])

        morse_a_texto = " ".join(traducido)
        return morse_a_texto