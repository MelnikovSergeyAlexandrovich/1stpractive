a = float(input("Введите первое число \n")) #Вводим 1 переменную с клавиатуры
b = float(input("Введите второе число \n")) #Вводим 2 переменную с клавиатуры
c = float(input("Введите третье число \n")) #Вводим 3 переменную с клавиатуры
if a<b<c: # Реализуем цикл, где значения, упорядоченные по возрастанию будут умножены на 2
    a *= 2 # Реализуем умножение 1 переменной на 2
    b *= 2 #Реализуем умножение 2 переменной на 2
    c *= 2 #Реализуем умножение 3 переменной на 2
else: #Если значения не упорядоченны по возрастанию, то заменяем их на противоположные
    a *= -1 #Реализуем замену 1 переменной на противоположную
    b *= -1 #Реализуем замену 2 переменной на противоположную
    c *= -1 #Реализуем замену 3 переменной на противоположную

print( a,"\n", b ,"\n" , c ) #Реализуем вывод полученных переменных


