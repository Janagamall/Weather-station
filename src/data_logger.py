import csv
import time

LOG_FILE = "weather_data.csv"

def log_data(temperature, humidity):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity])
