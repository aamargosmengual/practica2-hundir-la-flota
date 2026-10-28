import random

LISTA_LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #[cite: 9]
MAP_LETRAS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9} #[cite: 9]

def coordenada_a_indices(coord):
    """Convierte una coordenada como 'B3' a índices de matriz (2, 1)."""
    letra = coord[0].upper()
    numero = int(coord[1:])
    fila = numero - 1
    columna = MAP_LETRAS[letra]
    return fila, columna

def indices_a_coordenada(fila, columna):
    """Convierte índices de matriz (2, 1) a coordenada 'B3'."""
    letra = LISTA_LETRAS[columna]
    numero = fila + 1
    return f"{letra}{numero}"

def crear_tablero_vacio():
    """Crea una matriz de 10x10 inicializada con guiones '-'."""
    return [['-' for _ in range(10)] for _ in range(10)] #[cite: 13]

def es_posicion_valida(tablero, fila, col, tamano, orientacion):
    """Verifica si un barco cabe y tiene 1 casilla de separación alrededor."""
    fila_inicio = max(0, fila - 1)
    col_inicio = max(0, col - 1)
    
    if orientacion == 0:  # Horizontal
        if col + tamano > 10: return False
        fila_fin = min(9, fila + 1)
        col_fin = min(9, col + tamano)
    else:  # Vertical
        if fila + tamano > 10: return False
        fila_fin = min(9, fila + tamano)
        col_fin = min(9, col + 1)

    for f in range(fila_inicio, fila_fin + 1):
        for c in range(col_inicio, col_fin + 1):
            if tablero[f][c] == 'O': #[cite: 16]
                return False
    return True

def colocar_flota(tablero):
    """Coloca aleatoriamente los 10 barcos reglamentarios."""
    flota = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] #[cite: 13]
    
    for tamano in flota:
        colocado = False
        while not colocado:
            orientacion = random.randint(0, 1) #[cite: 13]
            if orientacion == 0:
                fila = random.randint(0, 9)
                col = random.randint(0, 10 - tamano)
            else:
                fila = random.randint(0, 10 - tamano)
                col = random.randint(0, 9)
                
            if es_posicion_valida(tablero, fila, col, tamano, orientacion):
                for i in range(tamano):
                    if orientacion == 0:
                        tablero[fila][col + i] = 'O' #[cite: 16]
                    else:
                        tablero[fila + i][col] = 'O' #[cite: 16]
                colocado = True


def inicializar_pdt():
    """Inicializa la lista de coordenadas pendientes de tiro (100 tuplas)."""
    pdt = []
    for i in range(10):
        for j in range(10):
            pdt.append((i, j))
    return pdt #[cite: 8, 14]

def disparo_aleatorio_ia(pdt):
    """La IA elige un disparo aleatorio y lo extrae de la lista."""
    idx = random.randint(0, len(pdt) - 1) #[cite: 8, 14]
    fila, col = pdt.pop(idx) #[cite: 9, 14]
    return fila, col

def evaluar_disparo(tablero, fila, col):
    """Evalúa el disparo y marca el tablero con 'X' (tocado) o '+' (agua)."""
    if tablero[fila][col] == 'O': #[cite: 16]
        tablero[fila][col] = 'X' #[cite: 7, 14]
        return 'Tocado'
    elif tablero[fila][col] == '-':
        tablero[fila][col] = '+' #[cite: 7, 14]
        return 'Agua'
    return 'Ya disparado'

def turno_usuario(tablero_ordenador, tablero_oculto):
    """Gestiona el disparo del jugador contra el ordenador."""
    valido = False
    while not valido:
        coord = input("Introduce tu jugada (ej. A5): ").strip().upper() #[cite: 7, 14]
        try:
            fila, col = coordenada_a_indices(coord)
            if 0 <= fila <= 9 and 0 <= col <= 9:
                resultado = evaluar_disparo(tablero_ordenador, fila, col)
                if resultado != 'Ya disparado':
                    # Marcamos también en el tablero de seguimiento del jugador
                    tablero_oculto[fila][col] = tablero_ordenador[fila][col]
                    print(f"{resultado}. Has disparado en {coord}.") #[cite: 7]
                    valido = True
                else:
                    print("Ya habías disparado ahí. Intenta de nuevo.")
            else:
                print("Coordenada fuera de límites.")
        except:
            print("Formato inválido. Usa una letra (A-J) y un número (1-10).")

def comprobar_victoria(tablero):
    """Cuenta los impactos ('X'). Si hay 20, la flota completa está hundida."""
    # La flota total tiene 20 casillas: 4 + 3x2 + 2x3 + 1x4 = 20
    tocados = 0
    for fila in tablero:
        tocados += fila.count('X')
    return tocados == 20

def turno_ia(pdt):
    """El ordenador elige un disparo y pregunta al usuario el resultado."""
    fila, col = disparo_aleatorio_ia(pdt)
    coord = indices_a_coordenada(fila, col)
    
    print(f"Ahora tiro yo: {coord}") #[cite: 8]
    valido = False
    while not valido:
        resultado = input("¿Cómo ha resultado mi disparo (A: agua, T: tocado, H: hundido)?: ").strip().upper() #[cite: 8, 14]
        if resultado in ['A', 'T', 'H']:
            if resultado in ['T', 'H']:
                print("Jaja, voy a por ti.") #[cite: 8]
            valido = True
        else:
            print("Por favor, introduce A, T o H.")
    return resultado


if __name__ == "__main__":
    print("Bienvenido a Hundir la Flota!!!") #[cite: 7]
    print("Voy a distribuir mis barcos") #[cite: 7]
    
    # 1. Inicialización
    tablero_ordenador = crear_tablero_vacio()
    colocar_flota(tablero_ordenador)
    tablero_oculto = crear_tablero_vacio() # Donde el usuario anota sus disparos
    pdt = inicializar_pdt() # Memoria de disparos de la IA
    
    print("Ya está. Podemos empezar:") #[cite: 7]
    
    # Variables de control del bucle
    fin_juego = False
    tocados_ia = 0 # Contador manual para los aciertos de la IA
    
    # 2. Bucle principal de la partida
    while not fin_juego: #[cite: 12, 14]
        # Mostrar el tablero del ordenador (para corrección) y el de anotaciones
        print("\n--- MI TABLERO (Ordenador) ---")
        print("   " + " ".join(LISTA_LETRAS))
        for i, fila in enumerate(tablero_ordenador):
            print(str(i + 1).rjust(2) + " " + " ".join(fila))
            
        print("\n--- TU MAPA DE DISPAROS ---")
        print("   " + " ".join(LISTA_LETRAS))
        for i, fila in enumerate(tablero_oculto):
            print(str(i + 1).rjust(2) + " " + " ".join(fila))
        
        # Turno Usuario
        print("\n--- TU TURNO ---")
        turno_usuario(tablero_ordenador, tablero_oculto)
        
        if comprobar_victoria(tablero_ordenador):
            print("\n¡ENHORABUENA! Has hundido toda mi flota. ¡Has ganado!")
            fin_juego = True
            break
            
        # Turno IA
        print("\n--- MI TURNO ---")
        resultado_ia = turno_ia(pdt)
        
        if resultado_ia in ['T', 'H']:
            tocados_ia += 1
            if tocados_ia == 20:
                print("\n¡HE GANADO! He hundido toda tu flota. Suerte la próxima vez.")
                fin_juego = True


