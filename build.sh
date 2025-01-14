#/bin/bash

set -e  # Exit on error

# clean up any existing folders
rm -rf roms

# grab ROMS from internet
wget https://github.com/p2000t/software/archive/refs/heads/main.zip -O repository.zip
unzip -o repository.zip
mv software-main/cartridges ./roms
rm -rf software-main

# grab basic bootstrap
wget https://github.com/ifilot/p2000t-sdcard/releases/download/latest-stable/BASICBOOTSTRAP.BIN -O roms/BASICBOOTSTRAP.BIN

# grab flasher
wget https://github.com/ifilot/p2000t-sdcard/releases/download/latest-stable/FLASHER.BIN -O roms/FLASHER.BIN

# grab basic bootstrap - release 2
wget https://github.com/ifilot/p2000t-sdcard/releases/download/release-2.x/BASICBOOTSTRAP.BIN -O roms/BASICBOOTSTRAP_RELEASE2.BIN

# grab flasher - release 2
wget https://github.com/ifilot/p2000t-sdcard/releases/download/release-2.x/FLASHER.BIN -O roms/FLASHER_RELEASE2.BIN

# grab RAM tester
wget https://github.com/ifilot/p2000t-ram-expansion-board/releases/latest/download/RAMTEST.BIN -O roms/RAMTEST.BIN

# run build_rom.py
python3 build_rom.py

# clean up
rm -rf roms