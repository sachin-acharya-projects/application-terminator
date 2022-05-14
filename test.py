import time, ctypes, sys
start_time = time.time()

def function_1():
    ini_list = [
        [1, 2, 5, 10, 7],
        [4, 3, 4, 3, 21],
        [45, 65, 8, 8, 9, 9],
        [1, 2, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 7, 8, 12]
    ]

    elem = 8
    elem1 = 0

    # element exists in listof listor not?
    res1 = elem in (item for sublist in ini_list for item in sublist)
    res2 = elem1 in (item for sublist in ini_list for item in sublist)

    # printing result
    print(res1, res2)
def function_2():

    ini_list = [
        [1, 2, 5, 10, 7],
        [4, 3, 4, 3, 21],
        [45, 65, 8, 8, 9, 9]
    ]

    elem_to_find = 8
    elem_to_find1 = 0

    # element exists in listof listor not?
    res1 = any(elem_to_find in sublist for sublist in ini_list)
    res2 = any(elem_to_find1 in sublist for sublist in ini_list)

    # printing result
    print(res1, res2)
def tups():
    tup = ("", "", "")
    a = [test == '' for test in tup]
    print(all(a))

class CheckingUAC:
    def __init__(self):
        if self.isAdmin():
            print("Hello World")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    def isAdmin(self):
        try:
            return ctypes.windll.shell32.isUserAdmin()
        except:
            return False

CheckingUAC()
print("{} seconds".format(time.time() - start_time))
