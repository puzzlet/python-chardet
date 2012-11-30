import sys

if sys.version_info >= (3, ):
    _b = lambda _: _.encode('ascii')
    _bytechar = int
    _byteord = int
else:
    _b = str
    _bytechar = chr
    _byteord = ord
