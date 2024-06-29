import random


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center_x = x + width // 2
        self.center_y = y + height // 2

    def draw(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                screen[self.y + i][self.x + j] = '#'


def generate_rooms(screen, num_rooms):
    rooms = []
    padding = 1  # Задаем промежуток между комнатами

    for _ in range(num_rooms):
        width = random.randint(4, 8)
        height = random.randint(3, 6)
        # Учитываем промежуток при генерации координат комнат
        x = random.randint(0, len(screen[0]) - width - padding - 1)
        y = random.randint(0, len(screen) - height - padding - 1)

        overlap = False
        for room in rooms:
            # Проверка перекрытия с учетом промежутка между комнатами
            if (x <= room.x + room.width + padding and x + width + padding >= room.x and
                    y <= room.y + room.height + padding and y + height + padding >= room.y):
                overlap = True
                break

        if not overlap:
            # Создаем комнату, если перекрытия нет
            new_room = Room(x, y, width, height)
            rooms.append(new_room)
            new_room.draw(screen)
    return rooms


def print_screen(screen):
    clear_screen()  # Очистка экрана перед выводом
    for row in screen:
        print("".join(row))


# Подготовка экрана и генерация комнат
width, height = 40, 20
screen = [[' ' for _ in range(width)] for _ in range(height)]
rooms = generate_rooms(screen, 5)
print_screen(screen)
