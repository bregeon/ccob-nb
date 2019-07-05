#!/bin/env python3
# define FTDI_OMNI1509			0xD491	/* Omni1509 embedded USB-serial */
# vendor: 0403 ("Future Technology Devices International, Ltd"), product: d491 ("Zolix Omni 1509 monochromator")

import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0403, idProduct=0xD491)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')


# dev.bLength
# dev.bNumConfigurations
# dev.bDeviceClass


# msg = 'test'
# assert dev.ctrl_transfer(0x40, CTRL_LOOPBACK_WRITE, 0, 0, msg) == len(msg)
# ret = dev.ctrl_transfer(0xC0, CTRL_LOOPBACK_READ, 0, 0, len(msg))
# sret = ''.join([chr(x) for x in ret])
# assert sret == msg

# msg = 'test'
# assert len(dev.write(1, msg, 100)) == len(msg)
# ret = dev.read(0x81, len(msg), 100)
# sret = ''.join([chr(x) for x in ret])
# assert sret == msg
