from subprocess import Popen, PIPE, STDOUT


class Test:
    def TestSample1CasesForProblem1Sample1(self):
        weather = 'Weather is Sunny'
        orbit1 = 'Orbit1 traffic speed is 12 megamiles/hour'
        orbit2 = 'Orbit2 traffic speed is 10 megamiles/hour'

        p = Popen(['python', 'Backend_Problem3_LengaburuTraffic.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        input = '{}\n{}\n{}\n{}\n'.format('1',weather,orbit1,orbit2)
        input_byte = str.encode(input)
        p_stdout = p.communicate(input=input_byte)[0]
        print('Problem 1 - Sample 1 Solution ')
        output = p_stdout.decode('utf-8').strip()
        assert 'Vehicle TukTuk on Orbit1' == output
        print(output)


    def TestSample1CasesForProblem1Sample2(self):
        weather = 'Weather is Windy'
        orbit1 = 'Orbit1 traffic speed is 14 megamiles/hour'
        orbit2 = 'Orbit2 traffic speed is 20 megamiles/hour'

        p = Popen(['python', 'Backend_Problem3_LengaburuTraffic.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        input = '{}\n{}\n{}\n{}\n'.format('1',weather,orbit1,orbit2)
        input_byte = str.encode(input)
        p_stdout = p.communicate(input=input_byte)[0]
        print('Problem 1 - Sample 2 Solution ')
        output = p_stdout.decode('utf-8').strip()
        assert 'Vehicle Car on Orbit2' == output
        print(output)


    def TestSample1CasesForProblem2Sample1(self):
        weather = 'Weather is Sunny'
        orbit1 = 'Orbit1 traffic speed is 20 megamiles/hour'
        orbit2 = 'Orbit2 traffic speed is 12 megamiles/hour'
        orbit3 = 'Orbit3 traffic speed is 15 megamiles/hour'
        orbit4 = 'Orbit4 traffic speed is 12 megamiles/hour'

        p = Popen(['python', 'Backend_Problem3_LengaburuTraffic.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        input = '{}\n{}\n{}\n{}\n{}\n{}\n'.format('2',weather,orbit1,orbit2,orbit3,orbit4)
        input_byte = str.encode(input)
        p_stdout = p.communicate(input=input_byte)[0]
        print('Problem 2 - Sample 1 Solution ')
        output = p_stdout.decode('utf-8').strip()
        print(output)
        assert 'Vehicle TukTuk to Hallitharam via Orbit1 and RK Puram via Orbit4' == output


    def TestSample1CasesForProblem2Sample2(self):
        weather = 'Weather is Windy'
        orbit1 = 'Orbit1 traffic speed is 5 megamiles/hour'
        orbit2 = 'Orbit2 traffic speed is 10 megamiles/hour'
        orbit3 = 'Orbit3 traffic speed is 20 megamiles/hour'
        orbit4 = 'Orbit4 traffic speed is 20 megamiles/hour'

        p = Popen(['python', 'Backend_Problem3_LengaburuTraffic.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        input = '{}\n{}\n{}\n{}\n{}\n{}\n'.format('2', weather, orbit1, orbit2, orbit3, orbit4)
        input_byte = str.encode(input)
        p_stdout = p.communicate(input=input_byte)[0]
        print('Problem 2 - Sample 2 Solution ')
        output = p_stdout.decode('utf-8').strip()
        print(output)
        assert 'Vehicle Car to RK Puram via Orbit3 and Hallitharam via Orbit4' == output


test = Test()
test.TestSample1CasesForProblem1Sample1()
test.TestSample1CasesForProblem1Sample2()
test.TestSample1CasesForProblem2Sample1()
test.TestSample1CasesForProblem2Sample2()