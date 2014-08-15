import json, os, codecs, argparse
import pydub

import config
pydub.AudioSegment.ffmpeg = config.PATH_TO_FFMPEG

def split_audio(audio_path, lyrics_path):
    if not os.path.exists("snippets"):
        os.mkdir("snippets")
    lines = json.load(codecs.open(lyrics_path, "r", "utf-8"))
    suffix = audio_path[audio_path.rfind("/")+1:audio_path.rfind(".mp3")] # TODO: find a better way to ID the song
    if not os.path.exists("snippets/"+suffix):
        os.mkdir("snippets/"+suffix)
        song = pydub.AudioSegment.from_mp3(audio_path)
        for i in range(len(lines)):
            s = song[lines[i]['begin_time']:lines[i]['end_time']]
            print s.duration_seconds
            s.export("snippets/%s/%s_%s.mp3" % (suffix, lines[i]['begin_time'], lines[i]['end_time']), format="mp3")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split the audio file in chunks given the timestamps from the synced lyrics')
    parser.add_argument('audio_path', help='Path to the mp3 file of the song')
    parser.add_argument('lyrics_path', help='Path to the synced lyrics file (in json format)')
    args = parser.parse_args()
    if not os.path.exists(args.audio_path):
        print "Path to the song not found"
        sys.exit(-1)
    if not os.path.exists(args.lyrics_path):
        print "Path to the synced lyrics not found"
        sys.exit(-1)
    split_audio(args.audio_path, args.lyrics_path)