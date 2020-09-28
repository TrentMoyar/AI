import PIL
from PIL import Image

print (PIL.PILLOW_VERSION)

import urllib.request
import io
URL = 'http://www.w3schools.com/css/trolltunga.jpg'
f = io.BytesIO(urllib.request.urlopen(URL).read())

img = Image.open(f)
img.show()
img = Image.open(f)
print(img.size)
pix = img.load()
print(pix[2,5])

bottom = 255//3
top = (255*2)//3
for x in range(img.size[0]):
   for y in range(img.size[1]):
      temp = []
      for val in range(len(pix[x,y])):
         if pix[x,y][val] <= bottom:
            temp.append(0)
         elif pix[x,y][val] >= top:
            temp.append(255)
         else:
            temp.append(127)

      pix[x,y] = (temp[0], temp[1], temp[2])
img.show()


      