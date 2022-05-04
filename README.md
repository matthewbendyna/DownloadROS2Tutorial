# DownloadROS2Tutorial

#This is a python script that uses selenium automation to download the entire tutorial for ROS2 Galactic from the website by
#crawling through free web tutorials and copying the HTML code into a text file in a directory on your PC. This provides you
#with a convenient way to download the official tutorials on your computer instead of copying and pasting text. Reduces
#a task that would ordinarily take a up to an hour or more to a minute.

#Prerequisites
#All you need is Python working on your pc, Google Chrome, and Chromedriver on your system path and selenium and pathlib installed via pip. pathlib may be installed on your system by default, but I'd make sure. Obviously you'll need to have an active internet connection when you run this automation

#After running the script, a CLI will open asking you to paste or type in the path of the existing directory on your PC where you would like to install the tutorial. I wrote and ran this on a Ubuntu system so the path will be typed something like "/home/user/Documents" but if you're on Windows then your path may look more like "C:\\users\\user\\Documents". It helps to understand how the os module in Python handles files in your OS.

If you've downloaded the tutorial in the chosen directory before, you'll be prompted with a question asking you if you want to delete and reinstall. This could be good if you've accidentally deleted or corrupted data and wish to recover 

Ideally, you should make sure your chromedriver copy is on system path, but if it's not, then you will be prompted to ensure Chrome and chromedriver.exe are installed and to type in the path to the chromedriver executable file, so it being on PATH is not an absolute requirement (it is needed to use Selenium to scrape Chrome however)

If all is well, you will see Chrome open up and the program will automatically sift through a bunch of web pages extremely quickly. It's important that you don't interfere with this process by closing the browser or clicking on any links or buttons on the window while the process is running, or you may corrupt data. Just let the bot do it's work.

After the bot is done, the browser will close and you should have the ROS2 Galactic Tutorial availabe on your PC offline. Follow the instructions of the CLI and open the first tutorial in a web browser (HTML documents open web pages, although the source code may not have all of the CSS styling of the online page

The online tutorials for ROS2 are here: https://docs.ros.org/en/galactic/Tutorials.html
If you are interested in learning web scraping to write programs like this, here is a good tutorial on that: http://automatetheboringstuff.com/2e/chapter12/
