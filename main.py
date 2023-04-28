import qrcode

import image

qr=qrcode.QRCode(version=15,box_size=10,border=5)#version means the size of image and its complexity of image

data="https://www.google.co.in/?client=safari&channel=mac_bm"

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill="black",back_color="white")

img.save("Qrcode.png")

