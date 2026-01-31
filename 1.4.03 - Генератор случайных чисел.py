'''Задача 3: Генератор случайных чисел

Условие:
Напишите функцию-генератор random_numbers(count, limit), которая генерирует
последовательность из count случайных целых чисел. Каждое число должно
быть в диапазоне от 1 до limit включительно.'''


import random

from typing import Generator # вызван лишь для аннотации функции


def random_numbers(count: int, limit: int) -> Generator[int]:
    # for _ in range(count):
    #     yield random.randint(1, limit)

    return (random.randint(1, limit) for _ in range(count))

# Этот код не нужно отправлять в решение, он для проверки
random.seed(42) # Фиксируем случайность для предсказуемого результата

print(list(random_numbers(5, 100)))