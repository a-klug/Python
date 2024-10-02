import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Load the data
path = r"C:\Users\AsherKlug\OneDrive - BSC Holdings\(RI.1753) - Work\Data\Beneficiated Data\Opt 1 - Haul String IOB002_720_P57_39.csv"
df = pd.read_csv(path)

# Define special coordinates for red plotting
# Replace with actual special coordinates
special_coords = [(667787.518, 7906501.032, 693.321)]

# Separate special coordinates into two lists
special_xx = [y for (x, y, z) in special_coords]
special_yy = [z for (x, y, z) in special_coords]
special_coords_2d = list(zip(special_xx, special_yy))

# Initialize plots
fig, ax = plt.subplots()
normal_x = []
normal_y = []
special_x = []
special_y = []

# Plot initial empty scatter
sc1 = ax.scatter([], [], color='blue', label='Normal')
sc2 = ax.scatter([], [], color='red', label='Special')
ax.set_xlim(df["YP"].min(), df["YP"].max())
ax.set_ylim(df["ZP"].min(), df["ZP"].max())
ax.set_xlabel("YP")
ax.set_ylabel("ZP")
ax.set_title("YP vs ZP")
ax.legend()

# Function to update the scatter plot


def update(i):
    yp = df.iloc[i]["YP"]
    zp = df.iloc[i]["ZP"]

    if (yp, zp) in special_coords_2d:
        special_x.append(yp)
        special_y.append(zp)

    else:
        normal_x.append(yp)
        normal_y.append(zp)

    if normal_x and normal_y:
        sc1.set_offsets(list(zip(normal_x, normal_y)))
    if special_x and special_y:
        sc2.set_offsets(list(zip(special_x, special_y)))
    return sc1, sc2


# Run the animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100)
plt.show()
