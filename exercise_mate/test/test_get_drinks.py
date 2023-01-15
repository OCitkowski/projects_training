from exercise_mate.get_drinks import get_drinks, get_drinks_with_step
from unittest import TestCase


# Основні задачі#
# Рухаємось далі! Тепер навчимося реалізовувати складніші цикли.#
# Одного разу ведучий на весіллі вирішив розважити гостей і встановив правило: кожен гість вимовляє тост, і всі присутні п'ють за здоров'я молодих.
#
# Наприклад:
#
#     коли приходить перший гість, він п'є на самоті;
#     коли приходить другий — п'ють удвох;
#     третій — п'ють утрьох і так далі.#
# Якщо гостей 5, то всього знадобиться 15 порцій (1 + 2 + 3 + 4 + 5).#
# Якщо 10, то 55 порцій (1 + 2 + 3 + ... + 10).#
# Реалізуй функцію get_drinks, яка приймає number_of_guests — скільки всьо


# *****************************

# А тепер напишемо цикл із кроком 😎
# Як ти вже знаєш, для конкурсу з напоями знадобилося безліч порцій. Тому ведучий вирішив змінити правила. Молодята обирають ціле додатне число step, і тепер тост говорить не кожен гість, а тільки перший і кожен, хто приходить через обрану кількість (step) гостей після попереднього тосту. При цьому, як і раніше, п'ють усі присутні.
#
# Наприклад:
#     якщо step = 1, то, як і раніше, тост говорить кожен гість, що прийшов;
#     якщо step = 2, то 1-й, 3-й, 5-й тощо;
#     якщо step = 3, то 1-й, 4-й, 7-й, 10-й тощо.
# Реалізуй функцію get_drinks_with_step, яка приймає number_of_guests і step та повертає потрібну кількість порцій.
class TestGetDrinks(TestCase):

    # todo test
    def test_unique(self):
        self.assertEqual(get_drinks(5), 15, 'is good')


class TestGetDrinksbyStep(TestCase):
    # get_drinks_with_step(0, 5)  # 0 - нема гостей — нема і порцій
    # get_drinks_with_step(10, 3)  # 1 + 4 + 7 + 10 = 22
    # get_drinks_with_step(5, 3)  # 1 + 4 = 5
    # get_drinks_with_step(18, 10)  # 1 + 11 = 12

    # todo test
    def test_unique(self):
        self.assertEqual(get_drinks_with_step(0, 5), 0, 'is good')
        self.assertEqual(get_drinks_with_step(10, 3), 22, 'is good')
        self.assertEqual(get_drinks_with_step(5, 3), 5, 'is good')
        self.assertEqual(get_drinks_with_step(18, 10), 12, 'is good')
