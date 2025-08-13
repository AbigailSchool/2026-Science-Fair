from Globals import Globals
from InfectionStatus import InfectionStatus
import os

def create_trial_data_line(
    status: list[int], total_infections: int, number_of_frames: int, seed: int
) -> str:
    trial01 = f"{Globals.FRAME_RATE: g},{Globals.RADIUS_OF_PERSON: g},{Globals.DAYS_TO_RECOVERY: g}"
    trial02 = f"{Globals.DAYS_TO_DEATH_MULTIPLIER: g},{Globals.DAYS_TO_DEATH: g},{Globals.DEATH_PROBABILITY: g}"
    trial03 = f"{Globals.HERD_IMMUNITY_THRESHOLD: g},{Globals.VACCINATED_PERCENT: g},{Globals.INFECTION_PROBABILITY: g}"
    trial04 = f"{Globals.INFECTION_RADIUS: g},{Globals.POPULATION: g},{total_infections: g},{status[InfectionStatus.Infected.value]: g}"
    trial05 = f"{status[InfectionStatus.Immune.value]: g},{status[InfectionStatus.Susceptible.value]: g},{status[InfectionStatus.Deceased.value]: g},{number_of_frames: g}, {seed: g}"
    return f"{trial01},{trial02},{trial03},{trial04},{trial05}"

def append_trial_data_to_dataset(data: list[str]):
    # Append the trial data to the dataset
    dataset_file = "measles_dataset.csv"

    is_a_new_file = not os.path.exists(dataset_file)
    with open(dataset_file, "a") as file:
        if is_a_new_file:
            file.write(
                "fps,p_rad,days_r,dm,d_t_d,d_prob,h_i_t,vac_p,inf_p,i_rad,pop,t_inf,n_inf,imm,sus,dec,frames, seed\n"
            )
        for line in data:
            file.write(line + "\n")


