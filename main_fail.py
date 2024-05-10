import tkinter as tk
POS_X = 70
WIDTH = 600
HEIGHT = 550


class Cours_in_TK:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f'{str(WIDTH)}x{str(HEIGHT)}')
        self.main_menu()

    def clear(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(f'{str(WIDTH)}x{str(HEIGHT)}')
        button_menu = tk.Button(self.root, text='Главное меню',
                                font=('Times', 25, 'bold'), command=self.main_menu)
        button_menu.place(x=POS_X, y=HEIGHT-100)

    def back(self, go):
        button_back = tk.Button(self.root, text='Назад',
                                font=('Times', 14, 'bold'), command=go)
        button_back.place(x=POS_X, y=HEIGHT - 150)

    def main_menu(self):
        self.clear()
        button_contact = tk.Button(self.root,
                                   text='Контакты для связи', font=('Times', 25, 'bold'),
                                   command=self.contact)
        button_contact.place(x=POS_X , y=130)
        button_course = tk.Button(self.root,
                                  text='Начать обучение', font=('Times', 25, 'bold'),
                                  command=self.start)
        button_course.place(x=POS_X , y=250)

    def contact(self):
        self.clear()
        label_contact = tk.Label(self.root,
                                 text='vk: https://vk.com/audios672707836\n\nTelegram: https://t.me/biaka_boliaka',
                                 font=('Times', 15))
        label_contact.place(x=POS_X , y=100)

    def start(self):
        self.clear()
        button_classic = tk.Button(self.root,
                                   text='Основы программирования',
                                   font=('Times', 25, 'bold'), command=self.vanil)
        button_classic.place(x=POS_X, y=100)
        button_OOP = tk.Button(self.root,
                                   text='ООП',
                                   font=('Times', 25, 'bold'), command=self.oop)
        button_OOP.place(x=POS_X, y=200)

    def vanil(self):
        self.clear()

        button_v = tk.Button(self.root, text='Переменные',
                             font=('Times', 25, 'bold'), command=self.value)

        button_type = tk.Button(self.root, text='Типы данных',
                                font=('Times', 25, 'bold'), command=self.type_value)

        button_if_else = tk.Button(self.root, text='Условная конструкция',
                                   font=('Times', 25, 'bold'), command=self.if_else)

        self.back(self.start)

        list_button = [button_v,
                       button_type,
                       button_if_else]
        y = 50
        for i in list_button:
            i.place(x=POS_X, y=y)
            y += 70

    def value(self):
        self.clear()
        self.back(self.vanil)
        text = '''
Переменная – это именованная область памяти.

У переменной есть: имя и значение.

Имена переменных не могут начинаться с цифр и состоять из символов,
отличных от английского алфавита, а также содержать дополнительные 
символы (за исключением нижнего подчеркивания).
Пробел использовать в имени переменной нельзя.
В Python имена переменных принято писать строчными буквами.
Капсом обозначаются константы, то есть значения
этих переменных нельзя менять (программа это позволит сделать, 
а вот совесть и карма пострадают).
Примеры переменных:
number = 7 (number -> имя, 7 -> значение)
name = 'Python'
baby_1 = "Tony"
'''
        label = tk.Label(self.root, text=text, font=('Times', 14))
        label.place(x=3, y=10)

    def if_else(self):
        self.clear()
        self.back(self.vanil)

    def type_value(self):
        self.clear()
        text='''
Типы данных делятся на изменяемые и не изменяемые.
К изменяемым относятся -> списки, словари и множества.
К НЕизменяемым относятся -> числа (int и float), кортежи, строки.
        '''
        label_type = tk.Label(self.root, text=text,
                              font=('Times', 14, 'bold'))
        label_type.place(x=2, y=10)

        button_lst = tk.Button(self.root, text='Списки',
                               font=('Times', 14, 'bold'),
                               bg='lightblue',
                               command=self.lst_l)

        button_dict = tk.Button(self.root, text='Словари',
                               font=('Times', 14, 'bold'),
                                bg='lightblue',
                                command=self.dict_l)

        button_set = tk.Button(self.root, text='Множества',
                               font=('Times', 14, 'bold'),
                               bg='lightblue',
                               command=self.set_l)

        button_number = tk.Button(self.root, text='Числа',
                                font=('Times', 14, 'bold'),
                                bg='salmon', command=self.number_l)

        button_tuple = tk.Button(self.root, text='Кортежи',
                               font=('Times', 14, 'bold'),
                                bg='salmon', command=self.tuple_l)

        button_str = tk.Button(self.root, text='Строки',
                                  font=('Times', 14, 'bold'),
                                  bg='salmon', command=self.str_l)

        self.back(self.vanil)

        list_button = [button_lst,
                       button_dict,
                       button_set,
                       button_number,
                       button_tuple,
                       button_str]
        y = 110
        for i in list_button:
            i.place(x=POS_X, y=y)
            y += 45

    def set_l(self):
        self.clear()
        self.back(self.type_value)
        text = '''
        тут будут методы для множеств...'''
        label = tk.Label(self.root, text=text, font=('Times', 14))
        label.place(x=3, y=10)

    def tuple_l(self):
        self.clear()
        self.back(self.type_value)

    def number_l(self):
        self.clear()
        self.back(self.type_value)
        text = '''Числа – не изменяемый тип данных.
5 она и в Африке 5, а вот 55 это уже не 5. То есть значение изменилось.
С числами работают все математические операции:
+ сложение
- вычитание
* умножение
** возведение в степень (2 ** 3 -> два с степени три)
/ вещественное деление (5 / 2 = 2.5)
// целочисленное деление (5 // 2 = 2, остаток отбрасывается)
% нахождение остатка (5 % 2 = 1, дели столбиком и поймешь почему)
Числа можно сравнивать между собой:
5 == 4 -> False
7 == 7 -> True
 Числа бывают целыми -> 7 (int)
 И вещественными (с плавающей точкой) -> 7.001 (float)'''

        label = tk.Label(self.root, text=text, font=('Times', 14))
        label.place(x=3, y=10)

    def dict_l(self):
        self.clear()
        self.back(self.type_value)

    def lst_l(self):
        self.clear()
        self.back(self.type_value)

    def str_l(self):
        self.clear()
        self.back(self.type_value)

    def oop(self):
        self.clear()

    def run(self):
        self.root.mainloop()


if __name__=='__main__':
    go = Cours_in_TK()
    go.run()





