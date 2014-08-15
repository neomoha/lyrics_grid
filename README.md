Scapelist
======

Source code of [LyricsGrid](http://searchsounds.upf.edu/lyrics_grid/), a hack developed at the [Paris Music Hack Day 2014](http://new.musichackday.org/2014/paris/)

The hack allows to visualize and interact with a song using the content of its lyrics.

For each line of the lyrics, the most salient word is selected (using Natural Language Processing techniques) and used as a tag to query Flickr for an image.

The resulting images are then visualized as an NxN grid.

The user can then move his/her mouse over the images, which will display the corresponding lyrics line, and play the audio snippet that corresponds to that line, thanks to the synchronized lyrics provided by MusixMatch API.

More info [here](https://www.hackerleague.org/hackathons/music-hack-day-paris-number-2/hacks/lyricsgrid-and-thisdayinplaylist)

Install Dependencies
------

(preferably in a virtualenv)

Run: 'pip install -r requirements'

You must also install [ffmpeg](https://www.ffmpeg.org/download.html).

Configurations
------

You need an API key for both [Flickr](https://www.flickr.com/services/api/misc.api_keys.html) and [MusixMatch](https://developer.musixmatch.com/).

Modify the content in _config.py_ accordingly.

The Stanford NLP tagger is the default Part-of-Speech tagger. For ease of use, it is also included in this repo.

How to deploy the hack (backend)
------

Run in this order:

* python get_lyrics.py ARTIST_NAME SONG_TITLE PATH_TO_AUDIO.mp3
* python split_audio.py PATH_TO_AUDIO.mp3 PATH_TO_LYRICS.json
* python get_images.py PATH_TO_LYRICS.json

All the above scripts have a help text (run for example 'python get_lyrics.py -h' to see the help text)

For ease of use, this repository includes the synced lyrics and images of 5 songs. The audio files though cannot be shared because of copyright issues. 

How to deploy the hack (frontend)
------
An easy way to deploy the frontend part of the hack using Linux or Mac OS X from the command line:

* cd web/
* python -m SimpleHTTPServer 8080

Then go to your browser and type 0.0.0.0:8080


