import qrcode
from pyzbar import pyzbar
from PIL import Image


def generate_qr_simple(data, args=None):
    qr_code = qrcode.make(data)
    qr_code.save("test.png")

def decode_qr(img_path):
    with Image.open(img_path) as img:
        qr_code = pyzbar.decode(img)
    return qr_code[0].data.decode("utf-8")
    
generate_qr_simple("Gosig Golden ist süß!")
print(decode_qr("test.png"))
