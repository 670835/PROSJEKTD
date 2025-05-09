import logging
import threading
import time
import requests

from messaging import ActuatorState
import common


class Actuator:
    def __init__(self, did):
        self.did = did
        self.state = ActuatorState(did, False)  # default: off

    def simulator(self):
        logging.info(f"Actuator {self.did} starting")

        while True:
            # Her kunne vi simulert faktisk virkning, men vi logger bare
            logging.info(f"Actuator {self.did}: {self.state.state}")
            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):
        logging.info(f"Actuator Client {self.did} starting")

        url = f"{common.BASE_URL}smarthouse/actuator/{self.did}/current"

        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    self.state = ActuatorState.from_dict(data)
                else:
                    logging.warning(f"Feil ved henting: {response.status_code} - {response.text}")
            except Exception as e:
                logging.error(f"Exception ved henting: {e}")

            time.sleep(common.LIGHTBULB_CLIENT_SLEEP_TIME)

    def run(self):
        simulator_thread = threading.Thread(target=self.simulator, daemon=True)
        simulator_thread.start()

        client_thread = threading.Thread(target=self.client, daemon=True)
        client_thread.start()



