from src.core.thermal_model import ThermalModel

def test_model():
    model = ThermalModel()
    assert model is not None
