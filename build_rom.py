#!/usr/bin/env python

def main():
    pass

def main():
    create_rom_default()

def create_rom_default():
    """
    Build the multirom image
    """
    data = bytearray()

    datalist = [
        'roms/BASICNL1.1.bin',        # regular BASIC NL v1.1    (00)
        'roms/BASICNL1.1A2.bin',      # regular BASIC NL v1.1a2  (01)
        'roms/BASICNL1.0.bin',        # regular BASIC EN v1.1a2  (02)
        'roms/JWSBasic.bin',          # JWS Basic                (03)
        'roms/BASICBOOTSTRAP.BIN',    # SD-CARD BASIC            (04)
        'roms/FLASHER.BIN',           # flasher utility          (05)
        'roms/RAMTEST.BIN',           # ram test                 (06)
        'roms/Maintenance 2.bin',     # maintenance utility      (07)
        'roms/Forth.bin',             # Forth programming lang   (08)
        'roms/assembler 5.9.bin',     # Assembler 5.9            (09)
        'roms/Zemon 1.4.bin',         # Zemon v1.4               (0A)
        'roms/flexbase1_6.bin',       # Flexbase v1.6            (0B) 
        'roms/familiegeheugen 4.bin', # Familiegeheugen v4       (0C)
        'roms/tekst 1.bin',           # Tekst v1                 (0D)
        'roms/Text2000 3.bin',        # Text2000 v3              (0E)
        'roms/TEXT2_DE.bin',          # Text2 DE v2              (0F)
        'roms/WordProcessor 2.bin',   # Wordproc v2              (10)
        'roms/games/Brick-Wall.bin',
        'roms/games/Doolhof.bin',
        'roms/games/Lazy Bug.bin',
        'roms/games/Monkey Kong.bin',
        'roms/games/Multipede.bin',
        'roms/games/Space Fight.bin',
        'roms/games/Tetris.bin'
    ]

    for rom in datalist:
        data.extend(read_rom(rom, False))

    data.extend([0x00] * (512 * 1024 - len(data)))

    print(len(data) / 1024)
        
    f = open('MULTIROM-512KiB.BIN', 'wb')
    f.write(data)
    f.close()

def read_rom(filename, swap=False):
    """
    Read a ROM file from BIN file and automatically expand it to 16KiB
    """
    f = open(filename, 'rb')
    data = bytearray(f.read())
    data.extend([0x00] * (0x4000 - len(data)))
    
    # swap upper and lower halfs
    if swap:
        dataswapped = data[0x2000:0x4000]
        dataswapped.extend(data[0x0000:0x2000])
        data = dataswapped
       
    f.close()
    return data

if __name__ == '__main__':
    main()