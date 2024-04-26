# Libraries
from qrcode import ERROR_CORRECT_L
from qrcode.main import QRCode


# Classes
class QrCodeGenerator:
    def __init__(
        self,
        qrContent: str = "This is the content of this qr code",
        qrFileName: str = "qrcode.png",
        qrAccentColor: str = "#000000",
        qrBackgroundColor: str = "#ffffff",
    ):
        """This class is used to generate QR code image in the `.png` format

        Args:
            qrContent (str, optional): The content of the QR code. Defaults to `This is the content of this qr code`.
            qrFileName (str, optional): The name of the QR code image. Defaults to `qrcode.png`.
            qrAccentColor (str, optional): The QR code accent color. Defaults to `#000000`.
            qrBackgroundColor (str, optional): The QR code background color. Defaults to `#ffffff`
        """
        # Initializing the variables
        self.content = qrContent
        self.fileName = qrFileName
        self.accentColor = qrAccentColor
        self.backgroundColor = qrBackgroundColor

        # Creating the QR Code object
        self.qrCode = QRCode(error_correction=ERROR_CORRECT_L)


# Main program
if __name__ == "__main__":
    pass
