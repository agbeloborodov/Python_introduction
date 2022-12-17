'''  Задание 8_1. Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»'''

class Soup:
    def __init__(self, first_product):
        self.first_product = first_product
    def show_my_soup(self, any_product):
        self.any_product = any_product
        if self.first_product == self.any_product or self.first_product in self.any_product:
            return print(f'Суп - из {self.first_product}')
        else:
            return print(f'Обычный кипяток')

first_soup = Soup('Говядина')
first_soup.show_my_soup('Говядина, овощи')      # Проверка с добавками
second_soup = Soup('Свинина')
second_soup.show_my_soup('Свинина')             # Проверка точного совпадения
any_soup = Soup('Баранина')
any_soup.show_my_soup('Топор, вода и соль')     # Проверка полного несовпадения

