import requests
import urllib
from playsound import playsound

//your audio type goes here:
headers = {'accept': 'audio/mp3'}

print "Speech to text !\n"
i=0

while True:
	msg = raw_input("> ")
  //
	url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?' + urllib.urlencode({'voice': 'fr-FR_ReneeVoice', 'text': msg})
	r = requests.get(url, auth=('7ffeeb09-cc81-4908-87ca-3707e7030e00', 'cDDMvWwBSlBq'), headers=headers)
	with open('./rsc/audio'+str(i)+'.mp3', 'wb') as f:
		for x in r.iter_content(1024):
			f.write(x)
	playsound('./rsc/audio'+str(i)+'.mp3')
	i+=1

