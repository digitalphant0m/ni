import requests
import json
import time

# comparing values
def compare(test,expected):
    if test == expected:
        return 1
    else:
        return 0

# 
def find(value):
    return 'found value'

# gateway function
def review(druthers):
     # init
    tests = 0
    failed = 0

    for x in druthers:
        # start time
        start = time.time()

        payload = x['payload']
        res = requests.post(x['url'], json=payload)

        if x['type'] == 'find':
            result = find(x)
        elif x['type'] == 'compare':
            result =  compare(res.status_code, 200)

        tests += 1

    #end result
    failed = tests - result
    # end time
    end = time.time()

    print('.----------------------------------------------------------------------')
    print('Ran ' + str(tests) + ' test(s) in ' + str(end - start))
    print('PASSED: ' + str(result))
    print('FAILED: ' + str(failed))

