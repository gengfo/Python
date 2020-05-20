import re

phoneNoRegExp = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = phoneNoRegExp.search('the string 123-2345-8739')
if mo:
    print mo.group(1)
    print mo.group(2)
    print mo.group(3)
else:
    print 'not found'



