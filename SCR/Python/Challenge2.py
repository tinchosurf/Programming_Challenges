# Reto #2
# LA SUCESIÓN DE FIBONACCI
# Fecha publicación enunciado: 10/01/22
# Fecha publicación resolución: 17/01/22
# Dificultad: DIFÍCIL

# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

num_list = []
num_aux = 0

for i in range (0,50):
    
    if i==0:
        num_list.append(0)
    elif i==1:
        num_list.append(i)
        num_aux = num_list[i]
    else:    
        num_list.append(num_aux + num_list[i-2])
        num_aux= num_list[i]

print(num_list)


# num_list = []

# for i in range(0, 50):
#     if i == 0:
#         num_list.append(0)
#     elif i == 1:
#         num_list.append(1)
#     else:
#         next_fibonacci = num_list[i - 1] + num_list[i - 2]
#         num_list.append(next_fibonacci)

# print(num_list)