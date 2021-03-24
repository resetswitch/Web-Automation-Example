<h1> Web-Automation-Example</h1>

<h3>Scenario</h3>
<h6>
  
You love a TV or Movie so much, you would like to download a bunch of related images. You find a website called <a href=fanart.tv>fanart.tv</a>. You search up your favorite TV or Movie, but you have to click `Save` on each of the images.
</h6>

<h3>Solution</h3>
<h6>
  
Instead of downloading each file manually by clicking the `Save` button on fanart.tv for every item and renaming that file to something more readable than `space-jam-566c0e18c9ceb.png` like , I can automate that process through Python packages `bs4` and `selenium`.
</h6>
  
<h3>Solution at a Glance</h3>
<h6>

All the images you can download on this wibsite page, can be saved on your local computer.
</h6>

<table>
<tr>
<td>

<img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Web-Automation-Example/browser-fanart.tv.png width=400 title="fanart.tv">
</td>
<td>

<img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Web-Automation-Example/file-explorer.png width=400 title="file explorer">
</td>
</tr>
</table>

<h2>How It Works</h2>

<img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Web-Automation-Example/web-automation-example.svg width=400 title="flow chart">

<h3>Phase 1</h3>
<h6>
  
Uses `BeautifulSoup` in the `bs4` package to extract information from the fanart.tv website.
</h6>

<h3>Phase 2</h3>
<h6>
  
Uses a `webdriver` in the `selenium` package to perform browser actions like clicking and typing on the website fanart.tv. Those files are then saved to a folder, where Python renames each file according to the information extracted in Phase 1 using `BeautifulSoup`.
</h6>

<h2>Setup</h2>


<h3>File Set Up</h3>
<h6>
<ol>
<li>
  
Change the arguments of the `fanart_dl` function call in `Download Script.py` to any Movie or TV show URL within https://fanart.tv/ and title of your choosing. Note: `title` is the name that will appear on the filename.
```python
 fanart_dl("https://fanart.tv/movie/2300/space-jam/", 
          title = "Space Jam (1996)",
          )
```
</li>
</ol>
</h6>



<h3>Chromedriver Set Up</h3>
<h6>
<ol>
<li> Download the the latest version of chromedriver https://chromedriver.chromium.org/download
<ul>
<li> Dont worry even if it is the wrong version the program should tell you</li>
<li> 
Example: You currently have ChromeDriver version 87, but you need 89
  
```python
 SystemExit: Message: session not created: This version of ChromeDriver only supports Chrome version 87
Current browser version is 89.0.4389.90 with binary path C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
```
</li>
</ul>
</li>
<li> Place the driver into the same folder as `Download Script.py`
<ul>
<li> Dont worry even if it is the wrong version the program should tell you</li>
<li> 
  
```python
Message: 'chromedriver.exe' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
</li>
<li>
  
File tree look like this:
```
└── Web Automation Example
    ├── README.md
    ├── Download Script.py
    ├── chromedriver.exe
    └── requirements.txt
```
</li>
</ul>
</li>
</ol>
</h6>




<h3>Pipenv Set Up and Running</h3>
<h6>
<ol>
<li>
  
install pipenv
```
pip install pipenv
```
</li>
<li>
  
change directory to the right folder
```
cd "some\directory\Web Automation\"
```
</li>
<li>
  
install from `requirements.txt` file
```
pipenv install -r requirements.txt
```
</li>
<li>
  
open the shell
```
pipenv shell
```
</li>
<li>
  
install from `requirements.txt` file
```
pipenv "Download Script.py"
```
</li>
</ol>
</h6>
