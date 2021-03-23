<h1> Web-Automation-Example</h1>

<h2>Setup</h2>

<h3>File Set Up</h3>
<h6>
<ol>
<li>
  
Change the arguments of the `fanart_dl` function call in `Download Script.py` to the website and title of your choosing
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
