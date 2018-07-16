class errorOne(Exception):pass

try:
    raise errorOne
except errorOne:
    print('fuck')

