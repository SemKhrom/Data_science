import numpy as np

'''Игра угадай число'''

number = np.random.randint(1, 101) #загадываем число

count = 0 #количество попыток

while True:
    count+=1
    predict_number = int(input('Угадай число от 1 до 100:'))

    if predict_number > number:
        print('Число больше загаданого')
    elif predict_number < number:
        print('Число меньше загаданого')
    else:
        print(f'Вы угадали! это число {number}, за {count} попыток!')
        break
