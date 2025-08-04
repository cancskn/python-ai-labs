"""
Take a list of name
Create a empty dictionary
Loop over list and check how many times name is repeated
Append to dictionary name as a key and times repeated as value
"""
def histogram(names):
    d = {}
    for name in names:
        if name not in d:
            d[name] = names.count(name)
    return d

names = ['can', 'mar', 'tedi', 'tedi']
print(histogram(names))



