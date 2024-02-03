def print_natural_numbers(m, n):
    if m > n:
        return ""
    else:
        return str(m) if m == n else f"{m}, " + print_natural_numbers(m + 1, n)

def sum_natural_numbers(m, n):
    if m > n:
        return 0
    else:
        return m + sum_natural_numbers(m + 1, n)

def ackermann_function(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_function(m - 1, 1)
    else:
        return ackermann_function(m - 1, ackermann_function(m, n - 1))

def main():
    task = int(input("Введите номер задачи (64, 66, или 68): "))
    
    if task == 64:
        m = int(input("Введите M: "))
        n = int(input("Введите N: "))
        print(f"Числа от {m} до {n}: {print_natural_numbers(m, n)}")
    elif task == 66:
        m = int(input("Введите M: "))
        n = int(input("Введите N: "))
        print(f"Сумма чисел от {m} до {n}: {sum_natural_numbers(m, n)}")
    elif task == 68:
        m = int(input("Введите M: "))
        n = int(input("Введите N: "))
        print(f"Результат функции Аккермана для A({m}, {n}): {ackermann_function(m, n)}")
    else:
        print("Некорректный номер задачи. Пожалуйста, введите 64, 66, или 68.")

if __name__ == "__main__":
    main()
