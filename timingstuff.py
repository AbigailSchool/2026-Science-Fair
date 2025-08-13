# import cProfile
# import pstats
from PPPandemic import simulate_pandemic
from Globals import Globals

# profiler = cProfile.Profile()
# profiler.enable()
quit = False
for mask_rate in range(10, 101, 10):
    if quit:
        break
    Globals.MASK_RATE = mask_rate / 100
    for vaccinated_percent in range(10, 101, 10):
        if quit:
            break
        Globals.VACCINATED_PERCENT = vaccinated_percent / 100

        quit = simulate_pandemic(True)
        print(f"Simulation Mask_Rate:  {mask_rate}, Vaccination_Percentage: {vaccinated_percent} complete!")
print("done!")

# profiler.disable()

# stats = pstats.Stats(profiler)
# stats.sort_stats('tottime')

# stats.print_stats(15)
