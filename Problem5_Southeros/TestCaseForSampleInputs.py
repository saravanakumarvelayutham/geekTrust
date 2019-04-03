from Solution import SoutherosSolution


class Tests:
    def RunProblem1(self):
        print('\nProblem1_Sample1')
        print('Input Messages to kingdoms from King Shan:')
        sampleIo = """Input: Air, "oaaawaala"
                Input: Land, "a1d22n333a4444p"
                Input: Ice, "zmzmzmzaztzozh\""""
        print(sampleIo)
        southeros = SoutherosSolution()
        southeros.ExecuteProblem1(sampleIo)


        print('\nProblem1_Sample2')
        print('Input Messages to kingdoms from King Shan:')
        sampleIo = """Input: Air, "Let's swing the sword together"
        Input: Land, "Die or play the tame of thrones"
        Input: Ice, "Ahoy! Fight for me with men and money"
        Input: Water, "Summer is coming"
        Input: Fire, "Drag on Martin!\""""
        print(sampleIo)
        southeros.ExecuteProblem1(sampleIo)

    def RunProblem2(self):
        print('\nProblem2_Sample1')
        print('Enter the kingdoms competing to be the ruler:')
        sampleIo = """Input: Land Air"""
        print(sampleIo)
        southeros = SoutherosSolution()
        southeros.ExecuteProblem2(sampleIo)

        print('\nProbelm2_Sample2')
        sampleIo = """Input: Fire Space"""
        print('Enter the kingdoms competing to be the ruler:')
        print(sampleIo)
        southeros = SoutherosSolution()
        southeros.ExecuteProblem2(sampleIo)

        sampleIo = """"""
test = Tests()
#test.RunProblem1()
test.RunProblem2()