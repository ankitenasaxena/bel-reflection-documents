# pip install "qrcode[pil]"
import qrcode

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=20,   # pixels per module → controls output size
    border=4,      # the quiet zone, keep at 4 minimum
)
qr.add_data("https://tekmonks.com/r/bel-reflection")
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("qr.png")