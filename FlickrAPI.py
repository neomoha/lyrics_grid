import flickrapi
from time import sleep

import config
from ImageWebService import ImageWebService

class FlickrAPI(ImageWebService):
    def __init__(self):
        self.api = flickrapi.FlickrAPI(config.FLICKR_KEY)
    
    def get_images_by_tag(self, tag_name):
        sleep(1.0)
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