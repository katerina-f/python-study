import pygame
import random
import math


class Vec2d:

    def __init__(self, vector):
        self.x = vector[0]
        self.y = vector[1]

    def int_pair(self): # получение пары целых чисел
        vec = int(self.x), int(self.y)
        return vec

    def __add__(self, other):  # сумма векторов
        return tuple(x + y for x,y in zip(self.int_pair(), other.int_pair()))

    def __sub__(self, other):  # разность векторов
        return tuple(x - y for x,y in zip(self.int_pair(), other.int_pair()))

    def __mul__(self, other):   # умножение
        if other >= 0:  # на скаляр
            return sum(self.x * other, self.y * other)
        elif isinstance(other, Vec2d): # скалярное умножение
            scalar = sum(x*y for x,y in zip(self, other))
            return scalar

    def __len__(self): # длина вектора
        return int(math.sqrt(sum(x**2 for x in self.int_pair())))

    def speed(self): # скорость вектора
        speed = random.random() * 2, random.random() * 2
        return speed


class Polyline:

    def __init__(self, points, speeds):
        self.points = points
        self.speeds = speeds

    # Персчитывание координат опорных точек
    def set_points(self, points, speeds):
        for p in range(len(points)):
            points[p] = points[p] + speeds[p]
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                speeds[p] = (- speeds[p][0], speeds[p][1])
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                speeds[p] = (speeds[p][0], -speeds[p][1])


    # "Отрисовка" точек
    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color, (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (p.int_pair()[0], p.int_pair()[1]), width)


def get_point(points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))


def get_points(base_points, count):
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res

def get_knot(points, count):
    if len(points) < 3:
        return []
    res = []
    for i in range(-2, len(points) - 2):
        print(points)
        ptn = []
        ptn.append(points[i]*0.5 + points[i + 1]*0.5)
        ptn.append(points[i + 1])
        ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))
        print(ptn)

        res.extend(get_points(ptn, count))

    return res

# Отрисовка справки
def draw_help():
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
                      (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# Основная программа
if __name__ == "__main__":
    SCREEN_DIM = (800, 600)

    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(Vec2d(event.pos))
                speeds.append(Vec2d(event.pos).speed())


        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline = Polyline(points, speeds)
        polyline.draw_points(points)
        polyline.draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            polyline.set_points(points, speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
