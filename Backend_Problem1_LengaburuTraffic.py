from Orbit import Orbit
from Route import Route
from Vehicle import Vehicle
from Routes import Routes
import GlobalVariables

def getOrbitSample1(i):
    orbit = input()
    orbitinfo = orbit.split()
    orbitspeed = [int(speed) for speed in orbitinfo if speed.isnumeric()][0]
    name = orbitinfo[0]
    source = GlobalVariables.Source
    destination = GlobalVariables.Destination
    if i == 1:
        craters = 10
    else:
        craters = 20
    if i == 1:
        distance = 20
    else:
        distance = 18
    orbit = Orbit(name, orbitspeed, source, destination, distance, craters)
    return orbit


def getOrbitSample2(i):
    orbit = input()
    orbitinfo = orbit.split()
    orbitspeed = [int(speed) for speed in orbitinfo if speed.isnumeric()][0]
    name = orbitinfo[0]
    source = GlobalVariables.Source
    destination = GlobalVariables.Destination
    if i == 1:
        craters = 20
        distance = 18
    elif i == 2:
        craters = 10
        distance = 20
    elif i == 3:
        craters = 15
        distance = 30
        destination = 'RK Puram'
    else:
        craters = 18
        distance = 15
        source = 'RK Puram'

    orbit = Orbit(name, orbitspeed, source, destination, distance, craters)
    return orbit


def getWeather():
    weather = input()
    weather = weather.split()[-1]
    return weather


def getReducedCraterByWeather(weather, numberOfCraters):
    if weather == 'Sunny':
        return numberOfCraters - (0.10 * numberOfCraters)
    if weather == 'Rainy':
        return numberOfCraters - (0.20 * numberOfCraters)
    return numberOfCraters


def TestSample1():
    weather = getWeather()
    orbit1 = getOrbitSample1(1)
    orbit2 = getOrbitSample1(2)
    orbit1.numberOfCraters = getReducedCraterByWeather(weather, orbit1.NumberOfCraters)
    orbit2.numberOfCraters = getReducedCraterByWeather(weather, orbit2.NumberOfCraters)
    source = 'SilkDub'
    destination = 'Hallitharam'
    routes = Routes(source, destination, 1, weather)
    routes.AddOrbit(orbit1)
    routes.AddOrbit(orbit2)
    print(routes.GetBestRoute())


def TestSample2():
    weather = getWeather()
    orbit1 = getOrbitSample2(1)
    orbit2 = getOrbitSample2(2)
    orbit3 = getOrbitSample2(3)
    orbit4 = getOrbitSample2(4)
    orbit1.numberOfCraters = getReducedCraterByWeather(weather, orbit1.NumberOfCraters)
    orbit2.numberOfCraters = getReducedCraterByWeather(weather, orbit2.NumberOfCraters)
    orbit3.numberOfCraters = getReducedCraterByWeather(weather, orbit3.NumberOfCraters)
    orbit4.numberOfCraters = getReducedCraterByWeather(weather, orbit4.NumberOfCraters)
    source = 'SilkDub'
    intermediate = 'RK Puram'
    destination = 'Hallitharam'
    routes = Routes(source, destination, 2, weather)
    routes.AddOrbit(orbit1)
    routes.AddOrbit(orbit2)
    routes.AddOrbit(orbit3)
    routes.AddOrbit(orbit4)
    routeCombinations = list()
    for vehicle in GlobalVariables.vehicleswithWeather:
        routes.source = source
        routes.destination = destination
        if weather not in vehicle.Weathers:
            continue

        route_source_to_destination = routes.GetBestRouteByVehicle(vehicle)

        routes.destination = intermediate
        route_source_to_intermediate = routes.GetBestRouteByVehicle(vehicle)

        routes.source = intermediate
        routes.destination = destination
        route_intermediate_to_destination = routes.GetBestRouteByVehicle(vehicle)

        routes.source = destination
        routes.destination = intermediate
        route_destination_to_intermediate = routes.GetBestRouteByVehicle(vehicle)

        source_intermediate_destination = [route_source_to_intermediate, route_intermediate_to_destination]
        source_destination_intermediate = [route_source_to_destination, route_destination_to_intermediate]

        source_intermediate_destination_totalDistance = sum([route.Time for route in source_intermediate_destination])
        source_destination_intermediate_totalDistance = sum([route.Time for route in source_destination_intermediate])

        if source_intermediate_destination_totalDistance > source_destination_intermediate_totalDistance:
            smallestRoutes = source_destination_intermediate
        else:
            smallestRoutes = source_intermediate_destination
        routeName = None
        # smallestRoutes.sort(key=lambda x: x.time)

        for route in smallestRoutes:
            if routeName is None:
                routeName = route.Name
            else:
                routeName = routeName + ' and ' + route.Destination + ' via ' + route.Orbit

        routes.Source = source
        routes.Destination = destination
        routeObj = Route(routeName, routes.Source, routes.Destination, '', vehicle, route.Time)
        routeCombinations.extend([routeObj])
    routeCombinations.sort(key=lambda x: x.Time)
    print(routeCombinations[0])


# In[18]:


sample = input()
GlobalVariables.initVehicles()
GlobalVariables.initSourceAndDestination()
if (sample == '1'):
    TestSample1()
elif sample == '2':
    TestSample2()
else:
    print('Enter valid input\n')
