# Importing required modules
import json, subprocess, os

output = subprocess.check_output("tasklist").decode()
output = output.splitlines()

output.pop(0)
output.pop(0)
output.pop(0)

serviceList = []

for item in output:
    content = " ".join(item.split()).split(" ")
    imageName = ""
    pidNum = 0
    for mini in content:
        if mini.isdigit():
            pidNum = content.index(mini)
            break
        else:
            imageName += " {}".format(mini)
    serviceType = content[pidNum + 1]
    serviceList.append(imageName.strip())
serviceList = list(set(serviceList))

class Options():
    def __init__(self):
        self.tasklist = []
        self.count = 0
    def options(self):
        with open('options.json', 'r') as file:
            items = json.load(file)
            print("Please Choose Options\n")
            print("[1] Close All")
            for item in list(items):
                self.tasklist.append(item['process'])
                print(f"[{items.index(item) + 2}]", item['name'])
    def closeApp(self, option):
        if not option:
            raise Exception('Invalid Parameter Passed. Only integer is allowed')
        else:
            if option == '1':
                for tasklist in self.tasklist:
                    if tasklist in serviceList:
                        subprocess.check_output("TASKKILL /F /IM {}".format(tasklist))
                        self.count += 1
            else:
                indx = int(option) - 2
                if self.tasklist[indx] in serviceList:
                    subprocess.check_output("TASKKILL /F /IM {}".format(self.tasklist[indx]))
                    self.count += 1
                else:
                    print("Task is not running currently")
        print(f"{self.count} Task(s) has been terminated successfully")
    def printItems(self):
        with open('mine.json', "w") as file:
            json.dump({
                "serviceList": serviceList,
                "tasklist": self.tasklist
            }, file, indent=4)
if __name__ == '__main__':
    options = Options()
    options.options()
    options.printItems()
    options.closeApp(input("Enter Option Index: "))