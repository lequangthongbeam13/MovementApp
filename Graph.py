import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
def ShowGraph():
    temperature_values = [48.7, 50.2, 49.3, 47.8, 46.5]
    movement_values = [1, 0, 1, 0, 1]  # 1: YES, 0: NO
    timestamps = [
        "2024-09-30 08:29:32",
        "2024-09-30 08:34:32",
        "2024-09-30 08:39:32",
        "2024-09-30 08:44:32",
        "2024-09-30 08:49:32"
    ]

    # object datetime
    time_data = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in timestamps]

    #create graph
    fig, ax1 = plt.subplots()

    # Temp
    ax1.plot(time_data, temperature_values, label="Temperature (°C)", color="tab:red")
    ax1.set_ylabel("Temperature (°C)", color="tab:red")
    ax1.tick_params(axis="y", labelcolor="tab:red")

    # movement
    ax2 = ax1.twinx()  #  second y
    ax2.plot(time_data, movement_values, label="Movement", color="tab:blue", linestyle="--")
    ax2.set_ylabel("Movement (1: Detected, 0: Not Detected)", color="tab:blue")
    ax2.tick_params(axis="y", labelcolor="tab:blue")

    # x (time)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S")) 
    ax1.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))  
    plt.gcf().autofmt_xdate()  

    
    plt.title("Temperature and Movement over Time")
    fig.tight_layout()  
    plt.show()

ShowGraph()