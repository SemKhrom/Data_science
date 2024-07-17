"""Игра угадай число,
компьютер сам загадывает число"""

import numpy as np
from game_v2 import score_game

def binar_search(number:int=1, arr=range(1, 101)) -> int:
    """Угадываем число при помощи 
    бинарного поиска

    Args:
        number, arr (int, list, optional):Загаданое число, Список чисел. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    left = 0 # Левая граница поиска 
    right = len(arr) # Правая граница поиска
    while left <= right: # Цикл завершится когда список окажется пустым
        count += 1 # Инициализируем переменую для подсчета попыток
        midlle = (left + right) // 2 #находим середину диапазона
        if arr[midlle] < number: # если число меньше искомого, отбрасыаем левую часть
            left = midlle
        elif arr[midlle] > number: # если больше, отбрасываем правую
            right = midlle
        else: 
            return count # как только нашли число ,возвращаем количество попыток
    
if __name__ == '__main__':
    # RUN
    score_game(binar_search)
    