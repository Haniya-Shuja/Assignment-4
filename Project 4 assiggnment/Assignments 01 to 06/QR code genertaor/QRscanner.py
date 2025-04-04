#import module

import qrcode
data = 'QR code make () function'
img = qrcode.make(data)
img.save(' qr code project 7.png')