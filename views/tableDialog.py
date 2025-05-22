from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QFrame, QSpinBox
from PySide6.QtCore import Qt
from models.menu import CARTE_ENTREES, CARTE_PLATS, CARTE_DESSERTS, MenuItem

class TableDialog(QDialog):
    def __init__(self, table_label: str, previous_order=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(table_label)
        self.occupied = None
        self.previous_order = previous_order
        self.order = {"entrees": [], "plats": [], "desserts": []}
        self._build_ui()
        self._populate_previous_order()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.addWidget(QLabel(f"Choisissez l'état de : {self.windowTitle()}"), alignment=Qt.AlignCenter)

        buttons = QHBoxLayout()
        self.btn_free = QPushButton("Libre")
        self.btn_occ = QPushButton("Occupée")
        self.btn_free.clicked.connect(self.set_free)
        self.btn_occ.clicked.connect(self.show_order_widgets)
        buttons.addWidget(self.btn_free)
        buttons.addWidget(self.btn_occ)
        main.addLayout(buttons)

        self.zone = QFrame()
        self.zone.hide()
        form = QVBoxLayout(self.zone)
        self._add_items(form, "Entrées", CARTE_ENTREES, "entree_spins")
        self._add_items(form, "Plats", CARTE_PLATS, "plat_spins")
        self._add_items(form, "Desserts", CARTE_DESSERTS, "dessert_spins")

        self.label_total = QLabel("Total : 0.00 €")
        form.addWidget(self.label_total)

        self.btn_ok = QPushButton("Enregistrer la commande")
        self.btn_ok.clicked.connect(self.validate_occupied)
        form.addWidget(self.btn_ok)

        main.addWidget(self.zone)

    def _add_items(self, layout, title, items, attr_name):
        layout.addWidget(QLabel(title))
        spins = []
        for item in items:
            line = QHBoxLayout()
            label = QLabel(str(item))
            spin = QSpinBox()
            spin.setRange(0, 99)
            spin.item = item
            spin.valueChanged.connect(self.update_total)
            line.addWidget(label)
            line.addWidget(spin)
            layout.addLayout(line)
            spins.append(spin)
        setattr(self, attr_name, spins)

    def _populate_previous_order(self):
        if not self.previous_order:
            return

        def restore(spins, key):
            items = {item["name"]: item["qty"] for item in self.previous_order.get(key, [])}
            for spin in spins:
                if spin.item.name in items:
                    spin.setValue(items[spin.item.name])

        restore(self.entree_spins, "entrees")
        restore(self.plat_spins, "plats")
        restore(self.dessert_spins, "desserts")

    def show_order_widgets(self):
        self.zone.show()

    def update_total(self):
        total = 0.0
        for spin in self.entree_spins + self.plat_spins + self.dessert_spins:
            total += spin.item.price * spin.value()
        self.label_total.setText(f"Total : {total:.2f} €")

    def validate_occupied(self):
        self.occupied = True

        def collect(spins):
            return [
                {"name": spin.item.name, "price": spin.item.price, "qty": spin.value()}
                for spin in spins if spin.value() > 0
            ]

        self.order = {
            "entrees": collect(self.entree_spins),
            "plats": collect(self.plat_spins),
            "desserts": collect(self.dessert_spins)
        }
        self.accept()

    def set_free(self):
        self.occupied = False
        self.accept()
