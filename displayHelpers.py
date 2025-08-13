from Globals import Globals
import Person
from InfectionStatus import InfectionStatus
import pygame


topOfLegend = Globals.HEIGHT + (Globals.LEGEND // 2)


def displayLegend(screen, status, total_infections):

    # Display legend
    pygame.draw.rect(
        screen,
        Globals.LIGHT_MAGENTA,
        (0, topOfLegend, Globals.WIDTH, Globals.LEGEND // 2),
    )

    pos_x = 0
    # pygame.draw.circle(screen, Globals.RED, (pos_x, Globals.HEIGHT + LEGION//2 + 17), 5)
    screen.blit(
        legend_font.render(
            f"Total Infections: {total_infections:04d}", True, Globals.BLACK
        ),
        (pos_x + 10, topOfLegend + 8),
    )

    pos_x = 280
    pygame.draw.circle(screen, Globals.RED, (pos_x, topOfLegend + 17), 5)
    screen.blit(
        legend_font.render(
            f"Infected: {status[InfectionStatus.Infected.value]:04d}",
            True,
            Globals.BLACK,
        ),
        (pos_x + 10, topOfLegend + 8),
    )

    pos_x += 180
    pygame.draw.circle(screen, Globals.GREEN, (pos_x, topOfLegend + 17), 5)
    screen.blit(
        legend_font.render(
            f"Immune: {status[InfectionStatus.Immune.value]:04d}", True, Globals.BLACK
        ),
        (pos_x + 10, topOfLegend + 8),
    )

    pos_x += 175
    pygame.draw.circle(screen, Globals.BLUE, (pos_x, topOfLegend + 17), 5)
    screen.blit(
        legend_font.render(
            f"Susceptible: {status[InfectionStatus.Susceptible.value]:04d}",
            True,
            Globals.BLACK,
        ),
        (pos_x + 10, topOfLegend + 8),
    )

    pos_x += 220
    pygame.draw.circle(screen, Globals.YELLOW, (pos_x, topOfLegend + 17), 5)
    screen.blit(
        legend_font.render(
            f"Deceased: {status[InfectionStatus.Deceased.value]:04d}",
            True,
            Globals.BLACK,
        ),
        (pos_x + 10, topOfLegend + 8),
    )


def initializePygame():
    pygame.init()

    global legend_font
    legend_font = pygame.font.SysFont(None, 30)

    # Screen Definitions
    pygame.display.set_caption(
        "Measles in Motion: A Digital Epidemic Simulation by Abigail Lightle"
    )

    return pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT + Globals.LEGEND))
