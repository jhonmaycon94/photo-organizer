import os
import shutil
from datetime import datetime

class ReceiptOrganizer:

    extensions = ['html', 'htm']

    def folder_path_from_receipt_date(self, file):
        date = self.get_receipt_modification_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m')
    
    def get_receipt_modification_date(self, file):
        receipt = open(file)
        date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def move_receipt(self, file):
        new_folder = self.folder_path_from_receipt_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def organize(self):
        receipts = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in receipts:
            self.move_receipt(filename)
    
RO = ReceiptOrganizer()
RO.organize()
