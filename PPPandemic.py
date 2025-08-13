import pygame
import random
import math
import os
from Globals import Globals
from InfectionStatus import InfectionStatus
from filehelpers import create_trial_data_line, append_trial_data_to_dataset
from Person import Person
from displayHelpers import initializePygame, displayLegend


def simulate_pandemic(show_visuals: bool):
    if show_visuals:
        screen = initializePygame()

        # Screen Definitions
        pygame.display.set_caption(
            "Measles in Motion: A Digital Epidemic Simulation by Abigail Lightle"
        )

    seed = 0
    running = True
    userQuit = False
    dataForAllTrials: list[str] = []
    for _ in range(Globals.NUMBER_OF_TRIALS):
        seed += 1
        random.seed(seed)

        # Trial Data
        status = []

        (people, locations) = initializePopulation()

        # Infect one random person
        people[random.randint(0, Globals.POPULATION - 1)].status = (
            InfectionStatus.Infected
        )

        # START: Main loop ----------------------------------------------------------------------------------------------------
        if show_visuals:
            clock = pygame.time.Clock()

        number_of_frames = 0
        days = 0
        total_infections = 1

        while running:
            number_of_frames += 1

            if show_visuals:
                screen.fill(Globals.GRAY)

                if len(pygame.event.get(pygame.QUIT)) > 0:
                    userQuit = True
                    break

            # Total number of infections
            total_infections += check_if_infected(people)

            status = [0, 0, 0, 0, 0]
            # check person status and MOVE & DRAW each person
            for person in people:
                status[person.status.value] += 1
                person.move(locations)
                if show_visuals:
                    person.draw(screen)

            if status[InfectionStatus.Infected.value] <= 0:
                break

            if show_visuals:
                pygame.display.set_caption(
                    f"Measles in Motion: A Digital Epidemic Simulation by Abigail Lightle\t(FPS: {int(clock.get_fps()+1)})\t(Frames: {number_of_frames})\t(Population: {Globals.POPULATION})\t(Seed: {seed} of {Globals.NUMBER_OF_TRIALS})\t(Vaccinated: {int(Globals.VACCINATED_PERCENT*100)}%)"
                )
                displayLegend(screen, status, total_infections)
                pygame.display.flip()
                clock.tick(Globals.FRAME_RATE)

            days += 1

        # END: Main loop -----------------------------------------------------------------------------------------------------
        if userQuit:
            break
        # Append This Trial to Dataset for Future Data Science Analysis
        #
        trial_data = create_trial_data_line(
            status, total_infections, number_of_frames, seed
        )
        dataForAllTrials.append(trial_data)

    if show_visuals:
        pygame.quit()

    append_trial_data_to_dataset(dataForAllTrials)
    return userQuit


def initializePopulation():
    people = []
    locations: dict[(int,int), list[Person]] = {}

    vaxers = makeUniformRandomDistribution(
        InfectionStatus.Susceptible, InfectionStatus.Immune, Globals.VACCINATED_PERCENT
    )
    maskers = makeUniformRandomDistribution(False, True, Globals.MASK_RATE)

    for index in range(Globals.POPULATION):
        x = random.randint(
            Globals.RADIUS_OF_PERSON, Globals.WIDTH - Globals.RADIUS_OF_PERSON
        )
        y = random.randint(
            Globals.RADIUS_OF_PERSON, Globals.HEIGHT - Globals.RADIUS_OF_PERSON
        )

        person = Person(x, y, maskers[index], True, status=vaxers[index])
        people.append(person)
        
        # if (x,y) in locations:
        #     locations[(x,y)].append(person)
        # else:
        #     locations[(x,y)] = [person]

    return (people, locations)


def makeUniformRandomDistribution(
    initial_trait, alternative_trait, trait_percentage: float
):
    # Create a list of all people as initial_trait
    distribution = [initial_trait] * Globals.POPULATION
    # Calculate the number of people to receive alternative_trait
    numberOfPickedPeople = int(Globals.POPULATION * trait_percentage)
    # Set the first N people in the list to alternative_trait status
    distribution[0 : numberOfPickedPeople - 1] = [
        alternative_trait
    ] * numberOfPickedPeople
    # Shuffle the list so alternative people are randomly distributed
    random.shuffle(distribution)
    return distribution


def check_if_infected(people: list[Person]):
    # Total number of infections
    total_infections = 0
    for person in people:
        if person.status == InfectionStatus.Infected:
            person.infection_days += 1

            # If infected for long enough, introduce a probability of death
            if (
                person.infection_days >= Globals.DAYS_TO_DEATH
                and random.random() < Globals.DEATH_PROBABILITY
            ):
                person.status = InfectionStatus.Deceased
            elif person.infection_days >= Globals.DAYS_TO_RECOVERY:
                person.status = InfectionStatus.Immune

            # ASK: Why do we not check if the other is the same person?
            for other in people:
                if (
                    other.status == InfectionStatus.Deceased
                    or other.status == InfectionStatus.Infected
                ):
                    continue

                dist = math.hypot(person.x - other.x, person.y - other.y)
                if dist > Globals.INFECTION_RADIUS:
                    continue

                will_be_infected = random.random() < calculate_infection_chance(
                    person, other, dist
                )
                if will_be_infected and (
                    other.status == InfectionStatus.Susceptible
                    or other.status == InfectionStatus.Immune
                ):
                    other.status = InfectionStatus.Infected
                    total_infections += 1

    return total_infections


def calculate_infection_chance(
    infected_person: Person, potential_victim: Person, distance: float
) -> float:
    if infected_person.masked and potential_victim.masked:
        (upper_bound, lower_bound) = Globals.BOTH_WITH_MASK_PROBABILITY_MODIFIERS
    elif infected_person.masked and not potential_victim.masked:
        (upper_bound, lower_bound) = Globals.INFECTED_WITH_MASK_PROBABILITY_DISTANCE_MODIFIERS
    elif not infected_person.masked and potential_victim.masked:
        (upper_bound, lower_bound) = Globals.SUSCEPTIBLE_WITH_MASK_PROBABILITY_MODIFIERS
    elif not infected_person.masked and not potential_victim.masked:
        (upper_bound, lower_bound) = Globals.NONE_WITH_MASK_PROBABILITY_DISTANCE_MODIFIERS

    distance_based_infection_chance = lerp(
        lower_bound, upper_bound, distance / Globals.INFECTION_RADIUS
    )

    if potential_victim.status == InfectionStatus.Immune:
        base_infection_chance = Globals.VACCINE_EFFECTIVENESS
    else:
        base_infection_chance = Globals.INFECTION_PROBABILITY        

    return base_infection_chance - distance_based_infection_chance


def lerp(lower_bound: float, upper_bound: float, interpolation_factor: float) -> float:
    return lower_bound + interpolation_factor * (upper_bound - lower_bound)


# Things to do:
# - Social Distance
# - Add ability to run all variations at once
