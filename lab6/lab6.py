"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

В холодильнике 10 брикетов мороженого разного вида. Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю."""

import random


def calculate_total_calories(combination):
    return sum(ice_cream[2] for ice_cream in combination)


def main():
    ice_creams = [
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

    days = 7
    total_calories = 0

    print("Берем мороженое без ограничения от 0 до 2")

    for day in range(days):
        daily_portion = random.randint(0, 2)
        print("День", day + 1)
        # берем несколько из списка от 0 до 2
        portion_list = ice_creams[:daily_portion]
        # удаляем из списка то что съели
        del ice_creams[:daily_portion]
        print('список на день: ', portion_list)
        daily_calories = calculate_total_calories(portion_list)
        print("Количество калорий в день: ", daily_calories)

        total_calories += daily_calories

    print("Общее количество потребленных калорий не благоприятный:", total_calories)

    total_calories = 0

    print("\n\n\nБерем одно из (от 0 до 2) мороженое с наименьшим колличеством каллорий")

    for day in range(days):
        daily_portion = random.randint(0, 2)
        print("День", day + 1)
        # берем несколько из списка от 0 до 2
        portion_list = ice_creams[:daily_portion]
        print('список на день: ', portion_list)
        # если взяли 2 то предпочтение тому что с минимальными каллориями
        if len(portion_list) > 1:
            ice_cream = sorted(portion_list, key=lambda ice_cream: ice_cream[2])[0]
            daily_calories = ice_cream[2]
            # удаляем из списка то что съели
            ice_creams.remove(ice_cream)
        elif len(portion_list) == 1:
            daily_calories = portion_list[0][2]
        else:
            daily_calories = 0

        print("Количество калорий в день: ", daily_calories)
        total_calories += daily_calories

    print("Общее количество потребленных калорий не благоприятный:", total_calories)

 main()
