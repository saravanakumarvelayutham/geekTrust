from Vehicle import Vehicle


def init():
    global vehicleswithWeather
    vehicleswithWeather = list()
    bike = Vehicle(1, 'Bike', 10, ['Sunny', 'Windy'], 2)
    tuktuk = Vehicle(2, 'TukTuk', 12, ['Sunny', 'Rainy'], 1)
    car = Vehicle(3, 'Car', 20, ['Sunny', 'Rainy', 'Windy'], 3)
    vehicleswithWeather.extend([bike, tuktuk, car])