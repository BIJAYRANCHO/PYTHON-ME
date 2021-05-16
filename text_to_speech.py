from gtts import gTTS
import os

# myText="Bijay Ghosh"
fh = open("test.txt", "r")
myText = fh.read().replace("\n"," ") 
#this above line will replace all the line endings with space.
language ='en'
#have to give which language format is going to speak out

output = gTTS(text=myText, lang=language, slow= False)
#gTTs funtion will read the text document and speak fast.

#output will be saved as xyz.mp3 file in folder 
output.save("xyz.mp3")
#text file will be close 
fh.close()
#bu default media player the xyz.mp3 file will be played.
os.system("start xyz.mp3")