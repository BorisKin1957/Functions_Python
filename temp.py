def multiply_by_three(x):
  return x * 3

def apply_operation(operation, value):
  return operation(value)

# Дополните код, чтобы получить результат 15
result = apply_operation(multiply_by_three, 5)
print(result)