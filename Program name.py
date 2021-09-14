from math import sqrt
a=[]                         #Массив, в котором будет происходить магия
while True:
        print("Введите количество значений, которые обработает программа")
        kolvo=int(input())
        if kolvo<3:
            print("У треугольника не может быть меньше трёх сторон")
        else:
            break
while True:
    print("Введите значение")
    znach=int(input())
    if znach<=0:
        print("Введённое число должно быть больше нуля")
    else:
        a.append(znach)
        if len(a)==kolvo:
            break
a.sort(reverse=True)
max=0                         #Вспомогательное значение
while True:
    s1=a[max]                 #Первая сторона
    s2=a[max+1]               #Вторая сторона
    s3=a[max+2]               #Третья сторона
    if (s1<s2+s3) and (s2<s1+s3) and (s3<s1+s2):                #Проверка существования треугольника
        p=(s1+s2+s3)/2                                          #Расчёт полупериметра для теоремы Герона
        squre=sqrt(p*(p-s1)*(p-s2)*(p-s3))                      #Расчёт площади по теореме Герона
        print(f"Первая сторона: {s1}")
        print(f"Вторая сторона: {s2}")
        print(f"Третья сторона: {s3}")
        print(f"Площадь: {squre}")
        break
    if s3==a[kolvo-1]:
        print("Невозможно создать  ни одного треугольника")
        break
    max+=1


