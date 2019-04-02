from Kingdom import Kingdom


def initalizeConstants():
    global kingdoms
    kingdoms = list()
    kingdomEmblems = {
        'Land' : 'Panda',
        'Water' : 'Octopus',
        'Ice' : 'Mammoth',
        'Air' : 'Owl',
        'Fire' : 'Dragon',
        'Space' : 'Gorilla'
    }
    for name,emblem in kingdomEmblems.items():
        kingdom = Kingdom(name,emblem,0)
        kingdoms.extend([kingdom])
    del kingdomEmblems

    global messagesForSelection
    messagesForSelection = ['Summer is coming','a1d22n333a4444p','oaaawaala','zmzmzmzaztzozh','Go risk it all','Let\'s swing the sword together',
                'Die or play the tame of thrones','Ahoy! Fight for me with men and money','Drag on Martin!','When you play the tame of thrones you win or you die.',
                'What could we say to the Lord of Death? Game on?','Turn us away and we will burn you first','Death is so terribly final while life is full of possibilities.',
                'You Win or You Die','His watch is Ended','Sphinx of black quartz judge my dozen vows','Fear cuts deeper than swords My Lord.',
                'Different roads sometimes lead to the same castle.','A DRAGON IS NOT A SLAVE.','Do not waste paper','Go ring all the bells',
                'Crazy Fredrick bought many very exquisite pearl emerald and diamond jewels.','The quick brown fox jumps over a lazy dog multiple times.',
                'We promptly judged antique ivory buckles for the next prize.','Walar Morghulis: All men must die.']

    global Round
    Round = 1

    global Winner