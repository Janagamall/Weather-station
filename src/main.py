import time
from sensor import get_sensor_data
from display import update_display
from data_logger import log_data

UPDATE_INTERVAL = 2  # Seconds

while True:
    temperature, humidity = get_sensor_data()
    if temperature is not None and humidity is not None:
        update_display(temperature, humidity)
        log_data(temperature, humidity)
    time.sleep(UPDATE_INTERVAL)
