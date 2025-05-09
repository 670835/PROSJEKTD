import json
import datetime


class SensorMeasurement:

    def __init__(self, init_value):
        self.timestamp = str(datetime.datetime.now().isoformat())
        self.value = init_value
        self.unit = "°C"

    def set_temperature(self, new_value):
        self.timestamp = str(datetime.datetime.now().isoformat())
        self.value = new_value

    def get_temperature(self):
        return self.value

    def to_json(self):
        sensor_measurement_encoded = json.dumps(self.__dict__)
        return sensor_measurement_encoded

    @staticmethod
    def json_decoder(json_sensor_measurement_dict):
        return SensorMeasurement(json_sensor_measurement_dict['value'])

    @staticmethod
    def from_json(json_sensor_measurement_str: str):

        json_sensor_measurement_dict = json.loads(json_sensor_measurement_str)
        actuator_state = SensorMeasurement.json_decoder(json_sensor_measurement_dict)

        return actuator_state


class ActuatorState:
    def __init__(self, uuid, state):
        self.uuid = uuid
        self.state = state

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_dict(data):
        # Sørg for at vi ikke får KeyError:
        uuid = data.get("uuid", None)
        state = data.get("state", None)

        if uuid is None or state is None:
            raise ValueError(f"Ugyldige data mottatt i from_dict: {data}")

        return ActuatorState(uuid, state)

    @staticmethod
    def json_decoder(json_actuator_state_dict):
        return ActuatorState.from_dict(json_actuator_state_dict)

    @staticmethod
    def from_json(json_actuator_state_str: str):
        json_actuator_state_dict = json.loads(json_actuator_state_str)
        return ActuatorState.from_dict(json_actuator_state_dict)