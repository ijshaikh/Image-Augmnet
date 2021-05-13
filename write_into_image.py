

from PIL import Image, ImageDraw, ImageFont
import os
import time

globalname = ''

def generateTime():
    return str(time.time()).replace(".","")

dix = {1 : 'eid1.jpg',
       2 : 'eid2.jpg',
       3 : 'eid3.jpg',
       4 : 'eid4.jpg',
       5 : 'eid5.jpg'}



def save_edit(x, y, font,fill,sw,text , im):
    d1 = ImageDraw.Draw(im)
    d1.text((x, y), text, font = font, stroke_width= sw, fill=fill)
    # im.show()
    image_path = "created/eid_"+globalname.replace(' ','_')+generateTime()+".jpg"
    im.save(image_path)
    return image_path




def ImageGenerator(select, name):
    global globalname
    globalname = name
    path = ''
    if select == 1:
        text = "From: "+name
        im = Image.open('blank/'+dix[select])
        x,y = 350, 325
        font = ImageFont.truetype("Fonts/ITCEDSCR.TTF", size=44)
        fill = (255,255,255)
        sw = 1
        path = save_edit(x,y,font,fill,sw, text , im)
    elif select == 2:
        text = "From: "+name
        im = Image.open('blank/'+dix[select])
        x,y = 340, 290
        font = ImageFont.truetype("Fonts/century_norm.ttf", size=22)
        fill = (255,255,255)
        sw = 0
        path = save_edit(x,y,font,fill,sw,text , im)
    elif select == 3:
        text = "From: "+name
        im = Image.open('blank/'+dix[select])
        x,y = 360, 250
        font = ImageFont.truetype("Fonts/pierre.otf", size=36)
        fill = (30,30,30)
        sw = 0
        path = save_edit(x,y,font,fill,sw,text , im)
    elif select == 4:
        text = "From: "+name
        im = Image.open('blank/'+dix[select])
        x,y = 40, 320
        font = ImageFont.truetype("Fonts/garamond.ttf", size=32)
        fill = (0, 204, 204)
        sw = 0
        path = save_edit(x,y,font,fill,sw,text , im)
    elif select == 5:
        text = "From: \n"+name
        im = Image.open('blank/'+dix[select])
        x,y = 35, 40
        font = ImageFont.truetype("Fonts/philosopher-regular.ttf", size=44)
        fill = (255, 255, 255)
        sw = 0
        path = save_edit(x,y,font,fill,sw,text , im)
    return path
    


# select = int(input("Enter Image number "))
# name = input("Enter your name")
#
# print(ImageGenerator(select,name))
