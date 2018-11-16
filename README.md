# ni
the python unit testing framework that requires more than just shrubbery.



#### example test
```
import json
import sys

from ni import Ni

print('Testing in progress....')

# NI_TEST

# modular configuration method for calling API(get,post,put,delete)

druthers = [
    {
        'payload':{'payload':'value'},
        'url':'http://[yourapi.com]',
        'type':'compare'
    },
    {
        'payload':"expected output",
        'url':'http://[yourapi.com]',
        'type':'find'
    }
]

# providing shrubbery
ni = Ni(druthers)
ni.review()
```
