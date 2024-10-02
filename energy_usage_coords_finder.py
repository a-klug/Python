import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Load the data
path = r"C:\Users\AsherKlug\OneDrive - BSC Holdings\(RI.1753) - Work\Data\Beneficiated Data\Opt 1 - Haul String IOB002_720_P57_39.csv"

data = pd.read_csv(path)

# Ensure the CSV has the columns: 'XP', 'YP', 'ZP'
if not all(col in data.columns for col in ['XP', 'YP', 'ZP']):
    raise ValueError("CSV must contain 'XP', 'YP', and 'ZP' columns")

# Specify the coordinates of the special points
# Example format: [(xp1, yp1, zp1), (xp2, yp2, zp2), ...]
special_points_coords = [(667250.005, 7906577.356, 729.147)]

# Filter special points
special_points = data[data.apply(lambda row: (
    row['XP'], row['YP'], row['ZP']) in special_points_coords, axis=1)]
regular_points = data[~data.apply(lambda row: (
    row['XP'], row['YP'], row['ZP']) in special_points_coords, axis=1)]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to update the scatter plot


def update(num, data, scat_regular, scat_special):
    if num < len(regular_points):
        row = regular_points.iloc[num]
        scat_regular._offsets3d = (list(scat_regular._offsets3d[0]) + [row['XP']],
                                   list(
                                       scat_regular._offsets3d[1]) + [row['YP']],
                                   list(
                                       scat_regular._offsets3d[2]) + [row['ZP']],
                                   )
    if num < len(special_points):
        row = special_points.iloc[num]
        scat_special._offsets3d = (list(scat_special._offsets3d[0]) + [row['XP']],
                                   list(
                                       scat_special._offsets3d[1]) + [row['YP']],
                                   list(scat_special._offsets3d[2]) + [row['ZP']])


# Initialize the scatter plots
scat_regular = ax.scatter([], [], [], c='b', label='Regular Points')
scat_special = ax.scatter([], [], [], c='r', label='Special Points')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(max(len(regular_points), len(special_points))),
                    fargs=(data, scat_regular, scat_special), interval=500, blit=False, repeat=False)

# Labels
ax.set_xlabel('XP')
ax.set_ylabel('YP')
ax.set_zlabel('ZP')

# Legend
ax.legend()

# Display the animation
plt.show()
