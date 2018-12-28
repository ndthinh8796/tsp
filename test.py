class Test:
    def __init__(self, city, lat, long):
        self.city = city
        self.lat = float(lat)
        self.long = float(long)


a = [Test('HCM', '5', '10'), Test('Ha noi', '10', '11')]
for x, y in enumerate(a):
    print(x, y)
    if y.lat == 5.0:
        a.pop(x)
for x in a:
    print(x)
