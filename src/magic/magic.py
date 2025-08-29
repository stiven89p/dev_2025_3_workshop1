class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        a, b = 0, 1
        for contador in range(n):
            a, b = b, a + b
        return a
                                                                                                                                                       
    def secuencia_fibonacci(self, n):
        
        a, b = 0, 1
        serie = []
        for contador in range(n):
            serie.append(a)   
            a, b = b, a + b 
        return serie
    
    def es_primo(self, n):
        if n <= 1:
            return False
        raiz = int(n**0.5)+1
        for contador in range(2,raiz):
            if n%contador == 0:
                return False
        return True
    
    def generar_primos(self, n):
        lista = []
        if n <= 1:
            return lista
        for numero in range(2,n):
            raiz = int(numero**0.5)+1
            es_primo = True
            for contador in range(2,raiz):
                if numero%contador == 0:
                    es_primo = False
                    break
            if es_primo:
                lista.append(numero)
        return lista
    
    def es_numero_perfecto(self, n):
        lista = []
        if n <= 1:
            return 0
        
        for numero in range(1,n):
            if n % numero == 0:
                lista.append(numero)
        return sum(lista) == n
       
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []

        triangulo = []
        for i in range(filas):
            if i == 0:
                triangulo.append([1])
            else:
                prev = triangulo[-1]
                fila = [1]
                for j in range(1, len(prev)):
                    fila.append(prev[j - 1] + prev[j])
                fila.append(1)
                triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        factorial = 1
        for n in range (1,n+1):
            factorial *= n
        return factorial
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        mcm = abs(a * b) // self.mcd(a, b)
        return mcm
    
    def suma_digitos(self, n):
        litas = [int(digito) for digito in str(n)]
        return sum(litas)
    
    def es_numero_armstrong(self, n):
        lista = [int(digito) for digito in str(n)]
        return sum(digito**3 for digito in lista) == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 0 or any(len(fila) != n for fila in matriz):
            return False
        
        suma_objetivo = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
        
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        
        return True