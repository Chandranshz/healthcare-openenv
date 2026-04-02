import random

class HealthcareEnv:
    def __init__(self):
        self.state_data = None
        self.done = False

    def reset(self):
        self.state_data = {
            "symptoms": random.choice([
                ["fever", "cough"],
                ["chest_pain", "shortness_of_breath"],
                ["headache", "nausea"]
            ]),
            "age": random.randint(20, 70),
            "diagnosis": None,
            "correct_diagnosis": None
        }

        correct_map = {
            ("fever", "cough"): "flu",
            ("chest_pain", "shortness_of_breath"): "heart_disease",
            ("headache", "nausea"): "migraine"
        }

        self.state_data["correct_diagnosis"] = correct_map.get(tuple(self.state_data["symptoms"]))

        self.done = False
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        reward = 0

        if action == self.state_data["correct_diagnosis"]:
            reward = 1.0
            self.state_data["diagnosis"] = action
            self.state_data["diagnosis_correct"] = True
            self.done = True
        else:
            reward = -0.5
            self.state_data["diagnosis"] = action
            self.state_data["diagnosis_correct"] = False

        return self.state(), reward, self.done, {}
    
    