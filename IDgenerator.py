
from PIL import Image, ImageDraw, ImageFont
img = Image.open('C:/Users/user/Documents/Untitled Folder 1/profile.PNG', 'r')
img=img.resize((128,128))

#background image(white)
background = Image.new('RGBA', (500, 300), (255, 255, 255, 255))

#for "id card"
image2 = Image.new('RGB', (500, 30), color = (0, 255, 255))
fnt = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 15)
l = ImageDraw.Draw(image2)
l.text((235,10), "ID Card", font=fnt, fill=(0, 0, 255))

#image for texts
image1 = Image.new('RGB', (400, 100), color = (255, 255, 255))
fnt = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(image1)
name=input("Enter Name: ")
dob=input("Enter Date of Birth: ")
fn=input("Enter Father's Name: ")
phn=input("Enter Form Number: ")
d.text((10,10), "Name:", font=fnt, fill=(0, 0, 255))
d.text((130,10), name, font=fnt, fill=(0, 0, 0))
d.text((10,35), "Date of birth:", font=fnt, fill=(0, 0, 255))
d.text((130,35), dob, font=fnt, fill=(0, 0, 0))
d.text((10,60), "Form No.:", font=fnt, fill=(0, 0, 255))
d.text((130,60), fn, font=fnt, fill=(0, 0, 0))
d.text((10,85), "Phone Number:", font=fnt, fill=(0, 0, 255))
d.text((130,85), phn, font=fnt, fill=(0, 0, 0))

#for logo
lgimg=Image.open('C:/Users/user/Documents/Untitled Folder 1/logo id.PNG', 'r')
lgimg=lgimg.resize((500,90))
offsetimg = (10, 130)
offsettxt = (150,130)
offsetlogo = (0,0)
offsetid=(0,90)
background.paste(img, offsetimg)
background.paste(image1,offsettxt)
background.paste(image2,offsetid)
background.paste(lgimg,offsetlogo)
background.save(name+'.png')

