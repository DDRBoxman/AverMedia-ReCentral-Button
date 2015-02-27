import usb.core
import usb.util
import sys


dev = usb.core.find(idVendor=0x07ca, idProduct=0x9850)  # fill in your own device, of course

print dev
