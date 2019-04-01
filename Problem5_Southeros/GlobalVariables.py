from Kingdom import Kingdom


def initalizeConstants():
    global kingdoms
    kingdoms = list()
    kingdomEmblems = {
        'Land' : 'Panda',
        'Water' : 'Octopus',
        'Ice' : 'Mammoth',
        'Air' : 'Owl',
        'Fire' : 'Dragon'
    }
    for name,emblem in kingdomEmblems.items():
        kingdom = Kingdom(name,emblem,0)
        kingdoms.extend([kingdom])
    del kingdomEmblems