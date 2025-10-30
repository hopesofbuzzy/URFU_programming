from random import randint
import pygame


# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

GRID_CENTER_WIDTH = SCREEN_WIDTH / 2 // GRID_SIZE * GRID_SIZE
GRID_CENTER_HEIGHT = SCREEN_HEIGHT / 2 // GRID_SIZE * GRID_SIZE
GRID_CENTER = (GRID_CENTER_WIDTH, GRID_CENTER_HEIGHT)

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
ZERO = (0, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """
    Базовый класс, от которого наследуются другие игровые объекты.
    Он содержит общие атрибуты игровых объектов —
    например, эти атрибуты описывают позицию и цвет объекта.
    """

    def __init__(self, position=(0, 0), body_color=(255, 255, 255)):
        """
        Конструктор для базового игрового объекта с цветом и позицией

        :param position: стартовая позиция объекта
        :param body_color: цвет игрового объекта
        """
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Абстрактный метод для отрисовки игрового объекта"""
        ...


class Apple(GameObject):
    """
    Класс, унаследованный от GameObject,
    описывающий яблоко и действия с ним.
    Яблоко отображается в случайных клетках игрового поля.
    """

    def __init__(self, position=GRID_CENTER, body_color=APPLE_COLOR):
        """
        Конструктор для класса яблока

        :param position: стартовая позиция яблока, которая затем заменяется
        :param body_color: цвет яблока
        """
        super().__init__(position, body_color)
        self.position = self.randomize_position()

    def randomize_position(self):
        """
        Райндомайзер позиции яблока. Не сравнивает позицию с телом змейки

        :return: новая позиция яблока
        """
        return (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    def draw(self):
        """Метод для отрисовки яблока в определённой позиции в виде квадрата"""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """
    Класс, унаследованный от GameObject, описывающий змейку и её поведение.
    Этот класс управляет её движением, отрисовкой,
    а также обрабатывает действия пользователя.
    """

    def __init__(self, position=GRID_CENTER, body_color=SNAKE_COLOR):
        """
        Конструктор для класса змейки

        :param position: стартовая позиция змейки, которая затем заменяется
        :param body_color: цвет змейки
        """
        super().__init__(position, body_color)
        self.reset_values()

    def update_direction(self):
        """
        Обновляет направление движения змейки.
        next_direction -> direction

        next_direction задаётся сигналами ввода извне.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """
        Двигает змейку в направлении движения.
        Регулирует движение у границ экрана.
        Не проверяет конец хвоста.
        """
        xnew = self.positions[0][0] + self.direction[0] * GRID_SIZE
        ynew = self.positions[0][1] + self.direction[1] * GRID_SIZE
        new_position = (xnew, ynew)
        if new_position[0] < 0:
            new_position = (SCREEN_WIDTH + new_position[0], new_position[1])
        elif new_position[0] >= SCREEN_WIDTH:
            new_position = (new_position[0] - SCREEN_WIDTH, new_position[1])
        elif new_position[1] < 0:
            new_position = (new_position[0], SCREEN_HEIGHT + new_position[1])
        elif new_position[1] >= SCREEN_HEIGHT:
            new_position = (new_position[0], new_position[1] - SCREEN_HEIGHT)
        self.positions = [new_position] + self.positions

    def draw(self):
        """
        Метод для отрисовки змейки. Рисует голову и "затирает" хвост.
        Затирание происходит с помощью цвета фона.
        """
        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """
        Возвращает позицию головы змейки

        :return: координаты позиции головый змейки в формате кортежа (x, y)
        """
        return self.positions[0]

    def reset(self):
        """Перезагружает состояние змейки на начало."""
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
        for position in self.positions:
            last_rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
        self.reset_values()

    def reset_values(self):
        """Перезагружает все значения атрибутов змейки на начало"""
        self.length = 1
        self.direction = RIGHT
        self.next_direction = None
        self.positions = [self.position]
        self.last = ZERO


def handle_keys(game_object):
    """
    Считывает ввод пользователя и передаёт данные в game_object.
    Регулирует контроль змейки и не даёт сделать "невозможный" поворот.
    """
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Метод главного игрового цикла игры"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake(GRID_CENTER, SNAKE_COLOR)
    apple = Apple(GRID_CENTER, APPLE_COLOR)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Проверяем, съела ли змейка яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            # Убедимся, что новая позиция яблока не на теле змейки
            while True:
                apple.position = apple.randomize_position()
                if not (apple.position in snake.positions):
                    break
        else:
            # В ином случае "затираем" конец хвоста
            snake.last = snake.positions[-1]
            snake.positions = snake.positions[:-1]

        # Проверяем, столкнулась ли змейка со своим хвостом
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        # Рисуем змейку и яблоко
        apple.draw()
        snake.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
