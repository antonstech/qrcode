import qrcode

data = input("Gieb hier den Inhalt des QR-Codes an (z.B Link oder Text): ")
name = input("Wie soll die Datei heißen?: ")
qr = qrcode.QRCode(box_size=50, border=1)
qr.add_data(data)
img = qr.make_image()
img.save(name + ".png")
print("Der QR-Code " + name + ".png" + " wurde erfolgreich erzeugt!")
