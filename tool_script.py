import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QScrollArea, QGroupBox, QComboBox, QColorDialog
from PyQt5.QtCore import QFile, Qt


class ShortcutWidget(QWidget):
    
    def __init__(self, title, color, delete_callback):
        super().__init__()

        self.title = title
        self.background_color = color

        self.title_label = QLabel(title)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #333333; background-color: rgba(255, 255, 255, 0.7);")

        self.delete_button = QPushButton("Delete")
        self.change_color_button = QPushButton("Change Color")

        self.delete_button.clicked.connect(delete_callback)
        self.change_color_button.clicked.connect(self.change_color)

        layout = QHBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.change_color_button)
        self.setLayout(layout)

        self.set_color(color)

    def set_color(self, color):
        style_sheet = f"background-color: {color}; border: 1px solid #c0c0c0; border-radius: 5px; padding: 5px;"
        self.setStyleSheet(style_sheet)
        self.background_color = color

        # Update button stylesheets
        self.update_button_stylesheets()

    def update_button_stylesheets(self):
        button_stylesheet = f"background-color: {self.background_color};"
        self.delete_button.setStyleSheet(button_stylesheet)
        self.change_color_button.setStyleSheet(button_stylesheet)

    def change_color(self):
        color_dialog = QColorDialog()
        color = color_dialog.getColor()
        if color.isValid():
            self.set_color(color.name())


class ShortcutGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shortcut Generator")
        self.resize(800, 400)

        # Load CSS file
        css_data = """
        /* Set background color for the entire application */
        QWidget {
            background-color: #f2f2f2;
        }

        /* Style for group boxes */
        QGroupBox {
            border: 1px solid #c0c0c0;
            border-radius: 10px;
            margin-top: 10px;
            padding: 10px;
            background-color: #ffffff; /* White background */
        }

        /* Style for labels */
        QLabel {
            color: #333333;
        }

        /* Style for line edits, text edits, and combo boxes */
        QLineEdit, QTextEdit, QComboBox {
            border: 1px solid #c0c0c0;
            border-radius: 5px;
            padding: 5px;
            background-color: #ffffff; /* White background */
        }

        /* Style for buttons */
        QPushButton {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            margin: 4px 2px;
            border-radius: 5px;
        }

        /* Hover effect for buttons */
        QPushButton:hover {
            background-color: #45a049; /* Darker green */
        }

        /* Pressed effect for buttons */
        QPushButton:pressed {
            background-color: #3e8e41; /* Even darker green */
        }
        """

        self.setStyleSheet(css_data)

        self.left_group = QGroupBox("Shortcut Generation")
        self.right_group = QGroupBox("Added shortcuts")

        self.title_label = QLabel("<b>Title:</b>")
        self.title_label.setToolTip("The title of the shortcut")
        self.title_input = QLineEdit()
        self.title_input.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.shortcut_label = QLabel("<b>Shortcut:</b>")
        self.shortcut_label.setToolTip("The shortcut you will type in your editor")
        self.shortcut_input = QLineEdit()
        self.shortcut_input.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.code_label = QLabel("<b>Code:</b>")
        self.code_label.setToolTip("The code that will be generated after typing your shortcut")
        self.code_input = QTextEdit()
        self.code_input.setFixedHeight(200)

        self.language_label = QLabel("<b>Language:</b>")
        self.language_label.setToolTip("Select the programming language for the snippet")
        self.language_dropdown = QComboBox()
        self.language_dropdown.addItems(["Python","C#", "C++", "Java", "JavaScript"])  # Default options

        self.add_button = QPushButton("Add Shortcut")
        self.add_button.clicked.connect(self.add_shortcut)

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export_to_snippet)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.title_label)
        left_layout.addWidget(self.title_input)
        left_layout.addWidget(self.shortcut_label)
        left_layout.addWidget(self.shortcut_input)
        left_layout.addWidget(self.code_label)
        left_layout.addWidget(self.code_input)
        left_layout.addWidget(self.language_label)
        left_layout.addWidget(self.language_dropdown)
        left_layout.addWidget(self.add_button)
        left_layout.addWidget(self.export_button)

        self.left_group.setLayout(left_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setAlignment(QtCore.Qt.AlignTop)

        self.scroll_area.setWidget(self.scroll_area_widget)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.scroll_area)

        self.right_group.setLayout(right_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.left_group, 2)
        main_layout.addWidget(self.right_group, 3)

        self.setLayout(main_layout)

        self.snippets = []

    def add_shortcut(self):
        title = self.title_input.text().strip()
        shortcut = self.shortcut_input.text().strip()
        code = self.code_input.toPlainText().strip()
        language = self.language_dropdown.currentText()

        if title and shortcut and code:
            snippet = f'<CodeSnippet Format="1.0.0">\n' \
                      f'\t<Header>\n' \
                      f'\t\t<Title>{title}</Title>\n' \
                      f'\t\t<Shortcut>{shortcut}</Shortcut>\n' \
                      f'\t\t<Description>Unity shortcut snippet</Description>\n' \
                      f'\t\t<Author>YourName</Author>\n' \
                      f'\t\t<SnippetTypes>\n' \
                      f'\t\t\t<SnippetType>Expansion</SnippetType>\n' \
                      f'\t\t</SnippetTypes>\n' \
                      f'\t</Header>\n' \
                      f'\t<Snippet>\n' \
                      f'\t\t<Code Language="{language.lower()}">\n' \
                      f'\t\t\t<![CDATA[{code}]]>\n' \
                      f'\t\t</Code>\n' \
                      f'\t</Snippet>\n' \
                      f'</CodeSnippet>\n'

            self.snippets.append(snippet)

            shortcut_widget = ShortcutWidget(title, "grey", self.delete_shortcut)
            self.scroll_area_layout.addWidget(shortcut_widget)

            self.title_input.clear()
            self.shortcut_input.clear()
            self.code_input.clear()
            self.code_input.setFocus()

            QMessageBox.information(self, "Success", "Shortcut added successfully.")
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")

    def export_to_snippet(self):
        if not self.snippets:
            QMessageBox.warning(self, "Error", "No shortcuts to export.")
            return

        file_name = "shortcuts.snippet"
        with open(file_name, "w") as file:
            file.write('<?xml version="1.0" encoding="utf-8"?>\n')
            file.write('<Shortcuts>\n')
            for snippet in self.snippets:
                file.write(snippet)
            file.write('</Shortcuts>\n')

        QMessageBox.information(self, "Success", f"Exported to {file_name} successfully.")

    def delete_shortcut(self):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            shortcut_widget = sender.parent()
            title = shortcut_widget.title
            self.scroll_area_layout.removeWidget(shortcut_widget)
            shortcut_widget.deleteLater()
            for snippet in self.snippets:
                if title in snippet:
                    self.snippets.remove(snippet)
                    break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = ShortcutGenerator()
    generator.show()
    sys.exit(app.exec_())