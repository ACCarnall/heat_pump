import numpy as np
import matplotlib.pyplot as plt


def model(x, m, c):
    return m*x + c


data = np.loadtxt("data.txt", usecols=(6, 4, 5))
fig = plt.figure(figsize=(8, 7))
ax = plt.subplot()

ax.scatter(data[:, 2], data[:, 0])
ax.scatter(data[-1:, 2], data[-1:, 0], color="red")

m = -(20 - np.nanmean(data[:, 0]))/np.nanmean(data[:, 2])
c = 20

x = np.arange(0, 51)
y = np.arange(-5, 21)

plt.plot(+0.1*24*20-0.1*24*y, y, color='green', label="100W per degree below 20$^\circ$C")
plt.plot(+0.2*24*20-0.2*24*y, y, color='red', label="200W per degree below 20$^\circ$C")
#plt.plot(x, m*x + c, color='blue', label="Best fit: " + str(round(-1000/m/24, 1)) + "W per degree")

ax.set_xlim(0, 70)
ax.set_ylim(-0, 22)

plt.legend(frameon=False, title="Heat loss from house")
plt.xlabel("Daily energy output from heat pump / kWh")
plt.ylabel("Mean daily outdoor temperature / $^\circ$C")
#plt.show()
plt.savefig("heat_pump_output.png", bbox_inches='tight', dpi=300)

data = np.loadtxt("data.txt", usecols=(3, 4, 5))
fig = plt.figure(figsize=(8, 6))
ax = plt.subplot()
print(data[:, 1])
ax.scatter(data[:, 0], data[:, 2]/data[:, 1])
ax.scatter(data[-1:, 0], data[-1:, 2]/data[-1:, 1], color="red")
ax.set_xlabel("Mean daily temperature for running heat pump/ $^\circ$C")
ax.set_ylabel("Heat pump daily coefficient of performance")

m = 0.1
c = 3.8

x = np.arange(-5, 21)
plt.plot(x, m*x + c, color='red')
ax.axvline(x=7.5, color='black', ls="--")
#ax.axhline(x=7, color='black', ls="--")
plt.savefig("heat_pump_performance.png", bbox_inches='tight', dpi=300)


# Annual consumption
average_temp = 7.5  # Average annual outdoor temperature
scop = 4.4
heat_loss_per_deg = 200  # Watts
electricity_cost = 0.16  # pence per kWh

print("Total annual heat loss", (20-average_temp)*heat_loss_per_deg*24*365/1000)
print("Total annual heating energy input", (20-average_temp)*heat_loss_per_deg*24*365/1000/scop)
print("Total annual heating electricity cost", electricity_cost*(20-average_temp)*heat_loss_per_deg*24*365/1000/scop)