from PIL import Image
import os

arr = os.listdir()
for file in arr:
 if file.startswith('ic_'):
  im = Image.open(file)
  im = im.rotate(-90)
  new_im = im.resize((128,128))
  new_im.convert('RGB').save('/opt/icons/'+file+'.jpeg')
