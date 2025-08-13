class Globals:
    """
    This class is used to store global variables for the PairProgram application.
    It is designed to be a singleton, ensuring that only one instance exists throughout the application.
    """

    NUMBER_OF_TRIALS = 10
    WIDTH = 1024
    HEIGHT = 768
    LEGEND = 64

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    """Immune"""
    RED = (200, 0, 0)
    """Infected"""
    BLUE = (0, 0, 200)
    """Susceptible"""
    YELLOW = (255, 255, 0)
    """Deceased"""
    GRAY = (100, 100, 100)
    """Background"""
    LIGHT_MAGENTA = (224, 0, 224)
    """Legend"""

    # Measles Herd Immunity Simulation Parameters
    POPULATION = 1000
    """Total number of people in the simulation"""

    INFECTION_RADIUS = 5
    """Distance within which an infected person can spread the infection"""

    INFECTION_PROBABILITY = 0.97
    """Represents the chance of spreading the infection when an infected person is near a susceptible person"""

    VACCINATED_PERCENT = 0.95
    """Proportion of the population that starts as immune (vaccinated)"""

    VACCINE_EFFECTIVENESS = 0.97
    """Vaccine effectiveness"""

    HERD_IMMUNITY_THRESHOLD = 0.93
    """The percentage of immune people needed to stop uncontrolled spread (NOT USED)"""

    DEATH_PROBABILITY = 0.02
    """Probability an infected person dies"""

    DAYS_TO_DEATH = 10
    """Minimum number of days an infected person must be sick before they have a chance to die"""

    DAYS_TO_DEATH_MULTIPLIER = 10
    """Frame/Day multiplier"""

    DAYS_TO_RECOVERY = 80
    """Number of days it takes to recover"""

    RADIUS_OF_PERSON = 5
    """Radius of each person in the simulation"""

    FRAME_RATE = 1000
    """use 10-60 to demo program and 1000 to run full speed"""

    MASK_RATE: float = 0.50
    """percent of people wearing masks"""

    NONE_WITH_MASK_PROBABILITY_DISTANCE_MODIFIERS: list[float] = [1.00, 0.03]

    INFECTED_WITH_MASK_PROBABILITY_DISTANCE_MODIFIERS: list[float] = [0.006, 0.005]

    SUSCEPTIBLE_WITH_MASK_PROBABILITY_MODIFIERS: list[float] = [0.38, 0.013]

    BOTH_WITH_MASK_PROBABILITY_MODIFIERS: list[float] = [0.005, 0.005]

    SOCIAL_DISTANCE = 5
