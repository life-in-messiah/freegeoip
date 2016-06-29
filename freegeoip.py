from requests import get


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def fetch(server="https://freegeoip.net/", ip=None):

    # construct the request URL
    query_prefix = ("/" if not server.endswith("/") else "") + \
        "json/" + \
        ("?q=" if ip else "")

    request_url = server + query_prefix + ip

    res = get(request_url)

    if res.status_code != 200:
        raise Exception("HTTP status code returned %i" % res.status_code)

    return Struct(**res.json())
