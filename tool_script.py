import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox


class ShortcutGenerator(QWidget):
    def __init__(self):
        super().__init__()

        #----------------------------window properties----------------------------
        self.setWindowTitle("Shortcut Generator")
        self.resize(600, 300)

        self.setStyleSheet("""
            QWidget {
                background-color: #222;
                color: #fff;
                font-family: Arial, sans-serif;
            }

            QLabel {
                font-weight: bold;
            }

            QPushButton {
                font-size: 14px;
                background-color: #333;
                color: #fff;
                border: 1px solid #5bc0de;
                padding: 8px 16px;
                border-radius: 4px;
            }           

            QPushButton:hover {
                background-color: #007bff;
            }

            QLineEdit, QTextEdit {
                background-color: #333;
                color: #fff;
                border: 1px solid #5bc0de;
                border-radius: 4px;
                padding: 6px 8px;
                font-size: 12px
            }
        """)

        #----------------------------input widgets----------------------------
        
        #shortcut title label and input
        self.title_label = QLabel("<b>Title:</b>")
        self.title_label.setToolTip("The title of the shortcut")
        self.title_input = QLineEdit()
        self.title_input.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        #shortcut label and input
        self.shortcut_label = QLabel("<b>Shortcut:</b>")
        self.shortcut_label.setToolTip("The shortcut you will type in your editor")
        self.shortcut_input = QLineEdit()
        self.shortcut_input.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        #code label and input (multiline)
        self.code_label = QLabel("<b>Code:</b>")
        self.code_label.setToolTip("The code that will be generated after typing your shortcut")
        self.code_input = QTextEdit()
        self.code_input.setFixedHeight(200)

        #add-shortcut button
        self.add_button = QPushButton("Add Shortcut")
        self.add_button.clicked.connect(self.add_shortcut)

        #export button
        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export_to_snippet)

        #layout parameters
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)
        layout.addWidget(self.shortcut_label)
        layout.addWidget(self.shortcut_input)
        layout.addWidget(self.code_label)
        layout.addWidget(self.code_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.export_button)
        self.setLayout(layout)

    #----------------------------shortcut function----------------------------
    def add_shortcut(self):
        title = self.title_input.text().strip()
        shortcut = self.shortcut_input.text().strip()
        code = self.code_input.toPlainText().strip()

        #----------------------------xml file----------------------------
        #check if fields are filled
        if title and shortcut and code:
            #write xml file
            with open("shortcuts.xml", "a") as file:
                file.write(f'<CodeSnippet Format="1.0.0">\n')
                file.write(f'\t<Header>\n')
                file.write(f'\t\t<Title>{title}</Title>\n')
                file.write(f'\t\t<Shortcut>{shortcut}</Shortcut>\n')
                file.write(f'\t\t<Description>Unity shortcut snippet</Description>\n')
                file.write(f'\t\t<Author>YourName</Author>\n')
                file.write(f'\t\t<SnippetTypes>\n')
                file.write(f'\t\t\t<SnippetType>Expansion</SnippetType>\n')
                file.write(f'\t\t</SnippetTypes>\n')
                file.write(f'\t</Header>\n')
                file.write(f'\t<Snippet>\n')
                file.write(f'\t\t<Code Language="csharp">\n')
                file.write(f'\t\t\t<![CDATA[{code}]]>\n')
                file.write(f'\t\t</Code>\n')
                file.write(f'\t</Snippet>\n')
                file.write(f'</CodeSnippet>\n')

            #----------------------------messages----------------------------
            #added-shortcut message
            QMessageBox.information(self, "Success", "Shortcut added successfully.")

            #clear fields
            self.title_input.clear()
            self.shortcut_input.clear()
            self.code_input.clear()
            self.code_input.setFocus()
        else:
            #error message
            QMessageBox.warning(self, "Error", "Please fill in all fields.")

    #----------------------------export function----------------------------
    def export_to_snippet(self):
        try:
            #change file extension to .snippet
            os.rename("shortcuts.xml", "shortcuts.snippet")
            QMessageBox.information(self, "Success", "Exported to shortcuts.snippet successfully.")
        except FileNotFoundError:
            #error message if no shortcuts are found
            QMessageBox.warning(self, "Error", "No shortcuts to export.")

#----------------------------initialize app----------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = ShortcutGenerator()
    generator.show()
    sys.exit(app.exec_())
