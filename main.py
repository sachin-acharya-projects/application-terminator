# Importing required modules
import subprocess, time, os, ctypes
from colorama import Fore, init
from database_handle import Options
from py_setenv import setenv
init(autoreset=True)
class ClosingApp:
    def __init__(self):
        self.__instance__ = Options()
    def init(self):
        pass # Currently do nothing
    def display(self):
        fetchedList = self.__instance__.fetch()
        if len(fetchedList) == 0:
            print("[Database is EMPTY] Please UPDATE database\n")
            print("[UP] Update Database\n")
        else:
            print("[Choose Options]")
            print("")
            print("[(Note: For multiple application [ENTER] individual index with whitespace in-between (space))]")
            print("\n")
            print("[All] Close All Applications")
            print("\n")
            for item in fetchedList:
                print("[{:02}] {}".format(item[0], item[1]))
                print("")
            print("\n")
            print("[CL] Clear Screen")
            print("")
            print("[DS] Display Menu")
            print("")
            print("[UP] Update Database")
            print("")
            print("[ADD] ADD APPLICATION TO SYSTEM PATH")
            print("")
            print("[EX] Exit")
    def update(self, params: tuple):
        return self.__instance__.insert(params)
    def close_apps(self, option='all'):
        print("\n")
        if "all" in option.lower():
            counting = 0
            for item in self.__instance__.fetch():
                try:
                    print("{}[Terminating {}]\r".format(Fore.GREEN, item[1]), end="")
                    __item_name__ = item[2] if str(item[2]).endswith('.exe') else item[2]+".exe"
                    subprocess.check_output("TASKKILL /F /IM {}".format(__item_name__), stderr=subprocess.STDOUT)
                    counting += 1
                except subprocess.CalledProcessError:
                    print("{}[Terminating {}] ❌".format(Fore.RED, item[1]))
                    if not counting <= 0:
                        counting -= 1
            # print("{} TASK(S) WERE TERMINATED".format(counting))
        else:
            counting = 0
            option = option.split()
            outlet = self.__instance__.fetch()
            for opt in option:
                opt = int(opt) - 1
                try:
                    print("{}[Terminating {}]\r".format(Fore.GREEN, outlet[opt][1]), end="")
                    __item_name__ = outlet[opt][3] if outlet[opt][3].endswith('.exe') else outlet[opt][3]+'.exe'
                    subprocess.check_output("TASKKILL /F /IM {} /T".format(__item_name__), stderr=subprocess.STDOUT)
                    counting += 1
                except subprocess.CalledProcessError:
                    print("{}[Terminating {}] ❌".format(Fore.RED, outlet[opt][1]))
                    if not counting <= 0:
                        counting -= 1
        print("_" * 60, "\n")
        if counting == 0:
            print("{}{} TASK(S) ARE TERMINATED".format(Fore.RED, counting))
        else:
            print("{}{} TASK(S) ARE TERMINATED".format(Fore.CYAN, counting))
        # print(" " * 10)
    def close(self):
        self.__instance__.close()
def main(app: ClosingApp):
    print("Please [SAVE] all your work before closing any task(s)\n")    
    app.init()
    app.display()
    while True:
        option = input("\nEnter [INDEX]: ")
        if 'ex' in option.lower() or 'exit' in option.lower() or 'e' in option.lower():
            break
        elif 'cl' in option.lower():
            os.system("cls")
        elif 'ds' in option.lower():
            app.display()
        elif 'up' in option.lower():
            print("[Updating into Database]\n")
            counting = 0
            while True:
                if counting > 0:
                    print("\nContinue Updating?")
                    print("press [ENTER] to continue")
                    print("[E/Exit] Exit\n")
                    opt = input("")
                    if opt.lower() == 'exit' or opt.lower() == 'e' or opt.lower() == 'ex':
                        break
                res = app.update((input("[Applications Name]: "), input("[Short Name]: "), input("[Process]: ")))
                print(res)
                if res:
                    counting += 1
                    continue
                else:
                    break
        elif 'add' in option.lower():
            BASE_PATH = os.path.dirname(os.path.abspath(__file__))
            print("\n{}This option will add current location {} to system path so that you can invoke this application with simple command 'Closing App' in your terminal".format(Fore.LIGHTBLACK_EX, BASE_PATH))
            print("")
            if input("Press [ENTER] to continue, [EXIT] to exit").lower() == 'exit':
                continue
            path_list = setenv("PATH", suppress_echo=True, user=True).split(";")
            if not BASE_PATH in path_list:
                setenv("PATH", value=BASE_PATH, append=True, user=True, suppress_echo=True)
            print("{}Location has been added to system path without any dublications".format(Fore.CYAN))
        else:
            app.close_apps(option)
    app.close()
    print("[Exiting]")
def isAdmin(args):
    try:
        isAdminL = bool(ctypes.windll.shell32.IsUserAnAdmin())
    except:
        isAdminL = False
    if '--force-admin' in args:
        isAdminL = True
    return isAdminL
def displayMessage():
    print("""{}Cannot Execute the Process
        [Reason]
            Permission Denied (UAC Elevation is Required)
        [Why]
            Why UAC Elevation is Required?
                Some of you applications are running under administrator previlege
                to [Terminate] those application, administrator permission is required
        
        [Restart] The Process with Administrator Permission (Run As Administrator)
        
        [OR]
        
        [If you do not need to close applications running under administrator, the [RE-RUN] Script with --force-admin option]
    """.format(Fore.RED))
if __name__ == '__main__':
    import sys
    if isAdmin(sys.argv):
        start_time = time.time()
        # Main Code Started here
        app = ClosingApp()
        main(app)
        # Main Code Ended here
        print("\n{}Program Completed in {} Seconds".format(Fore.CYAN, time.time() - start_time))
        time.sleep(1)
    else:
        displayMessage()
    exit(0)