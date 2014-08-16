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

import flickrapi

import config
from ImageWebService import ImageWebService

class FlickrAPI(ImageWebService):
    def __init__(self):
        self.api = flickrapi.FlickrAPI(config.FLICKR_KEY)
    
    def get_images_by_tag(self, tag_name):
        for photo in self.api.walk(tags=tag_name):
            print photo
            break
        if photo is not None:
            sizes = self.api.photos_getSizes(photo_id=photo.get('id'))
            for esizes in sizes: 
                for size in esizes:
                    if size.get('label') == 'Medium':
                        return size.get('source')
        return "img/unknown.jpg"