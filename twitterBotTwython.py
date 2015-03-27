from twython import Twython, TwythonError
import time

APP_KEY = 'PxetbkMABDLQQEk73X8JeUWNR'
APP_SECRET = 'OVeD2gxRrVOjQipJR1q53a1nVuvoAW92kH1Cc60KhOvujGtkVu'
OAUTH_TOKEN = '188006425-E8FeoYqqdEH9pi8DK5N63xbHi38Isn1yAUxnS7At'
OAUTH_TOKEN_SECRET = '8E9XbL0vnlknwCsW8UUUpYW3ttoQD0KYk6cbw0ybjxi2t'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	with open('botLines.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	for line in buff[:]:
		line = line.strip(r'\n')
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			with open ('botLines.txt', 'w') as tweetfile:
				buff.remove(line)
				tweetfile.writelines(buff)
			time.sleep(1800)
		else:
			with open ('botLines.txt', 'w') as tweetfile:
				buff.remove(line)
				tweetfile.writelines(buff)
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...")


except TwythonError as e:
	print (e)