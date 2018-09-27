import requests
import json
import time

class Ni:
    def __init__(self, druthers):
        self.druthers = druthers

    # comparing values
    def compare(self,test,expected):
        if test == expected:
            return 1
        else:
            return 0

    # find or match a given result
    def find(self,test,expected):
            arr = []
            for i in test:
                arr.append(i)
            if arr == expected['payload']:
                return 1
            else:
                return 0

    # gateway function
    def review(self):
        # init
        tests = 0
        failed = 0

        for x in self.druthers:
            # start time
            start = time.time()

            payload = x['payload']
            # init call
            res = requests.get(x['url'], json=payload)

            # config method
            if x['type'] == 'find':
                test1 = self.find(res.json(),x)
            elif x['type'] == 'compare':
                test2 = self.compare(res.status_code, 200)

            tests += 1

        result = test1+test2
        # end result
        failed = tests - result

        # end time
        end = time.time()

        print('.----------------------------------------------------------------------')
        print('Ran ' + str(tests) + ' test(s) in ' + str(end - start))
        print('PASSED: ' + str(result))
        print('FAILED: ' + str(failed))

