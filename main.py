# Importing required modules
import subprocess, time, os, ctypes
from colorama import Fore, init
from database_handle import Options

init(autoreset=True)
class ClosingApp:
    def __init__(self):
        self.__instance__ = Options()
    def init(self):
        output = subprocess.check_output("tasklist").decode()
        output = output.splitlines()

        output.pop(0)
        output.pop(0)
        output.pop(0)

        self.__serviceList = []

        for item in output:
            content = " ".join(item.split()).split(" ")
            imageName = ""
            # pidNum = 0
            for mini in content:
                if mini.isdigit():
                    # pidNum = content.index(mini)
                    break
                else:
                    imageName += " {}".format(mini)
            # serviceType = content[pidNum + 1]
            self.__serviceList.append(imageName.strip())
        self.__serviceList = list(set(self.__serviceList))
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
            print("[Cl] Clear Screen")
            print("")
            print("[DS] Display Menu")
            print("")
            print("[UP] Update Database")
            print("")
            print("[EX] Exit")
    def update(self, params: tuple):
        return self.__instance__.insert(params)
    def close_apps(self, option='all'):
        if "all" in option.lower():
            counting = 0
            for item in self.__instance__.fetch():
                if item[2] in self.__serviceList:
                    print("[Terminating {}]".format(item[0]))
                    subprocess.check_output("TASKKILL /F /IM {}".format(item[2]))
                    counting += 1
            return "{} TASK(S) ARE TERMINATED".format(counting)
        else:
            counting = 0
            option = option.split()
            outlet = self.__instance__.fetch()
            for opt in option:
                opt = int(opt) - 1
                if outlet[opt][3] in self.__serviceList:
                    print("Terminating {}".format(outlet[opt][1]))
                    subprocess.check_output("TASKKILL /F /IM {}".format(outlet[opt][3]))
                    counting += 1
            return "{} TASK(S) ARE TERMINATED".format(counting)
    def close(self):
        self.__instance__.close()
def main(app):
    print("Please [SAVE] all your work before closing any task(s)\n")    
    app.init()
    app.display()
    while True:
        option = input("\nEnter [INDEX]: ")
        if 'ex' in option.lower() or 'exit' in option.lower():
            break
        elif 'cl' in option.lower():
            os.system("cls")
        elif 'dl' in option.lower():
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
                    if opt.lower() == 'exit' or opt.lower() == 'e':
                        break
                res = app.update((input("[Applications Name]: "), input("[Short Name]: "), input("[Process]: ")))
                print(res)
                if res:
                    counting += 1
                    continue
                else:
                    break
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
    else:
        displayMessage()
    exit(0)