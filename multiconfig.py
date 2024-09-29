import pandas as pd

# Create the DataFrame

df = pd.DataFrame(columns=["Config", "Sheet", "Match Col 1",
                  "Match Val 1", "Sub Col 1", "Sub Val 1", "Number of Runs"])

scenario_identifiers = pd.read_excel('scenario_identifiers.xlsx')

headings = scenario_identifiers.columns

sheets = {
    "Battery": "Battery",
    "Trolley System": "Trolley System",
    "Trolley Segment": "Trolley Segment",
    "Recharge Level": "Recharge Level",
    "Truck Type": "Truck Variant",
    "Charging Method": "Charging Method",
    "Charging Bays": "Charging Bays"
}

matches = {
    "Battery": "Battery",
    "Trolley System": "Trolley System",
    "Trolley Segment": "Trolley Segment",
    "Recharge Level": "Recharge Level",
    "Truck Type": "Truck Type",
    "Charging Method": "Charging Method",
    "Charging Bays": "Charging Bays"
}

subs = {
    "Battery": "Battery",
    "Trolley System": "Trolley System",
    "Trolley Segment": "Trolley Segment",
    "Recharge Level": "Recharge Level",
    "Truck Type": "Truck Type",
    "Charging Method": "Charging Method",
    "Charging Bays": "Charging Bays"
}

for ind, row in scenario_identifiers.iterrows():
    config = row['scenario_id']
    categories =
