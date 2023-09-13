# projekt_03
Elections Scraper
This program serves for scraping the information about the 2017 elections in Czech Republic and exporting them into csv.file.

To be able to run the programm you need to install external libraries. Instalation should be done preferably within new environment. To create new environment, create new folder anywhere you would like to have this program saved. Then create new .py file with this code and run it:
import os
import venv

path = "C:\\Folder_x\\Folder_y\\Folder_z\\" (input your path to the folder you created for the program, double backslashes have to be used)
os.makedirs(path, exist_ok=True)
venv.create(path, with_pip=True)

Once new environment created open command prompt and change directory to the path of your environment:
command: cd C:\Folder_x\Folder_y\Folder_z\ (your environment path)
And then activate scripts for this environment, so you can install new libraries:
command: .\Scripts\Activate
Now you can download and install the Requestes and Beautifulsoup libraries:
command: pip install beautifulsoup4 requests 

Once environment is created and libraries are installed, you can run the program. To run it open command prompt or different interpreter and type:
command: python (path to your file) "(link to website with specified area)" "(name of output csv file)"
example: python C:\Folder_x\projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104" "Kolin.csv"

Alternatively, if your command prompt directory is the same as whrere the program is saved you can use just name of the file:
example: python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104" "Kolin.csv"

When you run run this command new csv file with selected name will be saved in the selected directory. The file showing information about the results of elections in specified area.
