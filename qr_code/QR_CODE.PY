import qrcode
# taking upi id as a input
upi_id=input("Enter the upi id=")
# defining the payment url based on the payment app
fampay_url=f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'
# crate qr codes for a payment app
fampay_qr=qrcode.make(fampay_url)
# saving the qr code to image file
fampay_qr.save('fampay_qr.png')
# display theqr codes(it need to install pillow )
fampay_qr.show()
