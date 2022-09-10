import calendar
from PIL import Image, ImageDraw, ImageFont

counter = 0
filename = "calendar.png"
plain = calendar.TextCalendar(calendar.MONDAY)
img = Image.new('RGB', (6000, 5000), (230, 230, 230))

offh = 50
offw = 20
d = ImageDraw.Draw(img)

monthcounter = 0
yearcounter = 0
rightshift = 0
downshift = 0

year_rect_color = (150, 150, 150)
year_rect_outline = (0, 0, 0)

for year in range(2000, 2100):
    if yearcounter == 10:
        downshift += 445
        rightshift = 0
        yearcounter = 0
    offh = 50
    offw = 20
    yearcounter += 1

    d.rectangle([(0 + 10 + rightshift, 0 + downshift), (560 + rightshift, 429 + downshift)], outline=(0, 0, 0), width=1)

    for month in range(1, 13):
        str1 = plain.formatmonth(year, month)
        # print(str1)
        monthcounter += 1
        d.text((offw + rightshift, offh + downshift), str1, (0, 0, 0))
        offw += 138
        if monthcounter == 4:
            monthcounter = 0
            offh += 125
            offw = 20

    f = ImageFont.truetype("comic.ttf", 30)

    d.rectangle([(240 + rightshift, 8 + downshift), (330 + rightshift, 45 + downshift)], fill=year_rect_color, outline=year_rect_outline, width=1)
    d.text((20 + 228 + rightshift, 50 - 45 + downshift), str(year), font=f, fill=(0, 20, 0))
    rightshift += 552

img.save('calendar.png')