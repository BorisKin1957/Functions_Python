def countdown(n):
    """
  Эта функция-генератор должна выдавать числа от n до 1.
  Например, для n=3 она должна выдать 3, потом 2, потом 1.
  """
    # Напишите ваш код здесь
    result = []
    if n > 0:
        for i in range(n):
            result.append(n - i)
    return result


# Этот код не нужно отправлять в решение, он для проверки
for number in countdown(5):
    print(number)