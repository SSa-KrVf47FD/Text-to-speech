import requests
import urllib
from playsound import playsound



print "Text to speech !\n"
i=0

# audio file extension goes here:
headers = {'accept': 'audio/mp3'}

while True:

        # text to be converted to speech goes here:
	msg = raw_input("> ")
	
        # French female voice is specified in this case.
        # For more informations about available voices refer to
        # https://www.ibm.com/watson/developercloud/text-to-speech/api/v1/
	url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?' + urllib.urlencode(
                {
                        'voice': 'fr-FR_ReneeVoice',
                        'text': msg
                })

	# You authenticate to the Text to Speech API by providing the username and password that are
	# provided in the service credentials for the service instance that you want to use(text to
	# speech in this case).
	r = requests.get(       url,\
                                auth = ('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'xxxxxxxxxxxx'),\
                                headers = headers )

	# audio is downloaded and saved to 'audioX.mp3' where X is an automatically incremented index
	# audios are saved in rsc for eventual later use
	with open('./rsc/audio'+str(i)+'.mp3', 'wb') as f:
		for x in r.iter_content(1024):
			f.write(x)
			
	# audio is played automatically after download
	playsound('./rsc/audio'+str(i)+'.mp3')
	
	i+=1

