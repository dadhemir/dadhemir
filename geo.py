import csv
from simple_geoip import GeoIP

geoip = GeoIP("at_MjrNJBsAWuIdVB5L4ExgieZBHz2A0");
#data = geoip.lookup("78.183.132.51")
#print(data)

with open('buzones.txt', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        ip = row[1]
        buzon = row[0]
        primerocteto = ip.split(".")
        dif200 = int(primerocteto[0]) - 200
        dif190 = int(primerocteto[0]) - 190
        dif180 = int(primerocteto[0]) - 180
        dif170 = int(primerocteto[0]) - 170
        dif160 = int(primerocteto[0]) - 160
        if not((dif200 >= 0 and dif200 < 10) or (dif190 >= 0 and dif190 < 10) or (dif180 >= 0 and dif180 < 10) or (dif170 >= 0 and dif170 < 10) or (dif160 >= 0 and dif160 < 10)):
            print(buzon + " accede desde la IP " + ip)
            data = geoip.lookup(ip)
            print(data)
            print("---")