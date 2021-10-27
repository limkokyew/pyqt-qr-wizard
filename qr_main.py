import os
import qrcode
import sys
from pyzbar import pyzbar
from PIL import Image, ImageQt
from PyQt5 import QtGui, QtWidgets, uic


class QRMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QRMainWindow, self).__init__()
        uic.loadUi("qt_ui.ui", self)
        self.qr_code = None
        self.last_visited_dir = "."
        self.generate_qr_button.clicked.connect(self.generate_qr)
        self.save_qr_button.clicked.connect(self.save_qr)
        self.upload_qr_button.clicked.connect(self.upload_qr)
        self.show()

    def generate_qr(self):
        data = self.encode_text_field.text()
        qr_code = qrcode.make(data)
        self.qr_code = qr_code
        
        qr_img = ImageQt.ImageQt(qr_code.get_image().resize((300, 300)))
        qr_img = QtGui.QPixmap.fromImage(qr_img)
        self.encode_image.setPixmap(qr_img)
    
    def save_qr(self):
        if self.qr_code is not None:
            file_name = QtWidgets.QFileDialog.getSaveFileName(
                self, "QR-Code speichern", self.last_visited_dir, "*.png"
            )
            if file_name[0]:
                self.qr_code.save(file_name[0])
                self.last_visited_dir = os.path.dirname(file_name[0])

    def upload_qr(self):
        qr_file_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QR-Code hochladen",
            self.last_visited_dir,
            "Bilder (*.jpg *.jpeg *.png)"
        )
        if qr_file_path[0]:
            with Image.open(qr_file_path[0]) as img:
                qr_code = pyzbar.decode(img)
                qr_img = ImageQt.ImageQt(img.resize((300, 300))).copy()
                qr_img = QtGui.QPixmap.fromImage(qr_img)
                self.decode_image.setPixmap(qr_img)
            if qr_code:
                self.decode_text_field.setText(qr_code[0].data.decode("utf-8"))
            else:
                self.decode_text_field.setText("Es wurde kein QR-Code erkannt.")
            self.last_visited_dir = os.path.dirname(qr_file_path[0])

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QRMainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
