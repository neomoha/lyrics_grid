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