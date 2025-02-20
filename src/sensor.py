import Adafruit_DHT

SENSOR_TYPE = Adafruit_DHT.DHT22
SENSOR_PIN = 4  # GPIO pin

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 1), round(humidity, 1)
    return None, None
