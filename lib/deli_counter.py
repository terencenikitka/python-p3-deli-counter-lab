katz_deli = []

def line ():
    pass


def take_a_number (curLine,name):
    print(name,curLine)


def now_serving ():
    if katz_deli[0] :
        print(f'current list serving {katz_deli[0]}')
        katz_deli.remove(katz_deli[0])

    else :
        print ('there is nobody waiting to be served')
