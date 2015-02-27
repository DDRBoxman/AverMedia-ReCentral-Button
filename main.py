import hid

if not hid.enumerate(0x07ca, 0x9850):
    raise IOError("No button connected")

device = hid.device(0x07ca, 0x9850)



result = list()
size = 23
while size > 0:
    count = min(size, 8)
    buf = device.read(count)
    if len(buf) < count:
        raise IOError(
            'pywws.device_cython_hidapi.USBDevice.read_data failed')
    result += buf
    size -= count
print result

buf = [0x01]

if device.write(buf) != len(buf):
        raise IOError(
            'pywws.device_cython_hidapi.USBDevice.write_data failed')