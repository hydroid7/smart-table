#!/bin/bash

# Upload files
source ~/pyenv/bin/activate

#rm *.mpy
#
#./micropython/mpy-cross/mpy-cross boot.py
#./micropython/mpy-cross/mpy-cross display.py
#./micropython/mpy-cross/mpy-cross main.py
#./micropython/mpy-cross/mpy-cross tableController.py
#./micropython/mpy-cross/mpy-cross web.py
for f in ./*.py
do
  ampy --port /dev/ttyUSB0 put "$f"
done
 ampy --port /dev/ttyUSB0 put ./frontend/dist/index.html


# Flash ROM
#esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 115200 erase_flash
#esptool.py --chip esp32 --port /dev/ttyUSB0  --baud 115200 write_flash -z --flash_mode dio --flash_freq 40m 0x1000 ~/Downloads/esp32-idf3-20200103-v1.12-35-g10709846f.bin
screen /dev/ttyUSB0 115200
