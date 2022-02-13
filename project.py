import qrcode

class CreateImage:
    def __init__(self, text):
        self.text = text
        self.image = qrcode.make(self.text)
        
    def SaveImage(self):
        self.image.save("your_qr_code.png")
        print("Image created successfully")

if __name__ == "__main__":
    text = input("Enter the text you want to convert into QR code: ")
    qrcode = CreateImage(text)
    qrcode.SaveImage()
