# Application Terminator

This is a simple program that can terminate all the provided applications that are running on background.  
Using this application we can terminate many applications at once. We can use this application to terminate single  
as well as multiple application with ease.

#### Who need this?
This program can be usefull to anybody especially to those who needs to launch/open many application simultaneously  
and after completion of work, needs to close all of them one-by-one. This is also for those whose PC lags due to multiple  
unused application running on background. They can easily free memory space by termination those applications

#### Need to Know  
How to use the application.  
* RUN CMD/POWERSHELL with UAC if possible  
* Navigate to Installed folder  
* Execute Following command  
````cmd
python main.py
````
_if program is executed without UAC, it needs to pass --force-admin option_
````cmd
python main.py --force-admin
````
* All the Options will be Displayed

#### Options
1. [All]  
    Case-Insensitive  
        it closes all applications displayed on menu  
2. [Cl/Clear]  
    Case-Insensitive  
        Clear Console Screen  
3. [DS]  
    Case-Insensitive  
    Displays this menu  
4. [UP]  
    Case-Insensitive  
    Update database meaning adding new applications to the list so we can close it from this program next time.  
5. [Integer]  
    This are the index of applications as shown in the menu  
    Multiple application can be choosed by separating indices with whitespace (space)  

#### Fields in Update field
* **Application name**  
Proper/Full name of application that will displayed on menu
* **Short Name**  
Name of application in short form (something like username)
* **Process**  
Executable file name of application

#### How to get Executable File name
Visit the application installed directory (not this) and locate the file with .exe that is used to launch the application
Copy the name of file with extension (.exe)

#### Requirements
````cmd
pip install colorama
````

#### Informations
Do not delete Options.db file
#### Test.py
Ignore this File, it is not necessary for this project