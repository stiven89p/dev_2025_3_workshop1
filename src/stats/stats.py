class Stats:
    def promedio(self, numeros):
        prom=0
        if len(numeros) == 0:
            return 0
        for i in range(0,len(numeros)):
            prom=numeros[i]+prom
        return prom/len(numeros)
    
    def mediana(self, numeros):
        numeros = sorted(numeros)
        medio = len(numeros)
        if medio == 0:
            return 0
        if medio % 2 == 1:
            return numeros[medio // 2]
        else:
            numero1 = numeros[medio // 2]
            numero2 = numeros[medio // 2 - 1]
            return (numero1 + numero2) / 2
    
    def moda(self, numeros):
        if len(numeros) == 0:
                return None

        repetidos = {}
        for n in numeros:
            if n in repetidos:
                repetidos[n] += 1
            else:
                repetidos[n] = 1
        return max(repetidos, key=repetidos.get)
    
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        pass
    
    def desviacion_estandar(self, numeros):
        if len(numeros) == 0:
            return 0
        
        suma = 0
        media = sum(numeros)/len(numeros)
        
        for i in numeros:
            suma += (i - media)**2 
        desviacion = (suma/(len(numeros)))**0.5

        return desviacion
    
    def varianza(self, numeros):
        suma = 0
        if len(numeros) == 0:
            return 0
        
        media = sum(numeros)/len(numeros)
        
        for i in numeros:
            suma += (i - media)**2 
        varianza = suma/(len(numeros))

        return varianza
    
    def rango(self, numeros):
        if len(numeros) == 0:
            return 0
        
        numeros.sort()
        rango = numeros[-1] - numeros[0]

        return rango