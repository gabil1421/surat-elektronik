import frappe
from frappe.model.document import Document

class SuratMasuk(Document):
    def validate(self):
        if not self.pengirim:
            frappe.throw("Pengirim tidak boleh kosong")
        if not self.perihal:
            frappe.throw("Perihal tidak boleh kosong")
