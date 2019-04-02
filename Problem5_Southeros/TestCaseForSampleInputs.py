from Solution import SoutherosSolution


class Tests:
    def RunProblem1(self):
        sampleIo = """Who is the ruler of Southeros?
                Ouput: None
                Allies of Ruler?
                Output: None
                Input Messages to kingdoms from King Shan: 
                Input: Air, "oaaawaala"
                Input: Land, "a1d22n333a4444p"
                Input: Ice, "zmzmzmzaztzozh\""""
        southeros = SoutherosSolution()
        print('Problem1_Sample1')
        southeros.ExecuteProblem1(sampleIo)

        sampleIo = """Who is the ruler of Southeros?
        Output: None
        Allies of King Shan?
        Output: None
        Input Messages to kingdoms from King Shan:
        Input: Air, "Let's swing the sword together"
        Input: Land, "Die or play the tame of thrones"
        Input: Ice, "Ahoy! Fight for me with men and money"
        Input: Water, "Summer is coming"
        Input: Fire, "Drag on Martin!\""""
        print('\nProblem1_Sample2')
        southeros.ExecuteProblem1(sampleIo)

    def RunProblem2(self):
        sampleIo = """Who is the ruler of Southeros?
        Output: None
        Allies of Ruler?
        Output: None
        Enter the kingdoms competing to be the ruler: 
        Input: Land Air"""
        #southeros = SoutherosSolution()
        #southeros.ExecuteProblem2(sampleIo)

        sampleIo = """Who is the ruler of Southeros? Output: None
        Allies of Ruler?
        Output: None
        Enter the kingdoms competing to be the ruler: 
        Input: Fire Space"""
        southeros = SoutherosSolution()
        southeros.ExecuteProblem2(sampleIo)
test = Tests()
#test.RunProblem1()
test.RunProblem2()