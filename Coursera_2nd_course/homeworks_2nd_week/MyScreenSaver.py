
from abc import ABC, abstractmethod
import math
import pygame
import random


class Vec2d:

    """
    2D-vectors class

    """

    def __init__(self, vector):
        self.x = vector[0]
        self.y = vector[1]

    def int_pair(self):
        vec = int(self.x), int(self.y)
        return vec

    def __add__(self, other):
        return Vec2d((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Vec2d((self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        if isinstance(other, Vec2d):
            return Vec2d((self.x * other.x, self.y * other.x))
        else:
            return Vec2d((self.x * other, self.y * other))

    def __len__(self):
        return int(math.sqrt(sum(x**2 for x in self.int_pair())))

    def speed(self):
        speed = random.random() * 2, random.random() * 2
        return Vec2d(speed)


class Polyline(ABC):

    """
    Polylines confined class

    """

    def __init__(self):
        self.points = []
        self.speeds = []
        self.count = 35

    def add_point(self, new_point):
        return self.points.append(Vec2d(new_point))

    def add_speed(self, new_point):
        return self.speeds.append(Vec2d(new_point).speed())

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p].x = -self.speeds[p].x
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p].y = -self.speeds[p].y

    @abstractmethod
    def draw_points():
        pass


class Knot(Polyline):

    """
    Smooth curves class

    """

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha \
            + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, base_points, count):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        knots = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            knots.extend(self.get_points(ptn, self.count))
        return knots

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            knots = self.get_knot()
            for p_n in range(-1, len(knots) - 1):
                pygame.draw.line(gameDisplay, color, knots[p_n].int_pair(),
                                    knots[p_n + 1].int_pair(), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color, p.int_pair(), width)

    def get_faster(self):
        for speed in self.speeds:
            if speed.x > 0:
                speed.x += 1
            else:
                speed.x -= 1

            if speed.y > 0:
                speed.y += 1
            else:
                speed.y -= 1

    def get_slower(self):
        for speed in self.speeds:
            if speed.x > 0:
                speed.x -= 1
            else:
                speed.x += 1

            if speed.y > 0:
                speed.y -= 1
            else:
                speed.y += 1

    def delete_point(self, point):
        if self.points != []:
            del self.points[-1]

    def add_point(self, point):
        super().add_point(point)
        self.get_knot()

    def set_points(self):
        super().set_points()
        self.get_knot()


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
    data.append(["Up", "Make speed higher"])
    data.append(["Down", "Make speed lower"])
    data.append(["LeftMouse", "Add point"])
    data.append(["RightMouse", "Delete point"])
    data.append([str(knot.count), "Current points"])

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

    knot = Knot()
    working = True
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
                    knot = Knot()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    knot.count += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    knot.count -= 1 if knot.count > 1 else 0
                if event.key == pygame.K_UP:
                    knot.get_faster()
                if event.key == pygame.K_DOWN:
                    knot.get_slower()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     knot.add_point(event.pos)
            #     knot.add_speed(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    knot.add_point(event.pos)
                    knot.add_speed(event.pos)
                elif event.button == 3:
                    knot.delete_point(event.pos)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knot.draw_points()
        knot.draw_points("line", 3, color)
        if not pause:
            knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
