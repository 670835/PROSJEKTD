import time
import logging

from smarthouse_lightbulb import Actuator
from smarthouse_temperature_sensor import Sensor
import common

# Konfigurer logging med tid og melding
logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

if __name__ == "__main__":
    # Lag instanser
    actuator = Actuator(common.LIGHTBULB_DID)
    sensor = Sensor(common.TEMPERATURE_SENSOR_DID)

    # Start tråder
    actuator.run()
    sensor.run()

    # Hold programmet i gang
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Avslutter smarthouse.")