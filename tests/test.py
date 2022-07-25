from utils import calculate_multiplier

def test_fire1()->None:
    multiplier = calculate_multiplier('fire', ['grass'])
    assert multiplier == '2x'

def test_fighting()->None:
    multiplier = calculate_multiplier('fighting', ['ice', 'rock'])
    assert multiplier == '4x'

def test_psychic()->None:
    multiplier = calculate_multiplier('psychic', ['poison', 'dark'])
    assert multiplier == '0x'

def test_water()->None:
    multiplier = calculate_multiplier('water', ['normal'])
    assert multiplier == '1x'

def test_fire2()->None:
    multiplier = calculate_multiplier('fire', ['rock'])
    assert multiplier == '0.5x'