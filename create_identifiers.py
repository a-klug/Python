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

# Add the bases cases
scenarios = itertools.product(
    ['DIESEL'],
    truck_fleets,
    haul_routes,
)

scenario_ids += ['-'.join(scenario) for scenario in scenarios]

# Create a datafile with all scenario identifiers
df = pd.DataFrame(scenario_ids, columns=['scenario_id'])

headings = ['Battery', 'Trolley System', 'Trolley Segment', 'Recharge Level',
            'Truck Fleet', 'Truck Type', 'Haul Route', 'Charging Method',
            'Charging Bays']

for heading in headings:
    df[heading] = ''

# Break up the identifiers into their components and add them to the DataFrame
for ind, row in df.iterrows():
    config = row['scenario_id'].split('-')
    if config[0] == 'DIESEL':
        break
    for head_ind, heading in enumerate(headings):
        print(heading)
        df.at[ind, heading] = config[head_ind]

df.to_excel('scenario_identifiers.xlsx', index=False)
