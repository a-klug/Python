import pandas as pd

# Load the data
print("Reading in the Haul Route")
path = r"C:\Users\AsherKlug\OneDrive - BSC Holdings\(RI.1753) - Work\Data\Beneficiated Data\Opt 1 - Haul String IOB002_720_P57_39.csv"

df = pd.read_csv(path)

name = path.split("\\")[-1].split(".")[0].split(" ")[-1]

# Process the data
# Data is in the format (XP, YP, ZP)

# Add a numeric index as a column
df["Index"] = df.index

# For each point, calculate the gradient and distance to the next point

route = pd.DataFrame(
    columns=["From Location", "To Location", "Gradient", "Distance",
             "Start Coordinates", "End Coordinates"])

ind = 0
print("Iterating over the points...")
while ind < len(df)-1:
    print("Progress: " + str(ind/len(df)*100))
    # Make sure we are not at the end of the dataframe
    start = df.iloc[ind]
    end = df.iloc[ind+1]
    # Create a string of the coordinates
    start_coords = f"({start['XP']}, {start['YP']}, {start['ZP']})"
    end_coords = f"({end['XP']}, {end['YP']}, {end['ZP']})"

    # Distance
    distance = ((end['XP'] - start['XP'])**2 +
                (end['YP'] - start['YP'])**2 +
                (end['ZP'] - start['ZP'])**2)**0.5

    # Check if the distance is zero. If it is, we can skip this point
    if distance == 0:
        ind += 1
        continue

        # Gradient - z-rise over xy-run
        # Make sure we are not dividing by zero
    gradient = (end['ZP'] - start['ZP']) / distance

    # Ensure that the coordinates are saved as strings
    route = pd.concat(
        [
            route,
            pd.DataFrame({
                "From Location": [name + f"_{start['Index']}"],
                "To Location": [name + f"_{end['Index']}"],
                "Gradient": [gradient],
                "Distance": [distance],
                "Start Coordinates": [str(start_coords)],
                "End Coordinates": [str(end_coords)]
            })
        ]
    )
    ind += 1

route.reset_index(inplace=True)
# Ensure that the points connect
for ind, row in route.iterrows():
    if ind > 0:
        prev_row = route.loc[ind-1]
        if prev_row["To Location"] != row["From Location"]:
            route.at[ind, "From Location"] = prev_row["To Location"]
            print("Route updated for continuity")
    if ind == len(route):
        route.at[ind, "To Location"] = "Dump"


# Save the data
route.to_excel("route.xlsx", index=False)


# Process the route data to concatenate multiple route segments
concat_route = route.copy().reset_index()
concat_route["Combine"] = ''
last_row = None
combiner = 1
for ind, row in concat_route.iterrows():
    if ind < len(concat_route) and last_row is not None:
        if row["Gradient"] == 0:
            combiner += 1 if last_row["Gradient"] != 0 else 0
        else:
            combiner += 1
    last_row = row
    concat_route.at[ind, "Combine"] = combiner

# Combine those rows
concat_route = concat_route.groupby("Combine").aggregate({
    "From Location": "first",
    "To Location": "last",
    "Gradient": "sum",
    "Distance": "sum",
    "Start Coordinates": "first",
    "End Coordinates": "last"
})

concat_route.to_excel("final_route.xlsx", index=False)
