import pandas as pd
import matplotlib.pyplot as plt
import os
folder = os.path.dirname(os.path.abspath(__file__))


# reading csv data with pandas lib
local_data = pd.read_csv(folder+"/local_temp.csv") # Egypt
global_data = pd.read_csv(folder+"/global_temp.csv")


# moving average col with a window of 5 and fill nan with the average value
local_data["moving_avg"] =  local_data["avg_temp"].rolling(10).mean().fillna(local_data["avg_temp"].mean())
global_data["moving_avg"] = global_data["avg_temp"].rolling(10).mean().fillna(global_data["avg_temp"].mean())

# visualization
plt.rc('font', size=12)
fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(local_data["year"], local_data["moving_avg"], color='blue', label='Alexandria, Egypt')
ax.plot(global_data["year"], global_data["moving_avg"], color='red', label='Global')

ax.set_xlabel('Time (Year)')
ax.set_ylabel('Tempreture (Celsius)')
ax.set_title('Global vs. Alexandria, Egypt Tempreture')
ax.grid(True)
ax.legend(loc='upper left');

plt.figtext(0.5, 0.01, "Line Chart of (10-year Moving Average)", ha="center", fontsize=18)


# statistical observations
local_std = round(local_data["moving_avg"].std(),3)
global_std = round(global_data["moving_avg"].std(),3)

local_mean = round(local_data["moving_avg"].mean(),3)
global_mean = round(global_data["moving_avg"].mean(),3)




