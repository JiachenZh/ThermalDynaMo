from src.core.thermal_model import ThermalModel

def test_model_initialization():
    model = ThermalModel()
    assert model.temperature == 25.0

def test_prediction():
    model = ThermalModel()
    assert 25.0 < model.predict(100) < 40.0

def test_prediction_boundary():
    model = ThermalModel()
    #test power is 0 and max
    assert model.predict(0) == 24.5
    assert 25.0 < model.predict(200) < 55.0	