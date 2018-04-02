# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 03:12:41 2018

@author: hp
"""

#import base64
# 
#with open("words.jpg", "rb") as imageFile:
#    str = base64.b64encode(imageFile.read())
#    print (str)
#    
#fh = open("imageToSave.png", "wb")
#fh.write(str.decode('base64'))
#fh.close()

#from io import BytesIO
#from PIL import Image, ImageDraw
#
#image = Image.new("RGB", (300, 50))
#draw = ImageDraw.Draw(image)
#draw.text((0, 0), "This text is drawn on image")
#
#byte_io = BytesIO()
#
#image.save('image.png')


the_image_bytes = file("an_image.png", 'rb').read()
the_image_bytes = a_pil_image.tostring()

#a_pil_image = Image.fromstring('RGB', (300, 500), the_image_bytes)
