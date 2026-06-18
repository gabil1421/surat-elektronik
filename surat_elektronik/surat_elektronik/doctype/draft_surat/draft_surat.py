import frappe
from frappe.model.document import Document

class DraftSurat(Document):
    def on_submit(self):
        frappe.get_doc({
            "doctype": "Surat Masuk",
            "perihal": self.perihal,
            "pengirim": frappe.session.user,
            "tanggal_masuk": frappe.utils.today()
        }).insert()
