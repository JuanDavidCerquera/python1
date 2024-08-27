# numero = int(input("Ingrese un número entero positivo: "))
# es_primo = True
# if numero <= 1:
#     es_primo = False
# else:
#     for i in range(2, (numero // 2) -1):
#         if numero % i == 0:
#             es_primo = False
#             break
# if es_primo:
#     print("El número es primo.")
# else:
#     print("El número no es primo.")




# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# hacer que la flecha sea el doble de grande (pero mantener las proporciones)

# print("         *               ",end="\n \n"                       )
# print("      *","*              ",end="\n \n",sep="     "           )
# print("    *","*                ",end="\n \n",sep="         "       )
# print("  *","*                  ",end="\n \n",sep="             "   )
# print(" * * *","* * *           ",end="\n \n",sep="       "         )
# print("     *","*               ",end="\n \n",sep="       "         )
# print("     *","*               ",end="\n \n",sep="       "         )
# print("     *","*","*","*","*   ",end="\n \n",sep=" "               )


# duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)

# print("     *     "*2)
# print("    * *    "*2)
# print("   *   *   "*2)
# print("  *     *  "*2)
# print(" ***   *** "*2)
# print("   *   *   "*2)
# print("   *   *   "*2)
# print("   *****   "*2)

# print('Greg\'s book.')
# print(0b1011)

# print((5 * ((25 % 13) + 100) / (2 * 13))/2)
# eo = "007"

# print("Agent " + eo)

# a = '1'
# b = "1"
# print(a + b)

# a = 6
# b = 3
# a /= 2 * b
# print(a)



# anything = input("Dime lo que sea...")
# print("Hmm...", anything, "... ¿en serio?")


# anything = float(input("Ingresa un número:"))
# something = float(anything) ** 2.0
# print(anything, "al cuadrado es", something)
 

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")


# # ingresa un valor flotante para la variable a aquí
# valFloatA = float(input(" ingresa un valor flotante para la variable a aquí: "))
# # ingresa un valor flotante para la variable b aquí
# valFloatB = float(input(" ingresa un valor flotante para la variable b aquí: "))

# # mostrar el resultado de la suma aquí
# print(valFloatA + valFloatB)
# # mostrar el resultado de la resta aquí
# print(valFloatA - valFloatB)
# # mostrar el resultado de la multiplicación aquí
# print(valFloatA * valFloatB)
# # mostrar el resultado de la división aquí
# print(valFloatA / valFloatB)

# print("\n¡Eso es todo, amigos!")

# x=-5
# y= 1/(x+(1/(x+(1/(x+(1/x))))))
# print(y)



# horaInicio      = int(input("ingresar hora de inicio: "))
# minutoInicio    = int(input("ingresar minuto de inicio: "))
# minutoDuracion  = int(input("ingrese el tiempo de duracion del evento: "))

# horafin=horaInicio
# minutofin=minutoInicio + minutoDuracion


# # se le da formato de tiempo (minutos 0 - 60) a la salida de la consola
# if(minutofin>=60):
#     adicionalHoras= minutofin // 60
#     horafin += adicionalHoras
#     minutofin -= adicionalHoras*60

# # se le da formato de tiempo (horas 1-12) a la salida de la consola
#     # if(horafin > 12):
#     #     formatohora = horafin // 12
#     #     horafin -= formatohora*12

# # se le da formato de tiempo (horas 1-24) a la salida de la consola
#     if(horafin > 24):
#         formatohora = horafin // 24
#         horafin -= formatohora*24

# if(minutofin>=10):
#     print("hora fin: ",horafin,":",minutofin , sep="")
# if(minutofin<10):
#     print("hora fin: ",horafin,":0",minutofin , sep="")
# z = y = x = 1
# print(x, y, z, sep='*')

# true = "hola"

# x = 2 / 4
# print(x)
# y = 4 / x

# print(y)

# n = int(input("escribe un numero: "))
# print(n>=100 )

# # Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))

# # Elige el número más grande
# if number1 > number2: larger_number = number1
# else: larger_number = number2

# # Imprime el resultado
# print("El número más grande es:", larger_number)


# num1= int(input("escribe un numero: "))
# num2= int(input("escribe un numero: "))
# num3= int(input("escribe un numero: "))

# largest_num= num1

# if(num2> largest_num):
#     largest_num=num2
    
# if(num3> largest_num):
#     largest_num=num3

# print("numero mas grande: ", largest_num)


# name = input("Introduce el nombre de la flor: ")

# if name == "ESPATIFILIO":
#     print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
# elif name == "espatifilo":
#     print("No, ¡quiero un gran ESPATIFILIO!")
# else:
#     print("¡ESPATIFILIO!, ¡No", name + "!")
	

# while True:
#     print("Estoy atrapado dentro de un bucle.")








# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

# odd_numbers = 0
# even_numbers = 0

# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while number:
#     # Verificar si el número es impar.
#     if number % 2:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)
 

# counter = 5
# while counter:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)



# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)
# secret_number= 2147
# numero_escocido = int(input("escoge un numero: "))
# while numero_escocido != secret_number:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
# print("¡Bien hecho, muggle! Eres libre ahora.")



# for i in range(10):
#     print("El valor de i es", i)

# for i in range(0, 16, 2):
#     print("El valor de i es", i)



# power = 1
# for expo in range(16):
#     print("2 a la potencia de", expo, "es", power)
#     power *= 2

# import time

# for i in range(1,6):
#     print(i,"Mississippi")
#     time.sleep(2.0)
# print("Lista o no, aquí vengo!")


# # break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")



# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")


# largest_number = -99999999
# counter = 0

# number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# while number != -1:
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# if counter:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")




# while True:
#     palabra = input("ingrese la contraseña: ")
#     if(palabra == "chupacabra"):
#         print("Has dejado el bucle con éxito.")
#         break
#     print("contraseña incorrecta.")




# palabra = input("ingrese una palabra: ").upper()
# for letra in palabra:
#     if(letra == "A" or letra == "I" or letra == "O" or letra == "U" or letra == "E"):
#         continue
#     print(letra)


    
# palabra = input("ingrese una palabra: ").upper()
# palbaraMostrar =""
# for letra in palabra:
#     if(letra == "A" or letra == "I" or letra == "O" or letra == "U" or letra == "E"):
#         continue
#     palbaraMostrar+=letra
# print(palbaraMostrar)


# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)


# numcajas= int(input("Ingresa el número de bloques: "))
# altura=0
# i=1
# while numcajas:
#     if(numcajas >= i):
#         altura+=1
#         numcajas -=i
#     else:
#         break
#     i+=1
# print("La altura de la pirámide es: ",altura)


# c0 = int(input("escribe un numero entero que sea mayor a 0: "))
# pasos=0


# while c0 !=1:
#     if(c0 % 2== 0):
#         c0 /=2
#     else:
#         c0 = 3 * c0 + 1
#     pasos +=1
#     print(c0)
# print("pasos=",pasos)


# for i in range(1, 11):
#     if(i %2 != 0):
#         print(i)


# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")


# i = 6
# j = 5
# log = j and i and 2

# print(log)


# i = 134
# log=~i
# print(log)



# flag_register = 1234
# the_mask = 0

# print(bin(flag_register))
# bit = (flag_register >> the_mask) & 1
# print(bit)

# # Cambiar el bit en la posición pos
# numero_cambiado = flag_register ^ (1 << the_mask)
# print(bin(numero_cambiado))


# Borrar el bit en la posición pos
# numero_sin_bit = flag_register & ~(1 << the_mask)
# print(bin(numero_sin_bit))


# x = 8
# y = 1
# print(bin(x))
# print(bin(y))

# b = x | y
# c = ~x
# d = x ^ y
# print(bin(b))
# print(b)

# lista_sombrero = [1,2,3,4,5]
# del lista_sombrero[-1]
# print(len(lista_sombrero))

# my_list = []  # Creando una lista vacía.
# for i in range(5):
#     my_list.insert(0, i + 1)
# print(my_list)


# # a la lista se le asigna una secuencia de cinco valores enteros;
# my_list = [10, 1, 8, 3, 5]
# total = 0
# # la variable i toma los valores 0, 1,2,3, y 4, y luego indexa la lista, seleccionando los elementos
# # siguientes: el primero, segundo, tercero, cuarto y quinto;
# # observa la forma en que se ha empleado la función len() - hace que el código sea independiente de cualquier posible cambio en el contenido de la lista.
# for i in range(len(my_list)):
#     # cada uno de estos elementos se agrega junto con el operador += a la variable suma, dando el resultado final al final del bucle;
#     total += my_list[i]
# print(total)


# # alternar valores de las variables
# variable_1 = 1
# variable_2 = 2

# variable_1, variable_2 = variable_2, variable_1


# # alternar los valores de los valores de los indices de la lista
# my_list = [10, 1, 8, 3, 5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)

# my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# for i in range(len(my_list) // 2):
#     my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]

# print(my_list)




# beatles=[]

# # paso 1
# print("Paso 1:", beatles)
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# # paso 2
# print("Paso 2:", beatles)
# for i in range(2):
#     beatles.append(input("escribe el nombre que faltan"))
# # paso 3
# print("Paso 3:", beatles)
# del beatles[-1]
# del beatles[-1]
# # paso 4
# print("Paso 4:", beatles)
# beatles.insert(0, "Ringo Starr")
# # paso 5
# print("Paso 5:", beatles)


# # probando la longitud de la lista
# print("Los Fav", len(beatles))



# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)


# # auto organizacion
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
# # revertir
# my_list.reverse()
# print(my_list)
 

# a = "A"
# b = "B"
# c = "C"
# d = " "
 
# lst = [a, b, c, d]
# lst.sort()
 
# print(lst)




# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)

# # Copiando la lista completa.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# Copiando parte de la lista.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:4]
# print(new_list)



# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)


# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# print(new_list)


# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)



# my_list = [10, 8, 6, 4, 2]
# del my_list[:]
# print(my_list)


# # in y noy in
# my_list = [0, 3, 12, 8, 2]

# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = 0

# for i in range(0, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)


# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# for i in my_list:
#     for e in my_list[i:]:
#         if(i==e):
#             del my_list[e]



# print("La lista con elementos únicos:")
# my_list.sort()
# print(my_list)


# vehicles_one = ['coche', 'bicicleta', 'motor']
# print(vehicles_one) # output: ['coche', 'bicicleta', 'motor']
 
# vehicles_two = vehicles_one
# del vehicles_two[0] # elimina 'coche'
# print(vehicles_one) 



# my_list = [1, 2, 3, 4, 5]
# slice_one = my_list[2: ]
# slice_two = my_list[ :2]
# slice_three = my_list[-2: ]
 
# print(slice_one)  # output: [3, 4, 5]
# print(slice_two)  # output: [1, 2]
# print(slice_three)  # output: [4, 5]



# squares = [x ** 2 for x in range(10)]

# print(squares)



# board = [[f'{i},{j}' for i in range(8)] for j in range(8)]

# board[0][0] = 'ROOK'
# board[0][7] = 'ROOK'
# board[7][0] = 'ROOK'
# board[7][7] = 'ROOK'
# board[4][2] = 'KNIGHT'
# board[3][4] = 'PAWN'

# for row in range(8):
#     print()
#     for colum in range(8):
#         print(board[colum][row], end=" | ", )


# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # La matriz se actualiza aquí.
# #
 
# total = 0.0
 
# for day in temps:
#     total += day[11]
 
# average = total / 31
 
# print("Temperatura promedio al mediodía:", average)


# highest = -100.0
 
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
# print("La temperatura más alta fue:", highest)

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, v)
# print(my_list)


# def message():
#     print("Ingresar valor: ")
 
# print("Inicia aqui.")
# message()
# print("Termina aqui.")


# def introduction(first_name, last_name):
#     print("Hola, mi nombre es", first_name, last_name)
 
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")


# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# adding(3, c = 1, b = 2)


# El valor por predeterminada para el parámetro se asigna de la siguiente manera:
# def introduction(first_name, last_name="Smith"):
#     print("Hola, mi nombre es", first_name, last_name)

# introduction("Enrique")



# un argumento no predeterminado no puede ir despues de un argumento predeterminado
# def add_numbers(a, b=2, c=3):
#     print(a + b + c)
 
# add_numbers(a=1, c=3)


# none == null
# value = None
# if value is None:
#     print("Lo siento, no contienes ningún valor")



# def is_year_leap(year):
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         return False
#     elif year % 4 == 0:
#         return True
#     return False

# def days_in_month(year,month):
#     if month >12 or month <=0:
#         print("Mes fuera de rango")
#         return None
#     month-=1
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     yaerbis = is_year_leap(year)
#     if yaerbis:
#         if month==1:
#             days[month] +=1
#     return days[month]

# def days_in_day(year,month,day):
#     days= days_in_month(year,month)
#     if days== None:
#         return None
#     elif day > days or day <= 0:
#         print("el mes no tiene esos dias.")
#         return None
#     else:
#         return day


# resultado= days_in_day(int(input("escribe un año: ")), int(input("escribe el numero del mes: ")),int(input("escribe un dia: ")))
# print(resultado)

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#         if md == None:
#             return None
#         days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None

# print(day_of_year(2000, 12, 31))



# def is_year_leap(year):
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         return False
#     elif year % 4 == 0:
#         return True
#     return False

# def days_in_month(year,month):
#     if month >12 or month <=0:
#         print("Mes fuera de rango")
#         return None
#     month-=1
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     yaerbis = is_year_leap(year)
#     if yaerbis:
#         if month==1:
#             days[month] +=1
#     return days[month]

# def days_in_day(year,month,day):
#     days= days_in_month(year,month)
#     if days== None:
#         return None
#     elif day > days or day <= 0:
#         print("el mes no tiene esos dias.")
#         return None
#     else:
#         return day


# def days_in_year(year,month,day):
#     daysYear = 0
#     if month >12 or month <=0:
#         print("Mes fuera de rango")
#         return None
#     month-=1
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     yaerbis = is_year_leap(year)
#     if yaerbis:
#         days[1] +=1
#     for i in range(month):
#         daysYear += days[i]
#     daysYear += day
#     return daysYear

# result = days_in_year(2000,12,31)
# print(result)



# def is_prime(num):
#     if num>1:
#         for i in range(2, int(1 + num ** 0.5)):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False

# num = int(input("Escriba el numero: "))
# if is_prime(num):
#     print(num)
# else:
#     print("No es primo")
# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.

# def liters_100km_to_miles_gallon(liters):
#     gallons = liters / 3.785411784 # litros / galon
#     miles = 100000 / 1609.344 # 100km / milla
#     return miles / gallons

# def miles_gallon_to_liters_100km(miles):
#     km100 = miles * 1609.344 / 100000 # millas / 100km
#     liters = 3.785411784  # litro * galon
#     return liters / km100

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_2 = [0, 1]
#     print("Print #3:", my_list_1)
#     # print("Print #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0] # Presta atención a esta línea.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)


# def is_a_triangle(a, b, c):
#     if a + b < c or b + c <= a or c + a <= b:
#         return False
#     return True
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(3, 2, 5))

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
 
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
 
 
# for n in range(0, 10): # probando
#     print(n, "->", fib(n))


# var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)



# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}

# # Imprimir valores aquí.
# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)
# print(dictionary['gato'])
# print(phone_numbers['Suzy'])


dictionary = {"gato": "cat", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "no está en el diccionario")

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# for spanish, french in dictionary.items():
#     print(spanish, "->", french)

# dictionary["gato"] = "minou"


# for español in sorted(dictionary.keys()):
#     print(español)


# for french in dictionary.values():
#     print(french)


# for spanish, french in dictionary.items():
#     print(spanish, "->", french)


# dictionary['cisne'] = 'cygne'
# print(dictionary)
# del dictionary['perro']
# print(dictionary)
# dictionary.popitem()
# print(dictionary)



# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break

#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
#         break

#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)

# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)



# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
 
# for item in (d1, d2):
#     d3.update(item)
#     # Escribe tu código aquí.
 
# print(d3)


# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)
# print(colors_dictionary)


# colors = {
#     "blanco": (255, 255, 255),
#     "gris": (128, 128, 128),
#     "rojo": (255, 0, 0),
#     "verde": (0, 128, 0)
#     }
 
# for col, rgb in colors.items():
#     print(col, ":", rgb)



# try:
#     value = int(input('Ingresa un número natural: '))
#     print('El recíproco de', value, 'es', 1/value)        
# except:
#     print('No se que hacer con', value)


# try:
#     value = int(input('Ingresa un número natural: '))
#     print('El recíproco de', value, 'es', 1/value)        
# except ValueError:
#     print('No se que hacer con', value)    
# except ZeroDivisionError:
#     print('La división entre cero no está permitida en nuestro Universo.') 



# while True:
#     try:
#         number = int(input("Ingresa un número entero: "))
#         print(5/number)
#         break
#     except (ValueError, ZeroDivisionError):
#         print("Valor incorrecto o se ha roto la regla de división entre cero.")
#     except:
#         print("Lo siento, algo salió mal...")


# value = input("Ingresa un número entero: ")
# print(10/value)

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# print('''
#     asdjasd
#     asdasd
#     asd
#     asda''')


# my_list = [1, 2]
 
# for v in range(2):
#     my_list.insert(-1, my_list[v])
 
# print(my_list)


# def function_1(a):
#     return None
 
 
# def function_2(a):
#     return function_1(a) * function_1(a)
 
 
# print(function_2(2))