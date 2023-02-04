# 3.2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# n = int(input("Введите число n: "))
# list = []
# multipl = []
# for i in range (1,n+1):
#     list.append(i)
# print(list)
# if len(list) % 2 !=0:
#    for i in range(0, len(list)//2+1):
#        multipl.append(list[i]*list[len(list)-i-1])
# elif len(list) % 2 ==0:
#     for i in range(0, len(list)//2):
#        multipl.append(list[i]*list[len(list)-i-1])
# print(multipl)

n = int(input("Введите четное число n: "))
list_main2 = [x for x in range (1,n+1)]
print(list_main2)
help_list = [x for x in list_main2[len(list_main2):len(list_main2)//2-1:-1]]
result_list = list(map(lambda i, x: i*x,[i for i in list_main2[0:len(list_main2)//2+1:1]],[x for x in list_main2[len(list_main2):len(list_main2)//2-1:-1]]))
print(f'Произведение первого и второго числа равно третьему {list(zip(list_main2,help_list,result_list ))}')