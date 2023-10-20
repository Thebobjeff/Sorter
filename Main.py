from PyQt6.QtWidgets import QApplication
from gui import Mainface  # Assuming your CombinedWindow class is in a file named combined_window.py

if __name__ == "__main__":
    app = QApplication([])  # Create a PyQt application
    window = Mainface()  # Create an instance of your CombinedWindow class
    window.show()  # Show the window
    app.exec()  # Run the application