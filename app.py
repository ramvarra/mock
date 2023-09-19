import requests
from pprint import pprint, pformat

class App:
    def __init__(self):
        pass

    def myip(self):
        r = requests.get('https://ipinfo.io')
        r.raise_for_status()
        return r.json()

    def get_my_loc(self) -> tuple[float, float]:
        info = self.myip()
        print("Info: ", info)

        # if loc is not there, raise ValueError
        if not (loc := info.get('loc')):
            raise ValueError("No LOC in ipinfo")

        vals = tuple(float(v) for v in info['loc'].split(','))

        # if loc has only one value, default the second value is 1.0
        if len(vals) == 1:
            return (vals[0], 1.0)

        #'33.4484,-112.0740',
        return vals

if __name__ == '__main__':
    app = App()
    ipinfo = app.myip()
    #pprint(ipinfo)

    pprint(app.get_my_loc())
