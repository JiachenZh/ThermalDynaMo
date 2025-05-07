class ThermalModel:
    def __init__(self):
        self.temperature = 25.0  # initial temperature

    def predict(self, power):
        """Predicting temperature changes based on power"""
        return self.temperature + power * 0.15 - 0.5 # 0.5 is for thermal release compensation