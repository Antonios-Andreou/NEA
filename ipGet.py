
from urllib.request import urlopen
from json import load
#required modules



def ipInfo(addr=''):

    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    latlong = data.get("loc").split(",")

    return tuple(latlong)


if __name__ == '__main__':
    latitude, longitude = ipInfo()
    print(latitude)
    print(longitude)


