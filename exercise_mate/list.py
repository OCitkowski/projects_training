# Настав час запускати масове виробництво роботів!
# Щоб роботи на лінії збиралися правильно, потрібно
# маркувати деталі. Різні частини робота будуть складатися
# з різної кількості деталей. Тож зробимо наліпки для них!
# Напиши функцію make_stickers, яка приймає число details_count
# і рядок robot_part. Функція повинна повертати список рядків у
# наступному форматі: {robot_part} detail #{n} (наприклад, Hand detail #1).
# Зверни увагу: якщо details_count = 0, поверни порожній список.
import math


# Наліпки готові? Чудово! Тепер потрібно збільшити продуктивність
# наших ліній удвічі!
# Напиши функцію double_power, яка приймає список потужностей
# current_powers та повертає список із подвоєними значеннями.

#
# А тепер навчимо наших роботів сортувати коробки на складі.
# Кожна коробка має свій унікальний номер, а роботи
# вчаться сортувати їх в порядку зростання.
# Але сортування — справа нелегка, іноді трапляються помилки.
# Тому нам поки що доведеться перевіряти,
# чи правильно робот відсортував коробки.
# Для цього напиши функцію is_sorted,
# яка отримує список чисел box_numbers і повертає True,
# якщо всі числа розташовані в порядку зростання, або False — якщо ні.

# Ускладнюємо роботу нашого робота!
# Тепер він вміє перетворювати команди руху на правильний сигнал
# і рухатися відповідно до нього:
#     "forward" означає y + 1 (крок уперед);
#     "back" означає y - 1 (крок назад);
#     "right" означає x + 1 (крок праворуч);
#     "left" означає x - 1 (крок ліворуч).
# Але було б чудово, щоб робот знав, де він знаходиться навіть без GPS.
# Для цього реалізуй функцію get_location, яка приймає 2 параметри:
#     список початкових координат coordinates у вигляді [x, y];
#     список із командами commands у вигляді ["command1", "command2", "command3" ...].
# Функція повинна повертати список кінцевих координат [x, y]
# після рухів згідно команд зі списку commands.
# Наприклад, ми маємо список із координатами coordinates = [2, 1]
# та список із командами commands = ["left", "back", "back"]:
#     координати після першої команди — [1, 1] (1 крок ліворуч);
#     координати після другої команди — [1, 0] (1 крок назад);
#     координати після третьої команди — [1, -1] (1 крок назад);
#     результатом буде список [1, -1].

# А тепер настав час збільшити обсяги виробництва роботів!
# Напиши функцію get_plan, яка приймає 3 параметри:
#     current_production — поточна кількість роботів, яку ми виробляємо за місяць;
#     months — кількість місяців, протягом якої виробництво має зростати;
#     percent — відсоток, на який має зростати виробництво щомісяця.
# Функція має повертати список із цілями на кожен місяць
# (скільки роботів треба виробити щоб дотримуватись запланованого зростання).
# Щоб краще зрозуміти, як це працює, розглянемо приклад.
# рипустимо, нам дано current_production = 200, months = 3 та percent = 50:
#     план на перший місяць — 200 + 50% = 300 роботів;
#     на другий місяць це вже 300 + 50% = 450 роботів;
#     і нарешті на третій місяць це 450 + 50% = 675 роботів.
# В результаті маємо отримати список [300, 450, 675].
# Зверни увагу: ціль на наступний місяць потрібно рахувати на основі попереднього місяця.
# Якщо число роботів виявиться дробовим, округли його за допомогою math.floor.

# Перша партія роботів готова, тепер їх треба перевірити. Усі роботи унікальні,
# і швидкість руху в кожного своя. У цьому завданні тобі потрібно знайти найменшу,
# найбільшу та середню швидкості роботів.
# Напиши функцію get_speed_statistic, яка приймає список швидкостей
# роботів test_results і повертає статистику у вигляді списку, у якому:
#     перший елемент — найменша швидкість;
#     другий елемент — найбільша швидкість;
#     третій елемент — середнє значення, округлене вниз (використай math.floor).
# Зверни увагу: якщо вхідний список швидкостей порожній — поверни [0, 0, 0].

def make_stickers(details_count: int, robot_part: str) -> list:
    details = []
    for detail in range(1, details_count + 1):
        details.append(f'{robot_part} detail #{detail} ')

    return details


def double_power(current_powers: list) -> list:
    for i in range(len(current_powers)):
        current_powers[i] *= 2
    return current_powers

    # write your code here
    pass


def is_sorted(box_numbers: list) -> bool:
    return sorted(box_numbers) == box_numbers


def get_location(coordinates: list, commands: list) -> list:
    # [x, y]
    list_commands = ['left', 'right', 'forward', 'back']
    for command in commands:

        if command in list_commands:
            if command == list_commands[0]:
                coordinates[0] -= 1
            elif command == list_commands[1]:
                coordinates[0] += 1
            elif command == list_commands[2]:
                coordinates[1] += 1
            elif command == list_commands[3]:
                coordinates[1] -= 1

        else:
            pass

    return coordinates


def get_plan(current_production: int, month: int, percent: int) -> list:
    production_month = []
    # production_month.append(current_production)
    for i in range(0, month):
        current_production += math.floor(current_production * percent / 100)
        production_month.append(current_production)

    return production_month


def get_speed_statistic(test_results: list) -> list:
    '''
    перший елемент — найменша швидкість;
    другий елемент — найбільша швидкість;
    третій елемент — середнє значення, округлене вниз (використай math.floor).
    Зверни увагу: якщо вхідний список швидкостей порожній — поверни [0, 0, 0].
    '''
    if len(test_results) > 0:
        results = []
        s_test_result = sorted(test_results)
        results.append(s_test_result[0])
        results.append(s_test_result[-1])
        results.append(math.floor(sum(s_test_result) / len(s_test_result)))
    else:
        results = [0, 0, 0]

    return results


if __name__ == "__main__":
    print(get_speed_statistic([]))  # [0, 0, 0]
    print(get_speed_statistic([10]))  # [10, 10, 10]
    print(get_speed_statistic([8, 9, 3, 12]))  # [3, 12, 8]
    print(get_speed_statistic([10, 10, 11, 9, 12, 8]))  # [8, 12, 10]

    # print(get_plan(10, 4, 30))  # [13, 16, 20, 26]
    # print((get_plan(1000, 6, 20)))  # [1200, 1440, 1728, 2073, 2487, 2984]

    #
    # get_plan(10, 4, 30)  # [13, 16, 20, 26]
    # print(get_location([0, 0], ["forward", "right"]) ) # [1, 1]
    # print(get_location([2, 3], ["back", "back", "back", "right"]) ) # [3, 0]
    # print(get_location([0, 5], ["back", "back", "back", "right", "left", "forward"]) ) # [0, 3]

    # print(is_sorted([1, 2, 3, 4, 5]) ) # True
    # print(is_sorted([0, 1, 1, 1, 2]) ) # True
    # print(is_sorted([4, 1, 1, 1, 2]))  # True
    # print(is_sorted([1, 2, 11]) ) # True

    # print(double_power([100, 150, 200, 220]))
# {robot_part} detail #{n}
# make_stickers(3, "Body")  # ["Body detail #1", "Body detail #2", "Body detail #3"]
# make_stickers(4, "Head")  # ["Head detail #1", "Head detail #2", "Head detail #3", "Head detail #4"]
# make_stickers(0, "Foot")  # []
