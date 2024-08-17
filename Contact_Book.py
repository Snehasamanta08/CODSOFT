import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QMessageBox

class ContactBook(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contact Book")
        layout = QVBoxLayout()

        # Form fields
        self.name_input = QLineEdit(self); layout.addWidget(QLabel('Store Name:')); layout.addWidget(self.name_input)
        self.phone_input = QLineEdit(self); layout.addWidget(QLabel('Phone Number:')); layout.addWidget(self.phone_input)
        self.email_input = QLineEdit(self); layout.addWidget(QLabel('Email:')); layout.addWidget(self.email_input)
        self.address_input = QLineEdit(self); layout.addWidget(QLabel('Address:')); layout.addWidget(self.address_input)

        # Buttons
        self.add_button = QPushButton('Add Contact', self); self.add_button.clicked.connect(self.add_contact)
        self.update_button = QPushButton('Update Contact', self); self.update_button.clicked.connect(self.update_contact)
        self.delete_button = QPushButton('Delete Contact', self); self.delete_button.clicked.connect(self.delete_contact)
        layout.addWidget(self.add_button); layout.addWidget(self.update_button); layout.addWidget(self.delete_button)

        # Contact list
        self.contact_list = QListWidget(self); self.contact_list.itemDoubleClicked.connect(self.view_contact_details)
        layout.addWidget(self.contact_list)

        self.setLayout(layout)

    def add_contact(self):
        contact = {'name': self.name_input.text(), 'phone': self.phone_input.text(),
                   'email': self.email_input.text(), 'address': self.address_input.text()}
        self.contacts.append(contact)
        self.update_contact_list()
        QMessageBox.information(self, "Success", "Contact added successfully")

    def update_contact_list(self):
        self.contact_list.clear()
        for contact in self.contacts:
            self.contact_list.addItem(f"{contact['name']} ({contact['phone']})")

    def view_contact_details(self):
        selected_contact = self.contacts[self.contact_list.currentRow()]
        self.name_input.setText(selected_contact['name'])
        self.phone_input.setText(selected_contact['phone'])
        self.email_input.setText(selected_contact['email'])
        self.address_input.setText(selected_contact['address'])

    def update_contact(self):
        selected_index = self.contact_list.currentRow()
        self.contacts[selected_index] = {'name': self.name_input.text(), 'phone': self.phone_input.text(),
                                         'email': self.email_input.text(), 'address': self.address_input.text()}
        self.update_contact_list()
        QMessageBox.information(self, "Success", "Contact updated successfully")

    def delete_contact(self):
        del self.contacts[self.contact_list.currentRow()]
        self.update_contact_list()
        QMessageBox.information(self, "Success", "Contact deleted successfully")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactBook()
    window.show()
    sys.exit(app.exec_())
