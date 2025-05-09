import logging
import threading
import time
import math
import requests

from messaging import SensorMeasurement
import common


class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')

    def simulator(self):
        logging.info(f"Sensor {self.did} starting")

        while True:
            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)
            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):
        logging.info(f"Sensor Client {self.did} starting")

        url = f"{common.BASE_URL}smarthouse/sensor/{self.did}/current"

        while True:
            try:
                response = requests.post(url, json={
                    "uuid": self.did,
                    "value": self.measurement.value,
                    "timestamp": self.measurement.timestamp,
                    "unit": self.measurement.unit
                })

                if response.status_code == 201:
                    logging.info(f"Temperatur sendt: {self.measurement.value}")
                else:
                    logging.warning(f"Feil ved sending: {response.status_code} - {response.text}")

            except Exception as e:
                logging.error(f"Exception ved sending: {e}")

            time.sleep(common.TEMPERATURE_SENSOR_CLIENT_SLEEP_TIME)

    def run(self):
        # Start tråd som simulerer fysisk sensor
        simulator_thread = threading.Thread(target=self.simulator, daemon=True)
        simulator_thread.start()

        # Start tråd som sender data til sky-tjenesten
        client_thread = threading.Thread(target=self.client, daemon=True)
        client_thread.start()

