from PIL import Image
from PIL import ExifTags

def read_im(path):
    im=Image.open(path)
    exifDataRaw=im._getexif()
    exifData={}
    for tag, value in exifDataRaw.items():
        decodedTag = ExifTags.TAGS.get(tag, tag)
        exifData[decodedTag] = value
    return im,exifData

def test():
    path="test.jpg"
    im,exi=read_im(path)
    print(exi)

test()
