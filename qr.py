import qrcode

img = qrcode.make("https://github.com/ivana-christ/")
img.save("qr.png", "PNG")