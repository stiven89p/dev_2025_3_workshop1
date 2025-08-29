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
        
        for columna in range(3):
            if tablero[0][columna] != " " and tablero[0][columna] == tablero[1][columna] == tablero[2][columna]:
                return tablero[0][columna]
        
        for fila in tablero:
            if " " in fila:
                return "continua"
        
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]
        
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        import random
        combinacion = []
        for _ in range(longitud):
            combinacion.append(random.choice(colores_disponibles))
        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
    
        if desde_fila == hasta_fila:
            paso = 1 if desde_col < hasta_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
            return True
        elif desde_col == hasta_col:
            paso = 1 if desde_fila < hasta_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
            return True
        else:
            return False