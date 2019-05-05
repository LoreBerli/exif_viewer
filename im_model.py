from PIL import Image
from PIL import ExifTags

class Img:
    def read_im(self,path):
        im = Image.open(path)
        exifDataRaw = im._getexif()
        exifData = {}
        if(exifDataRaw!=None):
            for tag, value in exifDataRaw.items():
                decodedTag = ExifTags.TAGS.get(tag, tag)
                exifData[decodedTag] = value
        else:
            exifData["None"]="None"
        return im, exifData

    def __init__(self,path=None):
        if(path!=None):
            self.path=path
            print("path:", self.path)
            self.im,self.exif = self.read_im(path)
        else:
            self.path=""
            self.im=None
            self.exif={"None":"None"}



