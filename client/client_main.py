
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class SimpleClient(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Simple PyQt6 Client")
        self.setGeometry(100, 100, 300, 200)  # 设置窗口位置和大小
        
        layout = QVBoxLayout()
        label = QLabel("Hello, PyQt6!")
        layout.addWidget(label)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = SimpleClient()
    client.show()
    sys.exit(app.exec())


