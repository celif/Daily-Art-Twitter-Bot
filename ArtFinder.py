#!/usr/bin/python
from ImportedLibs import *

class ArtFinder():

    def get_image_data(self):

        rijksmuseumKey = 'Rijksmuseum API Key'
        artworkLink = 'https://www.rijksmuseum.nl/api/en/collection/q?key=myKey&format=json'

        while True:

            # Generate random number to concatenate to itemNumber
            objectNumGenerator = random.randint(2,5000)
            itemNumber = 'SK-A-' + str(objectNumGenerator)

            imageLink = artworkLink.replace('q', itemNumber).replace('myKey', rijksmuseumKey)

            # Create response object and decode the JSON data
            myRequest = requests.get(imageLink)
            urlJSON = myRequest.json()
            processedData = json.dumps(urlJSON)

            # Load the processed JSON data into imageDir
            imageData = json.loads(processedData)
            imageDir = imageData['artObject']

            # Check if there is a valid image in imageDir
            if imageDir is not None:
                if imageDir['webImage'] is not None:
                    break

        # Create a dictionary of image attributes
        imageDict = {
            'artwork':imageDir['webImage']['url'], 
            'title':imageDir['title'],
            'artist':imageDir['principalMaker'],
            'date':imageDir['dating']['presentingDate']
        }
        
        return imageDict
    
