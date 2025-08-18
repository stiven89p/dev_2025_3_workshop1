class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        return (a + b) == 2
    
    def OR(self, a, b):
        return (a + b) > 0 
    
    def NOT(self, a):
        if a == 0:
            a=1
        else:
            a=0
        return a
        
    def XOR(self, a, b):
        return a != b
    
    def NAND(self, a, b):
        return a + b < 2
    
    def NOR(self, a, b):
        return a + b == 0
    
    def XNOR(self, a, b):
        return a == b
    
    def implicacion(self, a, b):
        return (not a) or b

        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        pass
    
    def bi_implicacion(self, a, b):
        return a == b