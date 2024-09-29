import itertools
import pandas as pd

battery_types = ['LT1', 'LT3']  # LTO 1C, LTO 3C
# panto, advanced trolley pole, side mount
trolley_systems = ['PTG', 'ATP', 'SM']
trolley_segments = ['TS1', 'TS2', 'TS3']  # up to three segments
recharge_levels = ['REC1', 'REC2', 'REC3']  # recharge level 1, 2, 3
truck_fleets = ['TF1', 'TF2']  # two fleets
truck_types = ['HYB', 'BET']  # hybrid, battery electric
haul_routes = ['MR', 'SN']  # Minas Rio, Sishen
charging_choices = ['SCM1', 'SCM2']  # static, swap
charging_bays = ['CB1', 'CB2', 'CB3']  # up to three bays

# Create unique combinations of all parameters
scenarios = itertools.product(
    battery_types,
    trolley_systems,
    trolley_segments,
    recharge_levels,
    truck_fleets,
    truck_types,
    haul_routes,
    charging_choices,
    charging_bays
)

# Generate unique scenario identifiers
scenario_ids = ['-'.join(scenario) for scenario in scenarios]

# Create a datafile with all scenario identifiers
df = pd.DataFrame(scenario_ids, columns=['scenario_id'])

print(len(df))
