class man_to_robot():
    def __init__(self):
        self.x = 1
        self.y = 1
    
    def move(self, direction, value):
        if direction.lower() == 'u':
            if self.y - value < 1:
                return print(f'Робот неможет выйти за границы поля. \nX: {self.x}\nY: {self.y}')
            self.y -= value  
            print(f'Текущая позиция: X: {self.x} Y: {self.y}')

        elif direction.lower() == 'd':
            if self.y + value > 100:
                return print(f'Робот неможет выйти за границы поля. \nX: {self.x}\nY: {self.y}')
            self.y += value
            print(f'Текущая позиция: X: {self.x} Y: {self.y}')
            
        elif direction.lower() == 'r':
            self.x += value
            if self.x > 100:
                self.x -= value
                return print(f'Робот неможет выйти за границы поля. \nX: {self.x}\nY: {self.y}')
            
            print(f'Текущая позиция: X: {self.x} Y: {self.y}')
            
        elif direction.lower() == 'l':
            if self.x - value < 1:
                return print(f'Робот неможет выйти за границы поля. \nX: {self.x}\nY: {self.y}')
            self.x += value
            print(f'Текущая позиция: X: {self.x} Y: {self.y}')

    def start(self):
        user_input = None
        while user_input != 'выйти':
            print('что бы выйти напишите "выйти"')
            direction = input('Введите направление (u,d,r,l): ')
            value = int(input('Введите значение: '))
            
            if direction != None and value != None:
                self.move(direction, value)
            else:
                print('Не корректные значения')


man_to_robot().start()