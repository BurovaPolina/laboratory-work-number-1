"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

В холодильнике 10 брикетов мороженого разного вида. Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю."""


# вернуть полный список для разных вариантов
def get_full_list():
    return [
        ("Шоколад", "качественное", 100),
        ("Банан", "некачественное", 150),
        ("Клубника", "некачественное", 120),
        ("Апельсин", "качественное", 80),
        ("Ваниль", "некачественное", 110),
        ("Лесные ягоды", "качественное", 90),
        ("Облепиха", "некачественное", 130),
        ("Смородина", "качественное", 70),
        ("Крем-брюле", "некачественное", 140),
        ("Сыр", "качественное", 60),
    ]


# получить количество каллорий для списка combination
def calculate_total_calories(combination):
    return sum(ice_cream[2] for ice_cream in combination)


# выборка для всех вариантов от текущего day
def default_selection(ice_creams, day, days):
    for sub_day in range(day, days):
        # проходим для каждого по выборке от 0 до 2
        total_calories = 0
        for selection in range(3):
            print('День:', sub_day + 1)
            if len(ice_creams[:selection]) == 0:
                print('список пуст, количесиво калорий 0')
            else:
                total_calories += calculate_total_calories(ice_creams[selection:])
                print('количество калорий в день', sub_day, ' :', calculate_total_calories(ice_creams[selection:]))
                print('ice_creams:', len(ice_creams[:selection]), ice_creams[:selection])
            del ice_creams[:selection]
    return total_calories


def main():
    days = 7
    print("==========================================")
    print("Берем мороженое без ограничения от 0 до 2")
    print("==========================================")
    total_calories = 0
    # проходим по дням каждый с каждым
    for day in range(days):
        ice_creams = get_full_list()

        total_calories += default_selection(ice_creams, day, days)

    print('общее количество калорий: ', total_calories, '\n\n')

    print("==========================================")
    print("Берем мороженое сначало с минимальными каллориями")
    print("==========================================")

    total_calories = 0
    # проходим по дням каждый с каждым
    for day in range(days):
        ice_creams = get_full_list()
        print('общее количество калорий: ', total_calories, '\n\n')
        # сортируем предпочтение тем что с минимальными каллориями
        ice_creams = sorted(ice_creams, key=lambda ice_cream: ice_cream[2])
        total_calories += default_selection(ice_creams, day, days)
    print('общее количество калорий: ', total_calories, '\n\n')

    print("==========================================")
    print("Берем мороженое сначало качественное")
    print("==========================================")

    # проходим по дням каждый с каждым
    for day in range(days):
        ice_creams = get_full_list()

        # сортируем предпочтение качественному
        ice_creams = sorted(ice_creams, key=lambda ice_cream: ice_cream[1])
        total_calories += default_selection(ice_creams, day, days)
    print('общее количество калорий: ', total_calories)


main()
