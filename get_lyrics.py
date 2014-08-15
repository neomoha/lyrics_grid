import urllib2, json, os, sys, codecs, argparse
from urllib import quote
from mutagen.mp3 import MP3
import nltk
from nltk.tag.stanford import POSTagger, NERTagger

import config

STANFORD_POS_TAG = POSTagger(config.PATH_TO_STANFORD_DISTSIM, config.PATH_TO_STANFORD_TAGGER)

def incr():
    i = 0
    while True:
        yield i
        i += 1

def get_synced_lyrics(track_artist, track_title, audio_path):
    '''
    Get synced lyrics (i.e., (with the audio timestamps) from MusixMatch
    '''
    audio = MP3(audio_path)
    url = "http://api.musixmatch.com/ws/1.1/matcher.subtitle.get?apikey=" + config.MUSIXMATCH_KEY
    url += "&q_track=" + quote(track_title)
    url += "&q_artist=" + quote(track_artist)
    url += "&f_subtitle_length=" + str(int(audio.info.length))
    url += "&format=json&f_subtitle_length_max_deviation=10&subtitle_format=mxm"
    print url
    data = json.load(urllib2.urlopen(url))
    synced_lyrics = []
    if data['message']['header']['status_code'] == 200:
        synced_lyrics = eval(data['message']['body']['subtitle']['subtitle_body'])
    return synced_lyrics

def select_keyword(tokens):
    '''
    Select the best candidate term to be the most representative word from the lyrics line
    '''
    idx = incr()
    pos_tags = [(t, config.POS_TAGS[t[1]], idx.next()) for t in STANFORD_POS_TAG.tag(tokens) if t[1] in config.POS_TAGS]
    if len(pos_tags) == 0:
        return None
    pos_tags = sorted(pos_tags, key=lambda x: (x[1], -x[2]))
    return pos_tags[0][0]

def process_lyrics(synced_lyrics):
    '''
    Get the most representative word for each line in the lyrics
    '''
    lines = []
    for i in range(len(synced_lyrics)):
        begin_time = int(synced_lyrics[i]['time']['total']*1000)
        end_time = None
        if i < len(synced_lyrics)-1:
            end_time = int(synced_lyrics[i+1]['time']['total']*1000)
        print begin_time, end_time
        tokens = nltk.word_tokenize(synced_lyrics[i]['text'])
        keyword = select_keyword(tokens)
        lines.append({'begin_time': begin_time, 'end_time': end_time, 'keyword': keyword, 'text':synced_lyrics[i]['text']})
        print "----------------"
    return lines
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the lyrics of a given song')
    parser.add_argument('artist', help='Song artist (use quotes for artist names with more than one word)')
    parser.add_argument('title', help='Song title (use quotes for song titles with more than one word)')
    parser.add_argument('path', help='Path to the mp3 file of the song')
    args = parser.parse_args()
    print args
    if not os.path.exists(args.path):
        print "Path not found"
        sys.exit(-1)
    synced_lyrics = get_synced_lyrics(args.artist, args.title, args.path)
    print synced_lyrics
    lines = process_lyrics(synced_lyrics)
    if not os.path.exists("json/"):
        os.mkdir("json")
    suffix = args.path[args.path.rfind("/")+1:args.path.rfind(".mp3")] # TODO: find a better way to get an ID for the song
    json.dump(lines, codecs.open("json/%s.json" % suffix, "w", "utf-8"))
    print lines
    sys.exit()
