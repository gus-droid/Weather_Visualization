import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Set Our Plot Background To Black
style.use("dark_background")

# Initalize Our Data
days_in_year = np.arange(1, 366)
mean_temp = 68
std_dev = 9
temperature_data = np.random.normal(mean_temp, std_dev, days_in_year.size)
seasonality = 9 * np.sin(2 * np.pi * days_in_year / 365)
temperature_data += seasonality

# print(temperature_data)

# Anyalyze Our Data
mean = np.mean(temperature_data) # mean of our tempeature
max = np.max(temperature_data) # max temperature
min = np.min(temperature_data) #min temperature
median = np.median(temperature_data) # median temperature
s_dev = np.std(temperature_data) # standard devition temperature

hottest_day = np.argmax(temperature_data) + 1 #argmax returns index of max value in array
coldest_day = np.argmin(temperature_data) + 1 #returns index of min value in array

# Visualize Our Data

fig, axs = plt.subplots(2, figsize = (6, 6)) # 2 rows

axs[0].plot(days_in_year, temperature_data)
axs[0].set_xlabel("Days Of The Year")
axs[0].set_ylabel("Temperature (°F)")
axs[0].set_title("Temperature Over The Year")
axs[0].grid(True, linestyle = '--', alpha = 0.7)

axs[1].hist(temperature_data)
axs[1].set_xlabel("Temperature (°F)")
axs[1].set_ylabel("Count of Days")
axs[1].set_title("Temperature Distribution Over The Year")
axs[1].grid(True, linestyle = '--', alpha = 0.7)

plt.tight_layout(rect=[0, 0, 1, 0.96]) # left, bottom, right, top
fig.suptitle("Line Graph & Histogram of Temperature vs Days of The Year")
plt.show()
