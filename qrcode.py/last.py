from tarfile import version

import qrcode
from PIL import Image
from qrcode.console_scripts import error_correction

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                border=2,)
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="blue")
img.save("my_new.png")