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

        unidades={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        decenas={1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
        centenas={1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
        millares={1:"M",2:"MM",3:"MMM"}

        numero_str = str(numero)[::-1]

        traducido = []

        for i, digito in enumerate(numero_str):
            digito = int(digito)
            if digito == 0:
                continue
            if i == 0:
                traducido.append(unidades[digito])
            elif i == 1:
                traducido.append(decenas[digito])
            elif i == 2:
                traducido.append(centenas[digito])
            elif i == 3:
                traducido.append(millares[digito])
        
        traducido = "".join(traducido[::-1])
        return traducido
    
    def romano_a_decimal(self, romano):
        
        valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        total = 0
        i = 0
        while i < len(romano):
            if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
                total += valores[romano[i + 1]] - valores[romano[i]]
                i += 2
            else:
                total += valores[romano[i]]
                i += 1
        return total
    
    def texto_a_morse(self, texto):

        morse = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','_':'..--.-', '(':'-.--.', ')':'-.--.-'}
        traducido=[]

        texto_mayusculas = texto.upper()

        for letra in texto_mayusculas:
            traducido.append(morse[letra])

        texto_a_morse = " ".join(traducido)
        return texto_a_morse
    
    def morse_a_texto(self, morse):

        cod_morse = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H','..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P','--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X','-.--':'Y', '--..':'Z','.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9', '-----':'0','--..--':',', '.-.-.-':'.', '..--..':'?', '-..-.':'/', '-....-':'-', '..--.-':'_','-.--.':'(', '-.--.-':')', '  ':''}
        traducido=[]

        separado = morse.split()

        for letra in separado:
            traducido.append(cod_morse[letra])

        morse_a_texto = "".join(traducido)
        return morse_a_texto