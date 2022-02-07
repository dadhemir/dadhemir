from simple_geoip import GeoIP

geoip = GeoIP("at_MjrNJBsAWuIdVB5L4ExgieZBHz2A0");

with open('source.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end='')
        ip = line
        data = geoip.lookup(ip)
        print(data)
        line = reader.readline()
        print("---")