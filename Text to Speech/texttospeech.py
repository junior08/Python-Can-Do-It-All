from gtts import gTTS
import os
 

mytext = 'Intrusion alert!'

language = 'en'
 
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("intrusion.mp3")

