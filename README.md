# freegeoip [![Build Status](https://travis-ci.org/life-in-messiah/freegeoip.svg?branch=master)](https://travis-ci.org/life-in-messiah/freegeoip)
Pythonic wrapper around the freegeoip web service

## Installation
~~Using pip~~ **NOT IMPLEMENTED YET: For now, download and then put freegeoip.py in your `PATH`**

## Usage
(Python 3 syntax)
```python
from freegeoip import fetch

# to fetch using the system IP
local_data = fetch()

# to fetch using a manually-entered IP
manual_data = fetch(ip="72.160.61.110")

# to fetch using a different server
server_data = fetch(server="http://freegeoip.mywebservice.com")
```

`fetch()` returns a data structure upon success or throws an `Exception` upon failure.  If we looked into the variable `local_data` from the above example, the available data would be as follows:
```python
local_data.country_name # Ex. "United States"
local_data.region_code  # Ex. "Montana"
local_data.city         # Ex. "Kalispell"
local_data.zip_code     # Ex. "59901"
local_data.latitude     # Ex. 48.1987
local_data.longitude    # Ex. -114.3857
local_data.metro_code   # Ex. 762
local_data.time_zone    # Ex. "America/Denver"
```
