import re

phoneNo = re.compile(r'\d\d\d\-\d\d\d\d\-\d\d\d\d')

mo = phoneNo.search('134-0201-5988')

if mo:
    print ('result '+ mo.group())
else:
    print 'not found'

