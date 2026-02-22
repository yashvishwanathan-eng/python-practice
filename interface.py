import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QLineEdit,
    QTextEdit, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor

# ── Main Window ─────────────────────────────────────────────
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("My PyQt6 App")
        self.setGeometry(100, 100, 500, 600)  # x, y, width, height

        # Central widget (every QMainWindow needs one)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # ── Title Label ──────────────────────────────────────
        title = QLabel("Welcome to My PyQt6 App!")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #2E75B6; margin: 10px;")
        main_layout.addWidget(title)

        # ── Divider Line ─────────────────────────────────────
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("color: #CCCCCC;")
        main_layout.addWidget(line)

        # ── Name Input Row ───────────────────────────────────
        name_label = QLabel("Enter your name:")
        name_label.setFont(QFont("Arial", 11))
        main_layout.addWidget(name_label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type your name here...")
        self.name_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #CCCCCC;
                border-radius: 6px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #2E75B6;
            }
        """)
        main_layout.addWidget(self.name_input)

        # ── Buttons Row ──────────────────────────────────────
        button_layout = QHBoxLayout()

        self.greet_button = QPushButton("Greet Me 👋")
        self.greet_button.setStyleSheet("""
            QPushButton {
                background-color: #2E75B6;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1A56A0;
            }
        """)
        self.greet_button.clicked.connect(self.greet_user)
        button_layout.addWidget(self.greet_button)

        self.clear_button = QPushButton("Clear 🗑️")
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        self.clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(button_layout)

        # ── Output Label ─────────────────────────────────────
        self.output_label = QLabel("Your greeting will appear here!")
        self.output_label.setFont(QFont("Arial", 13))
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_label.setStyleSheet("""
            background-color: #D6EAF8;
            color: #1A3A5C;
            padding: 15px;
            border-radius: 8px;
            font-weight: bold;
        """)
        main_layout.addWidget(self.output_label)

        # ── Notes Area ───────────────────────────────────────
        notes_label = QLabel("Notes:")
        notes_label.setFont(QFont("Arial", 11))
        main_layout.addWidget(notes_label)

        self.notes_area = QTextEdit()
        self.notes_area.setPlaceholderText("Type anything you want to save here...")
        self.notes_area.setStyleSheet("""
            QTextEdit {
                padding: 8px;
                border: 2px solid #CCCCCC;
                border-radius: 6px;
                font-size: 12px;
            }
            QTextEdit:focus {
                border: 2px solid #2E75B6;
            }
        """)
        self.notes_area.setMaximumHeight(150)
        main_layout.addWidget(self.notes_area)

        # ── Save Notes Button ────────────────────────────────
        save_button = QPushButton("Save Notes 💾")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1E8449;
            }
        """)
        save_button.clicked.connect(self.save_notes)
        main_layout.addWidget(save_button)

        # ── Status Bar ───────────────────────────────────────
        self.statusBar().showMessage("App is ready! 🚀")

    # ── Button Functions ─────────────────────────────────────
    def greet_user(self):
        name = self.name_input.text().strip()
        if name == "":
            QMessageBox.warning(self, "Oops!", "Please enter your name first!")
            return
        self.output_label.setText(f"Hello, {name}! Welcome to PyQt6! 🎉")
        self.statusBar().showMessage(f"Greeted {name} successfully!")

    def clear_all(self):
        self.name_input.clear()
        self.notes_area.clear()
        self.output_label.setText("Your greeting will appear here!")
        self.statusBar().showMessage("Cleared everything!")

    def save_notes(self):
        notes = self.notes_area.toPlainText().strip()
        if notes == "":
            QMessageBox.warning(self, "Empty!", "There's nothing to save!")
            return
        with open("my_notes.txt", "w") as f:
            f.write(notes)
        QMessageBox.information(self, "Saved!", "Your notes have been saved to my_notes.txt ✅")
        self.statusBar().showMessage("Notes saved to my_notes.txt!")


# ── Run the App ──────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())