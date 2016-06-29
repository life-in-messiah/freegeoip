from freegeoip import fetch

def test_from_montana():
    place = fetch(ip="72.160.61.110")
    assert place.country_name == "United States"
    assert place.region_code  == "MT"
    assert place.city         == "Kalispell"
    assert place.zip_code     == "59901"
    assert place.latitude     == 48.1987
    assert place.longitude    == -114.3857
    assert place.metro_code   == 762
    assert place.time_zone    == "America/Denver"
