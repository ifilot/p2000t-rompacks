#!/usr/bin/env python

import hashlib

def main():
    pass

def main():
    create_rom('rompacks/multirom512.pck', 'MULTIROM-512KiB.BIN', 512)
    create_rom('rompacks/multirom512-release2.pck', 'MULTIROM-512KiB-RELEASE2.BIN', 512)
    create_rom('rompacks/multirom64.pck', 'MULTIROM-64KiB.BIN', 64)

    # produce 2 game packs, one with Space Fight and the other with Fraxxon
    # the latter is meant for users who have a 16 KiB memory expansion
    create_rom('rompacks/games128-01.pck', 'GAMES-128KiB.BIN', 128)
    create_rom('rompacks/games128-02.pck', 'GAMES-128KiB-ALT.BIN', 128)

    # produce a third game pack designed for a SST39SF020 ROM
    create_rom('rompacks/games256.pck', 'GAMES-256KiB.BIN', 128)

def create_rom(tplfile, outfile, romsize):
    """
    Build the multirom image
    """
    data = bytearray()

    with open(tplfile, 'r') as f:
        roms = [line.strip() for line in f.readlines()]

    for rom in roms:
        data.extend(read_rom(rom, False))

    data.extend([0x00] * (romsize * 1024 - len(data)))

    print("%s %s %i KiB" % (outfile, hashlib.md5(data).hexdigest(), len(data) / 1024))
        
    f = open(outfile, 'wb')
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