import qrcode

# Create instance of QRCode
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border
)

# Add data to the QR code
data = "https://www.example.com"
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill="white", back_color="pink")


# Save the image
img.save("my_qrcode.png")

print("QR code saved as 'my_qrcode.png'")

from PIL import Image

# Open the image using Pillow
img = Image.open("my_qrcode.png")
img.show()  # This will open the default image viewer
