#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Location:
    def __init__(self,name):
        self.name = name


# In[2]:


class Orbit:
    def __init__(self,name,speed,source,destination,distance,numberofcraters):
        self.name = name
        self.speed = int(speed)
        self.source = source
        self.destination = destination
        self.distance = int(distance)
        self.numberofcraters = numberofcraters
    def __str__(self):
        return 'Name: {} speed: {} source: {} destination: {} distance: {} numberofcraters: {} \n'.format(self.name,self.speed,self.source,self.destination,self.distance,self.numberofcraters)


# In[3]:


class Vehicle:
    def __init__(self,order,name,speed,weathers,timepercrater):
        self.order = order
        self.name = name
        self.speed = int(speed)
        self.weathers = weathers
        self.timepercrater = int(timepercrater)
    def __str__(self):
        return 'Order: {} Vehicle: {} Speed: {} weathers: {} timePerCreater: {} \n'.format(self.order,self.name,self.speed,self.weathers,self.timepercrater)


# In[4]:


class Route:
    def __init__(self,name,source,destination,orbit,vehicle,time):
        self.name = name
        self.vehicle = vehicle
        self.time = time
        self.source = source
        self.destination = destination
        self.orbit = orbit
    def __str__(self):
        return self.name


# In[5]:


class Routes:
    def __init__(self,source,destination,sample,weather):
        self.source = source
        self.destination = destination
        self.orbits = list()
        self.routes = list()
        self.sample = sample
        self.weather = weather
    def AddOrbit(self,orbit):
        self.orbits.extend([orbit])
    
    def getBestRoute(self):
        self.routes.clear()
        orbits = list([orbit for orbit in self.orbits if ((orbit.source == self.source and orbit.destination == self.destination) or
                                                          (orbit.destination == self.source and orbit.source == self.destination))])
        for orbit in orbits:
            for vehicle in vehicleswithWeather:
                if self.weather not in vehicle.weathers:
                    continue
                if self.sample == 1:
                    route = 'Vehicle {} on {}'.format(vehicle.name,orbit.name)
                else:
                    route = 'Vehicle {} to {} via {}'.format(vehicle.name,orbit.destination,orbit.name)
                speed = orbit.speed
                if vehicle.speed < orbit.speed:
                    speed = vehicle.speed
                megaMilesPerMinute = speed * (1/60)
                time = orbit.distance  / speed
                routeObj = Route(route,self.source,self.destination,orbit.name,vehicle,time)
                self.routes.extend([routeObj])
        self.routes.sort(key=lambda x: x.time)
        #print(self.routes[0])
        return self.routes[0]
        
    
    def getBestRouteByVehicle(self,vehicle):
        self.routes.clear()
        orbits = list([orbit for orbit in self.orbits if ((orbit.source == self.source and orbit.destination == self.destination) or 
                                                          (orbit.destination == self.source and orbit.source == self.destination))])
        for orbit in orbits:
            if self.weather not in vehicle.weathers:
                continue
            if self.sample == 1:
                route = 'Vehicle {} on {}'.format(vehicle.name,orbit.name)
            else:
                route = 'Vehicle {} to {} via {}'.format(vehicle.name,orbit.destination,orbit.name)
            speed = orbit.speed
            if vehicle.speed < orbit.speed:
                speed = vehicle.speed
            megaMilesPerMinute = speed * (1/60)
            time = orbit.distance  / speed
            routeObj = Route(route,self.source,self.destination,orbit.name,vehicle,time)
            self.routes.extend([routeObj])
        self.routes.sort(key=lambda x: x.time)
        #print(self.routes[0])
        return self.routes[0]


# In[6]:


vehicleswithWeather = list()
bike = Vehicle(1,'Bike',10,['Sunny','Windy'],2)
tuktuk = Vehicle(2,'TukTuk',12,['Sunny','Rainy'],1)
car = Vehicle(3,'Car',20,['Sunny','Rainy','Windy'],3)
vehicleswithWeather.extend([bike,tuktuk,car])


# In[7]:


#for vehicle in vehicleswithWeather:
#    print(vehicle)


# In[8]:


def getOrbitSample1(i):
    orbit = input() #input('Enter orbit{} information \n'.format(str(i)))
    #if i == 1:
    #    orbit = "Orbit1 traffic speed is 12 megamiles/hour"
    #else:
    #    orbit = "Orbit2 traffic speed is 10 megamiles/hour"
    orbitinfo = orbit.split()
    orbitspeed = [int(speed) for speed in orbitinfo if speed.isnumeric()][0]
    name = orbitinfo[0]
    source = 'SilkDub'
    destination = 'Hallitharam'
    if i==1:
        craters = 10
    else:
        craters = 20
    if i==1:
        distance = 20
    else :
        distance = 18
    orbit = Orbit(name,orbitspeed,source,destination,distance,craters)
    return orbit


# In[9]:


def getOrbitSample2(i):
    orbit = input()#input('Enter orbit{} information \n'.format(str(i)))
    #if i == 1:
    #    orbit = "Orbit1 traffic speed is 20 megamiles/hour"
    #elif i==2:
    #    orbit = "Orbit2 traffic speed is 12 megamiles/hour"
    #elif i==3:
    #    orbit = "Orbit3 traffic speed is 15 megamiles/hour"
    #else:
    #    orbit = "Orbit4 traffic speed is 12 megamiles/hour"
    orbitinfo = orbit.split()
    orbitspeed = [int(speed) for speed in orbitinfo if speed.isnumeric()][0]
    name = orbitinfo[0]
    source = 'SilkDub'
    destination = 'Hallitharam'
    if i==1:
        craters = 20
        distance = 18
    elif i==2:
        craters = 10
        distance = 20
    elif i==3:
        craters = 15
        distance = 30
        destination = 'RK Puram'
    else:
        craters = 18
        distance = 15
        source = 'RK Puram'
        
    orbit = Orbit(name,orbitspeed,source,destination,distance,craters)
    return orbit


# In[10]:


def getWeather():
    #weather = input('Enter weather condition\n')
    weather = input()
    #weather = 'Weather is Windy'
    weather = weather.split()[-1]
    return weather


# In[11]:


def getReducedCraterByWeather(weather,numberOfCraters):
    if weather == 'Sunny':
        return numberOfCraters - (0.10 * numberOfCraters)
    if weather == 'Rainy':
        return numberOfCraters - (0.20 * numberOfCraters)
    return numberOfCraters


# In[12]:


def TestSample1():
    weather = getWeather()
    orbit1 = getOrbitSample1(1)
    orbit2 = getOrbitSample1(2)
    orbit1.numberofcraters = getReducedCraterByWeather(weather,orbit1.numberofcraters)
    orbit2.numberofcraters = getReducedCraterByWeather(weather,orbit2.numberofcraters)
    source = 'SilkDub'
    destination = 'Hallitharam'
    routes = Routes(source,destination,1,weather)
    routes.AddOrbit(orbit1)
    routes.AddOrbit(orbit2)
    print(routes.getBestRoute())


# In[13]:


def TestSample2():
    weather = getWeather()
    orbit1 = getOrbitSample2(1)
    orbit2 = getOrbitSample2(2)
    orbit3 = getOrbitSample2(3)
    orbit4 = getOrbitSample2(4)
    orbit1.numberofcraters = getReducedCraterByWeather(weather,orbit1.numberofcraters)
    orbit2.numberofcraters = getReducedCraterByWeather(weather,orbit2.numberofcraters)
    orbit3.numberofcraters = getReducedCraterByWeather(weather,orbit3.numberofcraters)
    orbit4.numberofcraters = getReducedCraterByWeather(weather,orbit4.numberofcraters)
    source = 'SilkDub'
    intermediate = 'RK Puram'
    destination = 'Hallitharam'
    routes = Routes(source,destination,2,weather)
    routes.AddOrbit(orbit1)
    routes.AddOrbit(orbit2)
    routes.AddOrbit(orbit3)
    routes.AddOrbit(orbit4)
    routeCombinations = list()
    for vehicle in vehicleswithWeather:
        routes.source = source
        routes.destination = destination
        if weather not in vehicle.weathers:
            continue
        allRoutes = list()
        route_source_to_destination = routes.getBestRouteByVehicle(vehicle)
        
        routes.destination = intermediate
        route_source_to_intermediate = routes.getBestRouteByVehicle(vehicle)
        
        routes.source = intermediate
        routes.destination = destination
        route_intermediate_to_destination = routes.getBestRouteByVehicle(vehicle)
        
        routes.source = destination
        routes.destination = intermediate
        route_destination_to_intermediate = routes.getBestRouteByVehicle(vehicle)
        
        source_intermediate_destination = [route_source_to_intermediate,route_intermediate_to_destination]
        source_destination_intermediate = [route_source_to_destination,route_destination_to_intermediate]
       
        source_intermediate_destination_totalDistance = sum([route.time for route in source_intermediate_destination])
        source_destination_intermediate_totalDistance = sum([route.time for route in source_destination_intermediate])
        
        if source_intermediate_destination_totalDistance > source_destination_intermediate_totalDistance:
            smallestRoutes = source_destination_intermediate
        else:
            smallestRoutes = source_intermediate_destination
        routeName = None
        #smallestRoutes.sort(key=lambda x: x.time)
        
        for route in smallestRoutes:
            if routeName is None:
                routeName = route.name
            else:
                routeName = routeName + ' and ' + route.destination + ' via ' + route.orbit
        
        routes.source = source
        routes.destination = destination
        routeObj = Route(routeName,routes.source,routes.destination,'',vehicle,route.time)
        routeCombinations.extend([routeObj])
    routeCombinations.sort(key=lambda x: x.time)
    print(routeCombinations[0])


# In[18]:


sample = '2'
if(sample == '1'):
    TestSample1()
elif sample == '2':
    TestSample2()
else:
    print('Enter valid input\n')

