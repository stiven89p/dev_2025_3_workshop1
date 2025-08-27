class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        reves = []

        for caracter in lista:
            reves.insert(0,caracter)
        
        return reves
    
    def buscar_elemento(self, lista, elemento):
        for i, valor in enumerate(lista):
            if valor == elemento:
                return i 
        return -1
        
    def eliminar_duplicados(self, lista):
        sin_duclicado = []
        for elemento in lista:
            if not any(elemento == x and type(elemento) == type(x) for x in sin_duclicado):
                sin_duclicado.append(elemento)
        return sin_duclicado
    
    def merge_ordenado(self, lista1, lista2):
        lista_combinada = []

        lista_combinada = lista1 + lista2

        lista_combinada.sort()

        return lista_combinada
    
    def rotar_lista(self, lista, k):
        if not lista:
            return lista

        n = len(lista)
        k = k % n

        lista = lista[-k:] + lista[:-k]

        return lista
    
    def encuentra_numero_faltante(self, lista):

        n = len(lista) + 1
        for contador in range(1, n+1):
            if contador not in lista:
                return contador
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
        
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [list(fila) for fila in zip(*matriz)]