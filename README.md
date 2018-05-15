# Daily Art Twitter Bot
Automatically tweet paintings from the Rijksmuseum in 24-hour intervals. Fully written in Python, this bot makes use of the Twython API and the Rijksmuseum API. Artwork information like title, artist, and publishing date is obtained as JSON from the Rijksstudio database. Pieces of artwork tweeted by this bot are all available on the Rijksmuseum website.

## Requirements

- Twython API (version 3.6.0 is used in this application)
- Rijksmuseum account (for obtaining the API key)
- Twitter account and application authentication keys (consumer key, consumer key secret, access token, and
   access token secret)
- Rijksmuseum API key (under advanced settings on user account page)

## Usage

Once a Twitter application has been created and the Rijksmuseum API key and Twitter authentication
keys are provided in ArtFinder.py and Tweeter.py, respectively, the program can be run. Assuming
Python 3 is already installed, simply run the following commands on the respective operating 
system.

Mac OS X & Linux:
```
$ python tweeter.py
```

Windows:
```
 C:/PATH/python tweeter.py
```
## License

This project is licensed under the MIT License - see the LICENSE.md file for details
