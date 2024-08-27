from random import randrange

tablero = [[1,2,3],[4,'X',6],[7,8,9]]


def display_board(tablero):
#     # La función acepta un parámetro el cual contiene el estado actual del tablero
#     # y lo muestra en la consola.
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {tablero[0][0]}   |   {tablero[0][1]}   |   {tablero[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {tablero[1][0]}   |   {tablero[1][1]}   |   {tablero[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {tablero[2][0]}   |   {tablero[2][1]}   |   {tablero[2][2]}   |
|       |       |       |
+-------+-------+-------+
""")


def enter_move(tablero):
# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    status = True
    while status:
        try:
            movimiento = int(input("elija la casilla a la que quiere marcar: "))
            if movimiento <1 or movimiento>9:
                print("Escoja uno de los valores del tablero.")
                continue
        except:
            print("Algo salio mal.")
            print("Verifique los datos que puso.")

        row = int(movimiento //3.1)
        colum = movimiento % 3
        if colum == 0:
            colum = 2
        else:
            colum -=1

        if tablero[row][colum] == 'X' or tablero[row][colum] == 'O':
            print("Campo ya ocupado.")
        else:
            tablero[row][colum] = 'O'
            status = False
    return victory_for(tablero, 'O')


def make_list_of_free_fields(tablero):
# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    list_disponible= []
    for i in range(3):
        for e in range(3):
            if tablero[i][e] == 'X' or tablero[i][e] == 'O':
                None
            else:
                list_disponible.append((i, e))
    print(list_disponible)
    return list_disponible


def victory_for(tablero, sign):
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    asiertos_d=0
    for i in range(3):
        asiertos_h = 0
        asiertos_v = 0
        for e in range(3):
            if tablero[i][e] == sign:
                asiertos_h +=1
                if asiertos_h == 3:
                    display_board(tablero)
                    print("ganador: ",sign)
                    return sign
        for e in range(3):
            if tablero[e][i] == sign:
                asiertos_v +=1
                if asiertos_v == 3:
                    display_board(tablero)
                    print("ganador: ",sign)
                    return sign
        if tablero[i][i]==sign:
            asiertos_d +=1
            if asiertos_d == 3:
                display_board(tablero)
                print("ganador: ",sign)
                return sign
        lista = [(0,2), (1,1), (2,0)]
    asiertos_d=0
    for i,e in lista:
        if tablero[i][e] == sign:
            asiertos_d +=1
            if asiertos_d == 3:
                display_board(tablero)
                print("ganador: ",sign)
                return sign


def draw_move(tablero):
# La función dibuja el movimiento de la máquina y actualiza el tablero.
    status=True
    while status:
        movimiento = int(randrange(1,10))
        row = int(movimiento //3.1)
        colum = movimiento % 3
        if colum == 0:
            colum = 2
        else:
            colum -=1

        if tablero[row][colum] == 'X' or tablero[row][colum] == 'O':
            None
        else:
            tablero[row][colum] = 'X'
            status=False
    return victory_for(tablero, 'X')


display_board(tablero)
turnos = 0
while turnos <6:
    o =enter_move(tablero)
    if o== 'O':
        print(o)
        break
    x =draw_move(tablero)
    if x == 'X':
        break
    display_board(tablero)