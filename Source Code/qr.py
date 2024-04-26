# Libraries
import sys

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
    ) -> None:
        """This class is used to initiate the generation of the QR code in the `.png` format

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

    def checkFileName(self, fileName: str) -> str:
        """Check if the file name that was given meets the criteria of the naming process

        Args:
            fileName (str): The file name of the QR code generated

        Returns:
            str: Returns a file name based on the simple rules of the naming process. Ideal file name is `*.png`
        """

        # example -> fileName="" (<- Null) -> fileName="qrcode"
        if fileName == "":
            fileName = "qrcode"
        # example -> fileName=".png" (<- No name but correct extension) -> fileName="qrcode"
        if fileName.split(".")[0] == "":
            fileName = "qrcode"
        # example -> fileName="qrcode.jpg" -> fileName="qrcode.jpg.png" (The last extension is the one that matters)
        if fileName.split(".")[1] != "png":
            fileName += ".png"
        return fileName  # returns the corrected file name (if correction were made, otherwise returns the original name given)

    def generate(self) -> None:
        """This function generates the QR code in the `.png` format"""
        self.qrCode.add_data(self.content)  # adding the content of the QR code
        self.qrCode.make(fit=True)  # not really sure what this does xD
        self.qrImage = self.qrCode.make_image(
            fill_color=self.accentColor, back_color=self.backgroundColor
        )  # editing the QR code accent color and background color
        self.fileName = self.checkFileName(self.fileName)  # correcting the file name
        self.qrImage.save(self.fileName)  # saving the QR code


# Putting everything together
if __name__ == "__main__":
    arguments = sys.argv  # command syntax: python qr.py {content}
    arguments = arguments[1:]  # removing the file path from the arguments (because it isn't an argument xD)
    # checking if the arguments are correct
    if len(arguments) == 0 or len(arguments) > 1:
        raise SyntaxError(
            "missing argument {qrContent}"
        )  # raising an error if the arguments are not correct
    # generating the QR code
    qr = QrCodeGenerator(
        qrContent=arguments[0]
    )  # creating the qr class and passing the content argument
    qr.generate()  # generating and saving the QR code

# VERSION: 1.0
# Syntax: python qr.py {content}
# Made by Harry Sidiropoulos
