import qrcode

url=input("Enter the URL:").strip()
file_path="D:\\qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)

print("Qr code has been generated")

