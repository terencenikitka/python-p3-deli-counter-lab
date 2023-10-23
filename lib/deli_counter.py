katz_deli = []

def line (array):
    integer=1
    if array:
        print("The line is currently: ", end="")
        for name in array:
            if name == array[len(array)-1]:
               print(f"{integer}. {name}")
            else:
               print(f"{integer}. {name}",end=" ")
               integer=integer+1

    else:
        print("The line is currently empty.")



def take_a_number (array,name):
    integer=1
    array.append(name)
    for element in array:
        if element==name:
            break
        else:
            integer=integer+1
    print(f"Welcome, {name}. You are number {integer} in line.")


def now_serving (array):
    if array :
        print(f'Currently serving {array[0]}.')
        array.remove(array[0])

    else :
        print ('There is nobody waiting to be served!')
