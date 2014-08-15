PATH_TO_FFMPEG = "/usr/local/bin/ffmpeg" # tested in Mac OS X

PATH_TO_STANFORD_TAGGER = "tagger/stanford-postagger/stanford-postagger.jar"
PATH_TO_STANFORD_DISTSIM = "tagger/stanford-postagger/models/english-bidirectional-distsim.tagger"
POS_TAGS = { #Part of spech tags with their corresponding weight. The smaller the weight, the more important the tag is for this hack.
    'NN': 1,
    'NNP': 1,
    'NNS': 1,
    'JJ': 2,
    'JJR': 2,
    'VBG': 3,
    'VBN': 3,
    'VB': 3
}

FLICKR_KEY = u"YOUR_FLICKR_API_KEY"

MUSIXMATCH_KEY = "YOUR_MUSIXMATCH_API_KEY"