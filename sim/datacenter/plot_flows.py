import re
import matplotlib.pyplot as plt
import seaborn as sns
import sys

BIG_SIZE = 12
FIGRATIO = 3 / 4
FIGWIDTH = 3.335 # inches
FIGHEIGHT = FIGWIDTH * FIGRATIO
FIGSIZE = (FIGWIDTH, FIGHEIGHT)

plt.rcParams.update(
{
"figure.figsize": FIGSIZE,
"figure.dpi": 300,
}
)

COLORS = sns.color_palette("Paired")
sns.set_style("ticks")
sns.set_palette(COLORS)

plt.rc("font", size=BIG_SIZE) # controls default text sizes
plt.rc("axes", titlesize=BIG_SIZE) # fontsize of the axes title
plt.rc("axes", labelsize=BIG_SIZE) # fontsize of the x and y labels
plt.rc("xtick", labelsize=BIG_SIZE) # fontsize of the tick labels
plt.rc("ytick", labelsize=BIG_SIZE) # fontsize of the tick labels
plt.rc("legend", fontsize=BIG_SIZE) # legend fontsize
plt.rc("figure", titlesize=BIG_SIZE) # fontsize of the figure title

alg = sys.argv[1]
# File containing the flow data
input_file = f"{alg}.out"

# Regular expression to parse the lines
# Flow ndp_431_730 flow_id 8 finished at 492.108 total bytes 2000000
# Flow Roce_510_486 24357 finished at 1047.01 total bytes 2000000
pattern = re.compile(r"Flow (.*) finished at ([\d.]+) total bytes (\d+)")

# Lists to store extracted data
flows = []
times = []

# Read and parse the file
with open(input_file, "r") as file:
    for line in file:
        match = pattern.match(line)
        if match:
            flow_id = match.group(1)  # Extract flow identifier
            finish_time = float(match.group(2))  # Extract finish time
            flows.append(flow_id)
            times.append(finish_time)

# print(finish_time)
# Sort data by time for better visualization
sorted_indices = sorted(range(len(times)), key=lambda i: times[i])
flows = [i for i, _ in enumerate(sorted_indices)]
times = [times[i] for i in sorted_indices]

# Plot the arrival times of different flows
plt.scatter(times, flows, marker='o', color='b', label="Flow Completion")
plt.xlabel("Finish time (seconds)")
plt.ylabel("Flow ID")
plt.tight_layout()
# Show the plot
plt.savefig(f"flow_{alg}.pdf")
print(f"Flow plot saved to flow_{alg}.pdf")