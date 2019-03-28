from Orbit import Orbit
from Routes import Routes
import GlobalVariables

def getOrbitSamples(sample,weather):
    orbits = []
    if sample == 1:
        orbitSamples = GlobalVariables.orbitInformationSample1
    else:
        orbitSamples = GlobalVariables.orbitInformationSample2
    for index,orbitSample in orbitSamples.iterrows():
        orbit = input()
        orbitinfo = orbit.split()
        orbitspeed = [int(speed) for speed in orbitinfo if speed.isnumeric()][0]
        name = orbitinfo[0]
        craters = getReducedCraterByWeather(weather,orbitSample['craters'])
        distance = orbitSample['distance']
        source = orbitSample['source']
        destination = orbitSample['destination']
        orbitObject = Orbit(name, orbitspeed, source, destination, distance, craters)
        orbits.extend([orbitObject])
    return orbits


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

def TestSample(sample):
    weather = getWeather()
    orbits = getOrbitSamples(sample,weather)

    routes = Routes(GlobalVariables.Source, GlobalVariables.Destination, sample, weather)

    for orbit in orbits:
        routes.AddOrbit(orbit)

    if sample == 1:
        print(routes.GetBestRoute())
    elif sample == 2:
        print(routes.GetBestRouteForSample2())


sample = int(input())
GlobalVariables.initVehicles()
GlobalVariables.initSourceAndDestination()
GlobalVariables.initCratersAndDistanceForOrbits()
assert sample in [1,2]
TestSample(sample)
