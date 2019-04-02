from Orbit import Orbit
from Routes import Routes
import GlobalVariables

def getOrbitSamples(weather):
    orbits = []
    if GlobalVariables.ProblemNumber == 1:
        orbitSamples = GlobalVariables.orbitInformationSample1
    else:
        orbitSamples = GlobalVariables.orbitInformationSample2
    for index,orbitSample in orbitSamples.iterrows():
        orbit = input()
        orbitinfo = orbit.split()
        orbitspeed = [int(speed) for speed in orbitinfo if speed.isnumeric()][0]
        name = orbitinfo[0]
        craters = orbitSample['craters']
        distance = orbitSample['distance']
        source = orbitSample['source']
        destination = orbitSample['destination']
        orbitObject = Orbit(name, orbitspeed, source, destination, distance, craters)
        orbitObject.setReducedCraterByWeather(weather)
        orbits.extend([orbitObject])
    return orbits


def getWeather():
    weather = input()
    weather = weather.split()[-1]
    return weather


def TestSample(problem):
    GlobalVariables.ProblemNumber = problem
    weather = getWeather()
    orbits = getOrbitSamples(weather)
    routes = Routes(GlobalVariables.Source,GlobalVariables.Intermediate, GlobalVariables.Destination, weather)
    for orbit in orbits:
        routes.AddOrbit(orbit)
    if problem == 1:
        print(routes.GetBestRoute())
    elif problem == 2:
        print(routes.GetBestRouteForProblem2())


sample = int(input())
GlobalVariables.initVehicles()
GlobalVariables.initSourceAndDestination()
GlobalVariables.initCratersAndDistanceForOrbits()
assert sample in [1,2]
TestSample(sample)
