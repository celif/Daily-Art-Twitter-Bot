#!/usr/bin/python
from ImportedLibs import *
from ArtFinder import *

class Tweeter(object):

    def setAuth(self):

        APP_KEY = 'Consumer Key'
        APP_SECRET = 'Consumer Secret'

        OAUTH_TOKEN = 'Access Token'
        OAUTH_TOKEN_SECRET = 'Access Token Secret'

        twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        return twitter
    
    def tweet_artwork(self, twitter, dict):

        IMAGE_SIZE_LIMIT = 5242880

        # Get the image from the dictionary
        artwork = requests.get(dict['artwork'])

        # Write artwork content to pictureFile
        pictureFile = BytesIO(artwork.content)

        tweetString = dict['title'] + "\nBy: " + dict['artist'] + " in " + dict['date']
        response = twitter.upload_media(media=pictureFile)

        if response['size'] > IMAGE_SIZE_LIMIT:
            return False
        else:    
            twitter.update_status(status=tweetString, media_ids=[response['media_id']])
       



if __name__ == '__main__':

    #Instantiate Tweeter and ArtFinder classes
    tweeterObject = Tweeter()
    artFinderObject = ArtFinder()
    account = tweeterObject.setAuth()

    # Tweet at 24 hour intervals
    while True:
        tweetData = artFinderObject.get_image_data()
        tweeterObject.tweet_artwork(account, tweetData)
        time.sleep(86400)
        
    
      