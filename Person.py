import random
import pygame
from Globals import Globals
from InfectionStatus import InfectionStatus


class Person:

    def __init__(
        self,
        x: int,
        y: int,
        mask: bool,
        socialdistance: bool,
        status: InfectionStatus = InfectionStatus.Susceptible,
        radius: int = Globals.RADIUS_OF_PERSON,
    ):
        self.x = x
        self.y = y
        self.status = status
        self.masked = mask
        self.socialdistancing = socialdistance

        self.color = self.getColorByStatus()

        self.radius = radius
        self.infection_days = 0  # Days since infected

    def move(self, locations: dict[(int, int), list[any]]):
        if self.status != InfectionStatus.Deceased:
            # if not self.socialdistancing:
                # use random walk
                self.x += -random.choice([1, -2, 3, -4, 5])
                self.y += -random.choice([-1, 2, -3, 4, -5])
            # else:
                # """
                # instead of storing the movement it chose in self.x/y, first use a for loop to go through all 25 options and see if anyone is in your personal space bubble.
                # take all the movement options taht work and put them in a list. randomlyu choose one.
                # if there isnt one where people are far enough away, don't move
                # THE END!

                # """
                # all_x_choices: list[int] = [1, -2, 3, -4, 5]
                # all_y_choices: list[int] = [-1, 2, -3, 4, -5]

                # places_safe_to_move = []
                # for x in all_x_choices:
                #     for y in all_y_choices:
                #         not_good = False

                #         for x_social_dist in range(
                #             -Globals.SOCIAL_DISTANCE, Globals.SOCIAL_DISTANCE + 1
                #         ):
                #             if not_good:
                #                 break
                #             x_canidate = self.x + x
                #             for y_social_dist in range(
                #                 -Globals.SOCIAL_DISTANCE, Globals.SOCIAL_DISTANCE + 1
                #             ):
                #                 y_canidate = self.y + y
                #                 test_x = x_canidate + x_social_dist
                #                 test_y = y_canidate + y_social_dist
                #                 if (test_x, test_y) in locations and len(
                #                     locations[(test_x, test_y)]
                #                 ) > 0:
                #                     not_good = True
                #                     break
                #         if not not_good:
                #             places_safe_to_move.append((self.x + x, self.y + y))
                # # Only move if there is a safe place to move
                # if len(places_safe_to_move) > 0:
                #     (self.x, self.y) = random.choice(places_safe_to_move)

            # Have people bounce off the walls and ceiling
                if self.x - self.radius <= 0 or self.x + self.radius >= Globals.WIDTH:
                    self.x = -self.x

                if (
                    self.y - self.radius <= 0
                    or self.y + self.radius >= Globals.HEIGHT + Globals.LEGEND // 2
                ):
                    self.y = -self.y

    def draw(self, screen):
        self.color = self.getColorByStatus()

        pygame.draw.circle(
            screen, self.color, (self.x, self.y), Globals.RADIUS_OF_PERSON
        )

        if self.masked:
            pygame.draw.rect(
                screen,
                Globals.WHITE,
                (
                    self.x,
                    self.y,
                    Globals.RADIUS_OF_PERSON,
                    Globals.RADIUS_OF_PERSON / 2.5,
                ),
            )

    def getColorByStatus(self):
        match self.status:
            case InfectionStatus.Susceptible:
                return Globals.BLUE
            case InfectionStatus.Immune:
                return Globals.GREEN
            case InfectionStatus.Infected:
                return Globals.RED
            case InfectionStatus.Deceased:
                return Globals.YELLOW
            case _:
                raise Exception("getColorByStatus: Unknown Status!!!!!!!")

    # the following code is for debugging
    # def __del__(self):
    #     print(f"Instance {self.x},{self.y} is being deleted.")
