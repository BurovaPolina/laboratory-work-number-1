#

def calculate_total_calories(combination):
    return sum(ice_cream[2] for ice_cream in combination)


def find_optimal_combination(ice_creams):
    min_calories = float('inf')
    optimal_combination = []

    for ice_cream in ice_creams:
        total_calories = ice_cream[2]
        if total_calories < min_calories:
            min_calories = total_calories
            optimal_combination = [ice_cream]

    return optimal_combination


def find_optimal_combination_target(ice_creams):
    min_calories = float('inf')
    optimal_combination = []

    for i in range(1, len(ice_creams) + 1):
        combinations = find_combinations(ice_creams, i)
        for combination in combinations:
            total_calories = calculate_total_calories(combination)
            if total_calories < min_calories:
                min_calories = total_calories
                optimal_combination = combination

    return optimal_combination


def find_combinations(lst, k):
    if k == 0:
        return [[]]
    if not lst:
        return []

    result = []
    first = lst[0]
    rest = lst[1:]
    for comb in find_combinations(rest, k - 1):
        result.append([first] + comb)
    result.extend(find_combinations(rest, k))
    return result


def main():
    ice_creams = [
        ("Брикет1", "качественное", 100),
        ("Брикет2", "некачественное", 150),
        ("Брикет3", "некачественное", 120),
        ("Брикет4", "качественное", 80),
        ("Брикет5", "некачественное", 110),
        ("Брикет6", "качественное", 90),
        ("Брикет7", "некачественное", 130),
        ("Брикет8", "качественное", 70),
        ("Брикет9", "некачественное", 140),
        ("Брикет10", "качественное", 60),
    ]

    mode = input("Выберите режим программы: '1' или '2': ")
    days = 7

    if mode.lower() == '1':
        total_calories = 0

        for day in range(days):
            optimal_combination = find_optimal_combination(ice_creams)
            total_calories += calculate_total_calories(optimal_combination)

            print("День", day + 1)
            print(optimal_combination[0][0])
            print("Калории:", calculate_total_calories(optimal_combination), '\n')

            ice_creams.remove(optimal_combination[0])

        print("Общее количество потребленных калорий:", total_calories)
    elif mode.lower() == '2':
        total_calories = 0

        for day in range(days):
            optimal_combination = find_optimal_combination_target(ice_creams)
            total_calories += calculate_total_calories(optimal_combination)

            print("День", day + 1)
            for ice_cream in optimal_combination:
                print(ice_cream[0])
            print("Калории:", calculate_total_calories(optimal_combination), '\n')

            for ice_cream in optimal_combination:
                ice_creams.remove(ice_cream)

        print("Общее количество потребленных калорий:", total_calories)
    else:
        print("Некорректный режим программы.")


main()
