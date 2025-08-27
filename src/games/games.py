class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):

        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        if jugador1 == "invalid" or jugador2 == "invalid":
            return "invalid"
        elif jugador1 == jugador2:
            return "empate"
        elif jugador1 == "piedra":
            if jugador2 == "tijera":
                return "jugador1"
            else:
                return "jugador2"
        elif jugador1 == "tijera":
            if jugador2 == "papel":
                return "jugador1"
            else:
                return "jugador2"
        elif jugador1 == "papel":
            if jugador2 == "piedra":
                return "jugador1"
            else:
                return "jugador2"
  
    def adivinar_numero_pista(self, numero_secreto, intento):

        if numero_secreto == intento:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        # Revisar columnas
        for c in range(3):
            if tablero[0][c] != " " and tablero[0][c] == tablero[1][c] == tablero[2][c]:
                return tablero[0][c]

        # Revisar diagonales
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        # Si no hay ganador, verificar si hay espacios vacíos
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si no hay espacios vacíos y nadie ganó → empate
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass