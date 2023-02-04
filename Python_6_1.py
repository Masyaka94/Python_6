# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#3.1 Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

# sum = 0
# for i in range (1,n+1):
#     list.append(i)
# for i in range (1,len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(f"Список из {n} элементов: {list}")
# print(f"Сумма нечетных элементов списка {list} равна: {sum}")

n = int(input("Введите число n: "))
list_main = [x for x in range (1,n+1)]
print(list_main)
value = sum(x for index, x in enumerate(list_main) if index % 2 == 1)
print(value)
