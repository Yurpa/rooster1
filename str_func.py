def strfunc(text):
    '''I want to commit a lot of harm to people'''
    return str(text).upper()

def kys(text):
    '''Watashi wa fkn deadass'''
    list = str(text).split(' ')
    new = ''
    newnew = []
    for i in list:
        newnew.append(i.capitalize())
    new = ' '.join(newnew)
    return new

def helloworld():
    print('Helloworld')
