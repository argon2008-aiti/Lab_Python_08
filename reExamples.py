import re

# find the word pretty
def hasPretty(inp):
    return re.search(r'pretty', inp) != None
print hasPretty('i am pretty so yeah')
print hasPretty('i am not that ahhh')
    
def whichPet(inp):
    result = re.search(r'pet (cat|dog)', inp)
    if result == None:
        return None
    return result.group(1)
print whichPet('my pet cat')
print whichPet('my pet dog was cool')
print whichPet('my pet donkey')


def getAdjs(inp):
    return re.findall(r'\w+y', inp)
    #return re.findall(r'[a-zA-Z0-9_]+y', inp) # the same thing
    #return re.findall(r'\w{1,}y', inp) # the same thing
print getAdjs('the funny book was goofy')


def isEmail(inp):
    return re.match (r'\w+@\w+(\.\w{2,4}(\.|\b))+', inp) != None
print isEmail('macpherson2008@hello.co.edu')
print isEmail('sd$sd@hello.com')


def getTxts(files):
    return re.findall(r'\w+\.txt', files )
print getTxts( 'yo.html blah.txt woah.txt he ' )


def isAwesome(inp):
    total = re.findall(r'\w+', inp )
    targets = re.findall(r'\w*awes[o|0]me\w*', inp )
    percentage = float( len(targets) )/ len(total)
    print "%.1f" %(percentage * 100)
isAwesome('iamawesomeblah and awes0me is as awesomeo does')



