# Read in a CSV file to a pandas DataFrame and then, row by row, plot and
# update a scatter plot of the data. This is a great way to visualise data as
# it is being processed.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the data
path = r"C:\Users\AsherKlug\OneDrive - BSC Holdings\(RI.1753) - Work\Data\Beneficiated Data\Opt 2 - Haul String IOB003_855_P62_35.csv"

df = pd.read_csv(path)

# Iterate through the data
# Plot the YP vs ZP data for each row
fig, ax = plt.subplots()
x = []
y = []
sc = ax.scatter(x, y)
ax.set_xlim(df["YP"].min(), df["YP"].max())
ax.set_ylim(df["ZP"].min(), df["ZP"].max())
ax.set_xlabel("YP")
ax.set_ylabel("ZP")
ax.set_title("YP vs ZP")


def update(i):
    x.append(df.iloc[i]["YP"])
    y.append(df.iloc[i]["ZP"])
    sc.set_offsets(list(zip(x, y)))
    return sc


ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100)
plt.show()
