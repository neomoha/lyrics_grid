# -*- coding: utf-8 -*-

# This file is part of LyricsGrid.
#
# LyricsGrid is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LyricsGrid is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LyricsGrid.  If not, see <http://www.gnu.org/licenses/>.

# Written by Mohamed Sordo (@neomoha)
# Email: mohamed ^dot^ sordo ^at^ gmail ^dot^ com
# Website: http://msordo.weebly.com

import os, sys, json, codecs, argparse
from time import sleep

import config
from FlickrAPI import FlickrAPI

def get_images(lyrics_path):
    '''
    Get an image for each line of the lyrics
    '''
    api = FlickrAPI()
    lines = json.load(codecs.open(lyrics_path, "r", "utf-8"))
    keywords_images = {}
    for i in xrange(len(lines)):
        if lines[i].has_key('image'): #ignore lines with an assigned image already
            continue
        keyword = lines[i]['keyword']
        if keyword is None:
            image = "img/unknown.jpg"
            continue
        keyword = keyword[0]
        if keywords_images.has_key(keyword):
            image = keywords_images[keyword]
        else:
            try:
                sleep(1.0) #be nice
                image = api.get_images_by_tag(keyword)
            except:
                image = "img/unknown.jpg"
            keywords_images[keyword] = image
        text = lines[i]['text'].replace('[SPK]', '').replace("[/SPK]", '')
        offset = text.find(keyword)
        text = text[:offset]+"[SPK]"+keyword+'[/SPK]'+text[offset+len(keyword):]
        lines[i]['text'] = text
        lines[i]['image'] = image
    return lines
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get an image for each line of the lyrics')
    parser.add_argument('lyrics_path', help='Path to the synced lyrics file (in json format)')
    parser.add_argument('-a', '--api', nargs='?', default="flickr", help='Image API service (default=flickr)')
    args = parser.parse_args()
    if not os.path.exists(args.lyrics_path):
        print "Path to the synced lyrics not found"
        sys.exit(-1)
    if args.api != "flickr":
        print "Currently only access to Flickr API is implemented"
        sys.exit(-1)
    
    lines = get_images(args.lyrics_path)
    json.dump(lines, codecs.open(args.lyrics_path, "w", "utf-8"))
