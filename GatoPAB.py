import random
import math

def dibujar_tablero(tablero):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(tablero[i][j], end="|")
        print("\n---------")

def revisar_ganador(tablero, jugador):
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True

    # Verificar columnas
    for j in range(3):
        if tablero[0][j] == jugador and tablero[1][j] == jugador and tablero[2][j] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    return False

def obtener_movimientos(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                movimientos.append((i, j))
    return movimientos

def minimax_alpha_beta(tablero, profundidad, alpha, beta, es_turno_max):
    if revisar_ganador(tablero, "X"):
        return 1
    if revisar_ganador(tablero, "O"):
        return -1
    if len(obtener_movimientos(tablero)) == 0:
        return 0

    if es_turno_max:
        mejor_valor = float("-inf")
        for movimiento in obtener_movimientos(tablero):
            i, j = movimiento
            tablero[i][j] = "X"
            valor = minimax_alpha_beta(tablero, profundidad + 1, alpha, beta, False)
            tablero[i][j] = " "
            mejor_valor = max(mejor_valor, valor)
            alpha = max(alpha, mejor_valor)
            if alpha >= beta:
                break
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for movimiento in obtener_movimientos(tablero):
            i, j = movimiento
            tablero[i][j] = "O"
            valor = minimax_alpha_beta(tablero, profundidad + 1, alpha, beta, True)
            tablero[i][j] = " "
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, mejor_valor)
            if beta <= alpha:
                break
        return mejor_valor

def jugar_IA(tablero):
    mejor_valor = float("-inf")
    mejor_movimiento = None
    alpha = float("-inf")
    beta = float("inf")
    for movimiento in obtener_movimientos(tablero):
        i, j = movimiento
        tablero[i][j] = "X"
        valor = minimax_alpha_beta(tablero, 0, alpha, beta, False)
        tablero[i][j] = " "
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
        alpha = max(alpha, mejor_valor)
        if alpha >= beta:
            break
    i, j = mejor_movimiento
    tablero[i][j] = "X"

def jugar_gato():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno_IA = random.choice([True, False])

    while True:
        dibujar_tablero(tablero)

        if turno_IA:
            print("Turno de la IA (X):")
            jugar_IA(tablero)
            if revisar_ganador(tablero, "X"):
                dibujar_tablero(tablero)
                print("¡La IA ha ganado!")
                break
            turno_IA = False
        else:
            print("Tu turno (O):")
            fila = int(input("Ingrese el número de fila (0-2): "))
            columna = int(input("Ingrese el número de columna (0-2): "))

            if tablero[fila][columna] == " ":
                tablero[fila][columna] = "O"
                if revisar_ganador(tablero, "O"):
                    dibujar_tablero(tablero)
                    print("¡Has ganado!")
                    break
                turno_IA = True
            else:
                print("Movimiento inválido. Intente nuevamente.")

        if len(obtener_movimientos(tablero)) == 0:
            dibujar_tablero(tablero)
            print("¡Empate!")
            break

jugar_gato()
