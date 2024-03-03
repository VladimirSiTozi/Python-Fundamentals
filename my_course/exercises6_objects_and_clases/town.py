class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town(input("Enter town: "))
town.set_latitude(input("Enter latitude: "))
town.set_longitude(input("Enter longitude: "))
print(town)

town1 = Town(input("Enter town: "))
town1.set_latitude(input("Enter latitude: "))
town1.set_longitude(input("Enter longitude: "))
print(town1)