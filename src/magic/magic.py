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

        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        pass
    
    def factorial(self, n):
        factorial = 1
        for n in range (1,n+1):
            factorial *= n
        return factorial
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        pass
    
    def suma_digitos(self, n):
        litas = [int(digito) for digito in str(n)]
        return sum(litas)
    
    def es_numero_armstrong(self, n):
        lista = [int(digito) for digito in str(n)]
        return sum(digito**3 for digito in lista) == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass