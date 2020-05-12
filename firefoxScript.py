# for launching new tabs in firefox
import subprocess

firefoxDirectory = r'C:\Program Files\Mozilla Firefox\firefox.exe' #directory of your browser

websiteLink1 = r'http://www.google.com/'
websiteLink2 = r'http://www.youtube.com/' #replace these with your preferred websites
websiteLink3 = r'http://www.reddit.com/'


subprocess.call([firefoxDirectory,'-new-tab', websiteLink1])
subprocess.call([firefoxDirectory,'-new-tab', websiteLink2])
subprocess.call([firefoxDirectory,'-new-tab', websiteLink3])


