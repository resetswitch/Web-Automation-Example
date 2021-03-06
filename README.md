<h1> Web-Automation-Example</h1>

<h4>Scenario</h4>
<h6>
  
You love a TV or Movie so much, you would like to download a bunch of related images. You find a website called <a href=fanart.tv>fanart.tv</a>. You search up your favorite TV or Movie, but you have to click the `Save` button below each of the images. They save as under some unpleasant name like `space-jam-566c0e18c9ceb.png`
</h6>

<h4>Solution</h4>
<h6>
  
Automate that process through Python packages `bs4` and `selenium`.
</h6>
  
<h4>Solution at a Glance</h4>
<h6>

All the images you can download on this website page, can be saved on your local computer via web automation.
<ul>
<li>

Image Left: Website containing image download buttons. Explore this example website yourself: <a href='https://fanart.tv/movie/2300/space-jam/'>https://fanart.tv/movie/2300/space-jam/</a>
</li>
<li>
 
Image Right: The files saved in file explorer via web automation.
</li>
</ul>
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

<h4>Phase 1</h4>
<h6>
  
Uses `BeautifulSoup` in the `bs4` package to extract information from the fanart.tv website.
</h6>

<h4>Phase 2</h4>
<h6>
  
Uses a `webdriver` in the `selenium` package to perform browser actions like clicking and typing on the website fanart.tv. Those files are then saved to a folder, where Python renames each file according to the information extracted in Phase 1 using `BeautifulSoup`.
</h6>

<h2>Setup</h2>


<h4>File Set Up</h4>
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



<h4>Chrome and Chromedriver Set Up</h4>
<h6>
<ol>
<li> If you havent already, download Chrome: <a href='https://www.google.com/chrome/'> https://www.google.com/chrome/<a>
<li> Download the the latest version of chromedriver: <a href='https://chromedriver.chromium.org/download'> https://chromedriver.chromium.org/download<a>
<ul>
<li> Dont worry! Even if it is the wrong version the program should tell you</li>
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
<li> Dont worry! Even if it is the wrong version the program should tell you</li>
<li> 
  
```python
 SystemExit: Message: 'chromedriver.exe' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
</li>
<li>
  
File tree should look like this:
```
????????? Web Automation Example
    ????????? README.md
    ????????? Download Script.py
    ????????? chromedriver.exe
    ????????? requirements.txt
```
</li>
</ul>
</li>
</ol>
</h6>




<h4>Pipenv Set Up and Running</h4>
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
  
run the `Download Script.py` file
```
pipenv "Download Script.py"
```
</li>
</ol>
</h6>
