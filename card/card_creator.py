# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(__file__)

# load templates
switch_down = Image.open(os.path.join(ROOT, 'switch_down.png'))
switch_down.thumbnail((int(111/2), int(287/2)))
switch_up = Image.open(os.path.join(ROOT, 'switch_up.png'))
switch_up.thumbnail((int(111/2), int(287/2)))

# create new image
card = Image.new(mode="RGBA", size=(3500, 2800), color=(255,255,255,00))

# specify tags
GAME = 1
EXROM = 2
ROML = 4
ROMH = 8

titles = {
    "roms/BASICNL1.1.bin" : "BASIC NL v1.1",
    "roms/BASICNL1.1A2.bin" : "BASIC NL v1.1a2",
    "roms/BASICNL1.0.bin" : "BASIC EN v1.0",
    "roms/JWSBasic.bin" : "JWS Basic",
    "roms/BASICBOOTSTRAP.BIN" : "SD-CARD Launcher",
    "roms/FLASHER.BIN" : "SD-CARD Flasher",
    "roms/RAMTEST.BIN" : "RAM test",
    "roms/Maintenance 2.bin" : "Philips Maintenance",
    "roms/Forth.bin" : "Forth",
    "roms/assembler 5.9.bin" : "Assembler 5.9",
    "roms/Zemon 1.4.bin" : "Zemon 1.4",
    "roms/flexbase1_6.bin" : "Flexbase 1.6",
    "roms/familiegeheugen 4.bin" : "Familiegeheugen v4",
    "roms/tekst 1.bin" : "Tekst 1.0",
    "roms/Text2000 3.bin" : "Tekst 2000 v3",
    "roms/TEXT2_DE.bin" : "Text2 DE",
    "roms/WordProcessor 2.bin" : "WordProcessor v2",
    "roms/games/Brick-Wall.bin" : "Brick Wall",
    "roms/games/Doolhof.bin" : "Doolhof",
    "roms/games/Fraxxon (joystick).bin" : "Fraxxon",
    "roms/games/Ghosthunt.bin" : "Ghosthunt",
    "roms/games/Lazy Bug.bin" : "Lazy Bug",
    "roms/games/Monkey Kong.bin" : "Monkey Kong",
    "roms/games/Multipede.bin" : "Multipede",
    "roms/games/Space Fight.bin" : "Space Fight",
    "roms/games/Tetris.bin" : "Tetris",
}

with open(os.path.join(ROOT, '..', 'rompacks', 'multirom512.pck'), 'r') as f:
    data = [titles[c.strip()] for c in f.readlines()]

# specify font
fnt = ImageFont.truetype(os.path.join(ROOT, 'OpenSans-ExtraBold.ttf'), 78)
d = ImageDraw.Draw(card)

# specify break point
breakpt = 20

pos = 0
ypos = 100
xpos = 100
cnt = 0
for i,label in enumerate(data):
    switch = format(i, '#07b')
    print("%30s %s" % (label, switch))
    d.text((xpos,ypos+15), label, font=fnt, fill=(0,0,0))
        
    # draw dipswitch box    
    xpos += 1000   
    d.rectangle((xpos-20, ypos-20, xpos+380, ypos+175), fill=(240,30,30), outline=(0,0,0), width=5)
    
    for s in switch[2:]:
        if s == "1":
            card.paste(switch_up, (xpos, ypos))
            xpos += 75
        else:
            card.paste(switch_down, (xpos, ypos))
            xpos += 75
    
    if i == 12:
        ypos = 100
    else:
        ypos += 200
        
    if i >= 12:
        xpos = 1800
    else:
        xpos = 100

#card.show()
card.save('card.png')