import uk_covid_announcement

def test_uk_covid_announcement_outputtype():
    assert isinstance(uk_covid_announcement.uk_covid_announcement(), str)

def test_uk_covid_announcement_outputlength():
    assert len(uk_covid_announcement.uk_covid_announcement()) > 0

def test_uk_covid_announcement_outputuppercase():
    assert uk_covid_announcement.uk_covid_announcement()[0].isupper()

def test_uk_covid_announcement_outputword():
    assert uk_covid_announcement.uk_covid_announcement()[0:12] == "For COVID-19"
