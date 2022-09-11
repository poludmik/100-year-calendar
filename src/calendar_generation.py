import calendar
from PIL import Image, ImageDraw, ImageFont
import ascii

counter = 0
filename = "calendar.png"
plain = calendar.TextCalendar(calendar.MONDAY)
f = ImageFont.truetype("comic.ttf", 30)
img = Image.new('RGBA', (5540, 4445), (255, 255, 255, 255))

offh = 50
offw = 20
d = ImageDraw.Draw(img)

monthcounter = 0
yearcounter = 0
rightshift = 0
downshift = 0

year_rect_color = (180, 180, 180)
year_rect_outline = (0, 0, 0)

for year in range(2000, 2100):
    if yearcounter == 10:
        downshift += 445
        rightshift = 0
        yearcounter = 0
    offh = 50
    offw = 19
    yearcounter += 1

    d.rectangle([(0 + 10 + rightshift, 6 + downshift), (560 + rightshift, 429 + downshift)], outline=(0, 0, 0), width=2)
    d.line([(0 + 10 + rightshift, 6 + downshift), (560 + rightshift, 6 + downshift)], fill=(0,0,0), width=4)
    d.line([(0 + 10 + rightshift, 429 + downshift), (560 + rightshift, 429 + downshift)], fill=(0, 0, 0), width=4)
    d.rectangle([(0 + 10 + rightshift, 6 + downshift), (560 + rightshift, 45 + downshift)], fill=(235, 235, 235), outline=(0, 0, 0), width=1)
    for month in range(1, 13):
        one_month_str = plain.formatmonth(year, month)
        # print(one_month_str)
        monthcounter += 1
        d.rectangle([(offw + rightshift - 4, offh + downshift - 2), (offw + rightshift + 122, offh + downshift + 117)], outline=(0,0,0), width=1)
        d.text((offw + rightshift, offh + downshift), one_month_str, (0, 0, 0))
        offw += 138
        if monthcounter == 4:
            monthcounter = 0
            offh += 125
            offw = 19

    d.rectangle([(238 + rightshift, 8 + downshift), (329 + rightshift, 45 + downshift)], fill=year_rect_color, outline=year_rect_outline, width=1)
    d.text((20 + 228 + rightshift, 50 - 45 + downshift), str(year), font=f, fill=(0, 20, 0))
    rightshift += 552


skull_fontsize = 20
font = ImageFont.truetype("../fonts/joystix_monospace.ttf", 50)

txt = Image.new('RGBA', img.size, (255,255,255,0))
new_layer = ImageDraw.Draw(txt)
new_layer.text((1240, 880), ascii.AsciiArts.skull, font=font, fill=(0, 0, 0, 100))
combined = Image.alpha_composite(img, txt)

combined.save('../calendar.png')