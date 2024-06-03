def find_norm_pairs(a, b):
    # Создание пар чисел
    pairs = [(a[i], a[i + 1]) for i in range(0, len(a) - 1, 2)]

    # Проверка делимости суммы пары на заданное число
    norm_pairs = [pair for pair in pairs if sum(pair) % b == 0]

    return norm_pairs



b = int(input("Введите число из первой вставки (от 3 до 20): "))
if b < 3 or b > 20:
    print("N")
else:
    a = list(range(1, 21))
a = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

# Нахождение правильных пар
norm_pairs = find_norm_pairs(a, b)

# Вывод результата
if norm_pairs:
    print("Правильные пары чисел:")
    for pair in norm_pairs:
        print(pair)
else:
    print("Нет подходящих пар.")

# Обработка случая с нечетной длиной последовательности
if len(a) % 2 != 0:
    print(f"Последнее число {a[-1]} осталось без пары.")

