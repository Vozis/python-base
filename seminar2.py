from itertools import count
from operator import truediv
import random




print('Hello world')

print('Задание 11')
# # Сформировать список из  N членов последовательности.
# # Для N = 5: 1, -3, 9, -27, 81 и т.д.

def creareList(n):
  my_dict=list(range(0,n))
  new_dict = []
  for i in my_dict:
    a = (-3)**i
    new_dict.append(a)
  return new_dict

print(creareList(5))
print('--------------------')
  

print('Задание 13')
# # Пользователь задаёт две строки. 
# # Определить количество вхождений одной строки в другой.

z = list(input('Введите первую строку: '))
x = list(input('Введите вторую строку: '))

def getAmount(z,x):
  count = 0
  for i in z:
    for j in x:
      if j == i: 
        count +=1
        
  if count == 0:
    print('нет совпадений')
  else:
    print(f'всего найдено {count} совпадений символов') 

getAmount(z,x)
print('--------------------')


c = input('Введите первую строку: ')
v = input('Введите вторую строку: ')

count = 0
start = 0

for i in range(len(c)):
  i = c.find(v, start)
  if i >= 0:
    start = i + 1
    count += 1
  else:
    break
print(count)

result = c.count(v)
print(result)  
print('--------------------')   
        

print('Задание 14')
# # Подсчитать сумму цифр в вещественном числе.

# для вещественных
s = float(input('Введите число: ')) 
a = int(s)
b = (s -int(s))
summ = 0
summ1 = 0

while a != 0:
  summ += int(a % 10)
  a = a // 10
print(f'Сумма целой части равна {summ}')
while b != 0:
  summ += int(b * 10)
  summ1 += int(b * 10)
  b = b * 10 - int(b*10)
print(f'Сумма дробной части равна {summ1}')

print(f'Сумма чисел равнеа {summ}')
print('--------------------')  

# для дробных
p = (input('Введите число: ')) 
x = p.split('.')
o = int(x[0])
i = int(x[1])
summ = 0
summ1 = 0

while o != 0:
  summ += int(o % 10)
  o = o // 10
print(f'Сумма целой части равна {summ}')
while i != 0:
  summ += int(i % 10)
  summ1 += int(i % 10)
  i = i // 10
print(f'Сумма дробной части равна {summ1}')

print(f'Сумма чисел равнеа {summ}')
print('--------------------')  


print('Задание 15')
# # Написать программу получающую набор 
# # произведений чисел от 1 до N.
# # Пример: пусть N = 4, тогда
# # [ 1, 2, 6, 24 ]

def getMultOfDigits(N):
  mult = 2
  my_range = list(range(1,N+1))
  result=[]
  for i in my_range:
    i = i * (mult-1)
    result.append(i)
    mult = i + 1
  return result
  
print(f'Способ 1: {getMultOfDigits(4)}')

def fact(n):
  f = 1
  result1 = []
  for i in range(n):
    f = f * (i+1)
    result1.append(f)
  return result1

print(f'Способ 2: {fact(4)}')
print('--------------------')  

print('Задание 16')
# # Задать список из n чисел последовательности
# # и вывести на экран их сумму

m = int(input('Количество элементов в последовательности: '))

list2 = list(range(m))
summ = 0
summ2 = sum(list2)
for i in list2:
  summ += (i+1)
  
print(f'Сумма числе последовательности: {summ}')
print(summ2)
print('--------------------')  


print('Задание 18')
# # Реализовать алгоритм перемешивания списка. 

old_list = [1,3,45,23,543,6765,4,3,2,4,6,78,68]

def shakeList(list):
  new_list = []
  step = 0
  length = len(old_list)
  n = 0
  
  while step < length:
    m = random.randint(0, length)
    for i in range(length):
      n = (i+1) - m
      a = old_list[n]
      new_list.append(a)
      step +=1
  return new_list

print(shakeList(old_list))

random.shuffle(old_list)
print(old_list)
print('--------------------')  



print('Задание 19')
# # Реализовать алгоритм задания случайных чисел.

def real_numbers(arg1=0, arg2=1, precision=5):
  mult = 10**precision
  return map(lambda x: x / mult, range(arg1*mult,arg2*mult+1))

list3 = list(real_numbers(0,5,2))
length = len(list3)
print(list3)
print(length)
print(random.uniform(-5,5))
