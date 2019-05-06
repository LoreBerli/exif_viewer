import im_model
import os

modes=["STD","COMPARE"]

class State:
    def __init__(self):
        self.cwd=os.getcwd()
        self.counter=0
        self.current_img=im_model.Img()
        self.other_img=im_model.Img()
        self.mode="STD"
        self.info=self.current_img.exif
        self.must_update=True
    def get_diff(self):
        diffs=[]
        for k in self.other_img.exif.keys():
            if(k not in self.current_img.exif.keys()):
                diffs.append(k)
            else:
                if(self.other_img.exif[k]!=self.current_img.exif[k]):
                    diffs.append(k)
        return diffs

    def change_current(self,new_one):
        self.current_img=im_model.Img(new_one)
        self.must_update=True
    def change_other(self,new_one):
        self.must_update = True
        self.other_img=new_one
    def slide(self,new_one):
        self.change_other(self.current_img)
        self.change_current(new_one)
    def roll(self,cnt):
        self.counter += cnt
        self.must_update = True
        self.ims =[d for d in os.listdir(self.cwd) if d.endswith(".jpg")]
        self.slide(self.cwd+self.ims[self.counter%len(self.ims)])

