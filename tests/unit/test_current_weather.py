import current_weather

def test_current_weather_outputtype():
    assert isinstance(current_weather.current_weather(), str)

def test_current_weather_outputlength():
    assert len(current_weather.current_weather()) > 0 

def test_current_weather_firstletteruppercase():
    assert current_weather.current_weather()[0].isupper()

def test_current_weather_outputword():
    assert current_weather.current_weather()[0:26] == "The current temperature is"
