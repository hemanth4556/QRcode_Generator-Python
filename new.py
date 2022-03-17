import qrcode

#qr = qrcode.QRCode(version=1, box_size=15, border=5)
#generate_image = qrcode.make("https://hemanth4556.github.io/personal-portfolio/#")
#generate_image.save('image1.png')


data = 'https://hemanth4556.github.io/personal-portfolio/#'

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'black'
                    )

img.save('image1.png')