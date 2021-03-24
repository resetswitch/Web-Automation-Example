import subprocess
import time
import random
import os
import sys
import getpass

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException


def createFolder(directory, clear=False, autodelete = False):
    """Creates a folder in the directory, if it doesnt exist. Also deletes some/all files if directed.

    Parameters
    ----------
    directory : str
        A directory to a folder
    clear : bool, optional
        Presents user with the option to delete file(s) (default is False)
    autodelete : bool, optional
        Presents user with the option to delete all files in the directory without prompting for each file (default is False)"""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        elif os.path.exists(directory) and clear == True:
            for filename in os.listdir(directory):
                while True:
                    if autodelete == False:
                        user_in = input("For Directory: {}\nDo you wish to Delete {}? y/n (a to auto-delete and q to quit):\n".format(directory, filename)).lower()
                        if user_in == 'a':
                            autodelete = True
                    if user_in == 'y' or autodelete == True:
                        os.remove(directory+filename)
                        print ("{} DELETED".format(filename))
                        break
                    elif user_in == 'n':
                        print("{} SKIPPED".format(filename))
                        break
                    elif user_in == 'q':
                        sys.exit("USER HAS QUIT")
                    else:
                        print("ERROR: NOT VALID INPUT")
        else:pass
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def delete_crdownload_file(path):
    """Deletes files in path that have extension .crdownload.

    Parameters
    ----------
    path : str
        A path to a folder that holds files with extension .crdownload"""
    for fname in os.listdir(path):
        if fname.endswith(".crdownload"):
            print("deleted {}".format(fname))
            os.remove(path+fname)
        else:
            print("pass {}".format(fname))

def open_browser(download_path_temp, executable_path):
    """Creates a selenium webdriver instance.

    Parameters
    ----------
    download_path_temp : str
        A path to a folder that will hold image files of groups (ie. HD Logo) until they are renamed appropriately.
    executable_path : str
        A path to to the chromedriver.exe"""
    print("Opening/Minimizing Browser")
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_settings.popups": 0,
          "download.default_directory": download_path_temp, # IMPORTANT - ENDING SLASH V IMPORTANT
          "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    try:
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
    except SessionNotCreatedException as err:
        print("\nYou downloaded the incorrect version, see below for right version number and this site to download the driver (https://chromedriver.chromium.org/downloads)\n")
        sys.exit(err)
    except WebDriverException as err:
        print("\nLikely that chromedriver.exe is not in the right directory. Please be sure that chromedriver.exe is in the same folder as 'Download Script.py' to download the driver (https://chromedriver.chromium.org/downloads)\n")
        sys.exit(err)
    return driver
            
def safe_filename_format(string):
    """Creates a selenium webdriver instance.

    Parameters
    ----------
    string : str
        Takes in a string (not including path) and converts the string to a windows/mac/linux friendly format, omitting
    any and all reserved characters"""       
    if os.name == "nt": #Windows
        reserved_characters = ["<",">",":","\"","/","\\","|","?", "*"]
        for rs in reserved_characters:
            string = string.replace(rs, "")
        string = string.replace('–','-')
    else:
        string = string.replace(":", "")
    return string
            
def fanart_dl(URL, title = None, download_path = None, download_path_temp = None):
    """Creates a selenium webdriver instance.

    Parameters
    ----------
    URL : str
        A fanart.tv movie or tv url (i.e. 'https://fanart.tv/movie/2300/space-jam/')
    title : str, optional
        Takes in string to prefix the filename (i.e. 'Space Jam (1996)')
    download_path : str, optional
        Change the default download path (default is r'/Users/{}/Desktop/TV Art/{}/'.format(username, title+' - TV Art')). Note ending slash.
    download_path_temp : str
        Change the default temporary download path (default is r'/Users/{}/Desktop/TV Art/temp/'.format(username)). Note ending slash.
    """   

    #Executable Path for chromedriver.exe
    executable_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')
    
    #Grabbing the html soup from Fanart.tv
    print("{:<100}".format("\rGathering HTML from {}".format(URL)), end = '', flush = True)
    URL_base = 'http://fanart.tv'
    request = requests.get(URL).content
    soup = BeautifulSoup(request, 'html.parser')
    print("{:<100}".format("\rGathered HTML from {}".format(URL)), end = '', flush = True)
    
    #Grabs the title of the page (i.e. Archer (2009)) but because of a lack of uniformity in title namings
    #   on Fanart.tv, like lack of years. a manual option has been added to this function
    if title == None:
        title = soup.find("div", class_ = 'title_background').text.replace("Fanart", "").strip()
        while True:
            user_in = input("\ntitle of Filenames will be, '{}'? Or do you wish for User Input title? c to confirm or u for user input:\n".format(title)).lower()
            if user_in == 'c':
                break
            elif user_in == 'u':
                title = input("input title (i.e. Parks and Recreation (2009)):\n")
            else:
                print("ERROR: NOT VALID INPUT")           
    else:
        pass
    title = safe_filename_format(title)
    print("{:<100}".format("\rHTML for Fanart.tv - {} Complete".format(title)), end = '\n', flush = True)
    
    #Defining the Directories
    username = getpass.getuser()
    if os.name == 'posix':
        if download_path == None:
            download_path = r'/Users/{}/Desktop/TV Art/{}/'.format(username, title+' - TV Art')
        else:pass
        if download_path_temp == None:
            download_path_temp = r'/Users/{}/Desktop/TV Art/temp/'.format(username) #IMPORTANT- ENDING SLASH
        else:pass
    elif os.name == 'nt':
        if download_path == None:
            download_path = r'C:/users/{}/Desktop/TV Art/{}/'.format(username, title+' - TV Art')
        else:pass
        if download_path_temp == None:
            download_path_temp = r'C:\Users\{}\Desktop\TV Art\temp\\'.format(username) #IMPORTANT- ENDING SLASH
        else:pass
    else:
        sys.exit('Need to define download_path and download_path_temp for Linux')
    createFolder(download_path,         clear = False)
    createFolder(download_path_temp,    clear = True)
    os.chdir(download_path_temp)
    
    #Fanart.tv has a certain category and class_ structure. Certain categories/category_classes can be skipped by ommission
    media_type = URL.split('/')[3] #should be either 'series' or 'movie'
    if media_type == 'series':
        #list of sections
        categories          = ["HD ClearLOGO"       , 'Poster'             , 'Season Poster'        , 'ClearLOGO'           , 'Clear ART'       , 'HD ClearART'         , 'Character ART'       , 'Season Thumbs'      ,'TV Thumbs'       , 'Background'              , 'Banner'          , 'Season Banner']
        #list of html <ul> class attributes
        category_classes    = ['artwork hdtvlogo'   , 'artwork tvposter'   , 'artwork seasonposter' , 'artwork clearlogo'   , 'artwork clearart', 'artwork hdclearart'  , 'artwork characterart', 'artwork seasonthumb','artwork tvthumb' , 'artwork showbackground'  , 'artwork tvbanner', 'artwork seasonbanner']
    elif media_type == 'movie':
        categories          = ["HD ClearLOGO"       , 'Poster'             , 'ClearLOGO'           , 'Clear ART'       , 'HD ClearART'              , 'Background'              , 'Banner'              , 'Movie Thumbs']           #I have chosen to exclude 'CD ART'
        category_classes    = ["artwork hdmovielogo", 'artwork movieposter', 'artwork movielogo'   , 'artwork movieart', 'artwork hdmovieclearart'  , 'artwork moviebackground' , 'artwork moviebanner' , 'artwork moviethumb']     #Excluding 'artwork moviedisc'
    else:
        sys.exit("This {} is a type of media that is not supported. Please choose either TV Shows (series) or Movies (movies)".format(media_type))
    no_download_class = 'artwork'
    
    #Setting up a browser for automation
    driver = open_browser(download_path_temp, executable_path)
    driver.minimize_window()
    
    #Goes through each element in category_classes
    for i, category_class in enumerate(category_classes):
        #Checks to see if the category has already been downloaded, if it has, then that category is skipped
        skip = None
        for filename in os.listdir(download_path):
            if categories[i] in filename:
                skip = True
                break
            else:
                skip = False
        if skip == True:
            continue
        else:pass
        
        #There are cases where category_class will not be found. As Fanart.tv html has a class 'artwork' to define categories that have no elements to download
        try:
            category_class_soup = soup.find('ul', class_ = category_class)
        except:
            continue
        if category_class_soup == None:
            continue
        
        #For the existence of a category_class, this loop will go through all the download URL's
        soup_URLs = category_class_soup.find_all("a", class_ = "btn btn-inverse download")
        for f_num, soup_URL in enumerate(soup_URLs):
            percent_complete = round((i/(len(category_classes)))*100 + (1/len(category_classes))/len(soup_URLs)*(f_num+1)*100,2)
            print("{:<200}".format("\rOverall {}% Complete; Downloading {} Links, {} of {}".format(percent_complete, categories[i], f_num+1, len(soup_URLs))), end = "", flush = True)
            stalled = None
            trys = 1
            #Occasionally a download will take some time to download and will 'stall' the loop.
            #If the download takes too long, the download will be deleted and re-attempt to download file for a certain number of 'trys'
            while stalled == True or stalled == None:
                stalled = False
                URL_path_component = soup_URL.get("href")
                if media_type == 'movie':
                    URL_path_component = URL_path_component.replace('§', '&sect')
                driver.get('https://fanart.tv' + URL_path_component)
                time.sleep(random.randint(2,4)) #so downloading wont look so robotic to the website
                stalled_time = 0
                while not all(['.crdownload' not in filename for filename in os.listdir(download_path_temp)]): #all would return [True, True, False]. False would be if if .crdownload was found
                    tts = 2 #time to sleep
                    time.sleep(tts)
                    stalled_time+=tts
                    print("{:<200}".format('\rOverall {}% Complete; Waiting for {} (html_class: {}) FILE ({}) to download; try(s) {}; Time Stalled {}s'.format(percent_complete, categories[i], category_class, f_num, trys, stalled_time)), end = '', flush = True)
                    if stalled_time == 30 and trys < 3:
                        stalled = True
                        trys+=1
                        driver.close()
                        delete_crdownload_file(download_path_temp)
                        driver = open_browser(download_path_temp, executable_path)
                        driver.minimize_window()
                        break
                    elif stalled_time == 30 and trys == 3:
                        stalled = False
                        driver.close()
                        delete_crdownload_file(download_path_temp)
                        driver = open_browser(download_path_temp, executable_path)
                        driver.minimize_window()
                        print("{:<200}".format("\rOverall {}% Complete; {} ({})FILE ({}) has been skipped. Reason: Timeout {}".format(percent_complete, categories[i], category_class, f_num, tts)), end = '\n', flush = True)
                        break
                    else:
                        stalled = False
        #Renames files according to their category       
        for filename in os.listdir(download_path_temp):
            proposed_rename = safe_filename_format(title + " - " + categories[i])
            file_num = ""
            root, ext = os.path.splitext(filename)
            count = 0
            while True:
                # time.sleep(3)
                if os.path.exists(download_path + proposed_rename + file_num + ext) == True:
                    count+=1
                    file_num = " ({})".format(count)
                else:
                    os.rename(download_path_temp + filename, download_path + proposed_rename + file_num + ext)
                    break
    print("{:<101}".format("\rNo more links remaining; Overall 100% Complete"), end = "\n", flush = True)
    print("Closing Browser")
    driver.close()
    print("Files have been downloaded to: {}".format(download_path))

fanart_dl("https://fanart.tv/movie/2300/space-jam/", 
          title = "Space Jam (1996)",
          download_path=None,
        # download_path_temp=r"C:\Users\bedj2\Desktop\TV Art\temp2\\"
          )

