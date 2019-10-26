from typing import Sequence
import math


def mean(x: Sequence[float]) -> float:
    return sum(x) / len(x)


def mean_sdv(x: Sequence[float]) -> (float, float):
    mean_simple = mean(x)
    mean_square = mean([i ** 2 for i in x])
    sdv = math.sqrt(mean_square - mean_simple ** 2)
    # <==>
    sdv = math.sqrt(sum((xi - mean_simple) ** 2 for xi in x) / len(x))
    return mean_simple, sdv


def cars(models, colors):
    return [f'{c} {m}' for c, m in zip(colors, models)]


def cars_with_years(models, colors, year_start):
    color_cars = cars(models, colors)
    return [f'{c} {i}' for i, c in enumerate(color_cars, year_start)]


def check_for_else(x: Sequence):
    """
    Zwroc pierwsza liczbe podzielna przez 3
    """
    for xi in x:
        if xi % 3 == 0:
            val = xi
            break
    else:  # Jesli petla nie zostala przerwana przez break
        val = 0
        print('Nie ma zadnej liczby podzielnej przez 3')
    return val



if __name__ == '__main__':
    # print(mean_sdv([1, 2, 2, 3]))
    # print(cars(models=['Volvo', 'Skoda', 'BMW'], colors=['Red', 'Blue', 'Green', 'White']))
    """
    print(cars_with_years(models=['Volvo', 'Skoda', 'BMW'],
                          colors=['Red', 'Blue', 'Green', 'White'],
                          year_start=1994))"""
    print(check_for_else([2, 4, 6]))
