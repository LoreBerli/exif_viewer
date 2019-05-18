from PIL import Image
from PIL import ExifTags

undecodable=["MakerNote","UserComment","FileSource"]
special_cases=["FileSource"]

class Img:
    def read_im(self,path):
        im = Image.open(path)
        exifDataRaw = im._getexif()
        exifData = {}
        if(exifDataRaw!=None):
            for tag, value in exifDataRaw.items():
                decodedTag = ExifTags.TAGS.get(tag, tag)
                if(decodedTag not in undecodable):
                    if(decodedTag in special_cases):
                        exifData[decodedTag] = self.decode(value,decodedTag)
                    else:
                        exifData[decodedTag] = value
        gps= exifData["GPSInfo"]
        for k in gps.keys():
            exifData[ExifTags.GPSTAGS[k]]= gps[k]
        #exifData.


        else:
            exifData["None"]="None"
        return im, exifData
    def decode(self,val,tag):
        if(tag==special_cases[0]):
            return dic[str(val)]




    def __init__(self,path=None):
        if(path!=None):
            self.path=path
            print("path:", self.path)
            self.im,self.exif = self.read_im(path)
        else:
            self.path=""
            self.im=None
            self.exif={"None":"None"}
dic={"b'\\x01'": "Film Scanner","b'\\x02'" : "Reflection Print Scanner","b'\\x03'" : "Digital Camera","b'\\x03\x00\x00\x00'" : "Sigma DigitalCamera"}
def test():
    impath="/home/cioni/material_exif/exif_viewer/DSCN0021.jpg"
    im=Img(impath)
    text=im.exif

test()
