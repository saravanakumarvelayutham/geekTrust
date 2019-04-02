from Vehicle import Vehicle
import pandas as pd

def initVehicles():
    global vehicleswithWeather
    vehicleswithWeather = list()
    bike = Vehicle(1, 'Bike', 10, ['Sunny', 'Windy'], 2)
    tuktuk = Vehicle(2, 'TukTuk', 12, ['Sunny', 'Rainy'], 1)
    car = Vehicle(3, 'Car', 20, ['Sunny', 'Rainy', 'Windy'], 3)
    vehicleswithWeather.extend([bike, tuktuk, car])


def initSourceAndDestination():
    global Source
    global Destination
    global Intermediate
    Source = 'SilkDub'
    Intermediate = 'RK Puram'
    Destination = 'Hallitharam'

def initCratersAndDistanceForOrbits():
    columns = ['craters','distance','source','destination']
    global orbitInformationSample1
    craters_sample1 = [10,20]
    distance_sample1 = [20,18]
    source_sample1 = [Source] * 2
    destination_sample1 = [Destination] * 2
    orbitInformationSample1 = list(zip(craters_sample1,distance_sample1,source_sample1,destination_sample1))
    orbitInformationSample1 = pd.DataFrame(orbitInformationSample1,columns=columns)

    global orbitInformationSample2
    craters_sample2 = [20,10,15,18]
    distance_sample2 = [18,20,30,15]
    source_sample2 = [Source,Source,Source,Intermediate]
    destination_sample2= [Destination,Destination,Intermediate,Destination]
    orbitInformationSample2 = list(zip(craters_sample2,distance_sample2,source_sample2,destination_sample2))
    orbitInformationSample2 = pd.DataFrame(orbitInformationSample2,columns=columns)

    global weatherInformation
    weatherInformation = {
        'Sunny' : 0.10,
        'Rainy' : 0.20,
        'Windy' : 0.0
    }

    global ProblemNumber