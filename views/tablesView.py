from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame, QPushButton, QSpinBox
)
from PySide6.QtCore import Qt

from models.Menu import CARTE_ENTREES, CARTE_PLATS, CARTE_DESSERTS, MenuItem


class TableView(QDialog):
    # ------------------------------------------------------------------ init
    def __init__(self, table_label: str,
                 previous_order: dict | None = None,
                 parent=None):
        super().__init__(parent)

        self.setWindowTitle(table_label)

        # État que le contrôleur viendra lire après exec()
        self._occupied: bool | None = None
        self._order: dict[str, list[dict]] = {
            "entrees": [], "plats": [], "desserts": []
        }

        # --------- en‑tête -------------------------------------------------
        main = QVBoxLayout(self)
        main.addWidget(QLabel(f"État de : {table_label}"), alignment=Qt.AlignCenter)

        # --------- boutons Libre / Occupée --------------------------------
        line = QHBoxLayout()
        main.addLayout(line)

        btn_free = QPushButton("Libre")
        btn_free.clicked.connect(self._on_free)
        line.addWidget(btn_free)

        btn_occ = QPushButton("Occupée")
        btn_occ.clicked.connect(self._show_zone)
        line.addWidget(btn_occ)

        # --------- zone commande (cachée au départ) -----------------------
        self.zone = QFrame(); self.zone.hide()
        form = QVBoxLayout(self.zone)
        main.addWidget(self.zone)

        # listes de spinbox pour chaque catégorie
        self.entree_spins  = self._add_spin_block("Entrées",  CARTE_ENTREES,  form)
        self.plat_spins    = self._add_spin_block("Plats",    CARTE_PLATS,    form)
        self.dessert_spins = self._add_spin_block("Desserts", CARTE_DESSERTS, form)

        # total
        self.lbl_total = QLabel("Total : 0.00 €")
        form.addWidget(self.lbl_total)

        # bouton valider
        btn_ok = QPushButton("Enregistrer la commande")
        btn_ok.clicked.connect(self._on_ok)
        form.addWidget(btn_ok)

        self.resize(340, 400)
        self._restore_previous(previous_order)

    # ----------------------------------------------------------------- utils
    def _add_spin_block(self, title: str, menu_list: list[MenuItem], parent_layout):
        """Ajoute un titre + une ligne ‹label + spin› pour chaque item."""
        parent_layout.addWidget(QLabel(title))
        spins: list[QSpinBox] = []
        for it in menu_list:
            h = QHBoxLayout()
            h.addWidget(QLabel(str(it)))
            sp = QSpinBox(minimum=0, maximum=99)
            sp.menu_item = it      # on attache l'objet MenuItem au spin
            sp.valueChanged.connect(self._update_total)
            h.addWidget(sp)
            parent_layout.addLayout(h)
            spins.append(sp)
        return spins

    def _restore_previous(self, data: dict | None):
        """Remplit les spinbox si une ancienne commande est passée."""
        if not data:
            return
        def load(spins, key):
            q = {d["name"]: d["qty"] for d in data.get(key, [])}
            for sp in spins:
                if sp.menu_item.name in q:
                    sp.setValue(q[sp.menu_item.name])
        load(self.entree_spins,  "entrees")
        load(self.plat_spins,    "plats")
        load(self.dessert_spins, "desserts")
        self._update_total()

    # ----------------------------------------------------------------- slots
    def _show_zone(self):
        self.zone.show()

    def _update_total(self):
        total = sum(
            sp.menu_item.price * sp.value()
            for sp in self.entree_spins + self.plat_spins + self.dessert_spins
        )
        self.lbl_total.setText(f"Total : {total:.2f} €")

    def _on_free(self):
        """Signalé ‹Libre› : on ferme en disant que la table est libre."""
        self._occupied = False
        self.accept()

    def _on_ok(self):
        """Construit self._order à partir des spinbox puis accepte le dialog."""
        self._occupied = True

        def collect(spins):
            return [
                {"name": sp.menu_item.name,
                 "price": sp.menu_item.price,
                 "qty": sp.value()}
                for sp in spins if sp.value() > 0
            ]

        self._order = {
            "entrees":  collect(self.entree_spins),
            "plats":    collect(self.plat_spins),
            "desserts": collect(self.dessert_spins)
        }
        self.accept()

    # ---------------------------------------------------------------- getters
    def is_free(self) -> bool:
        """Appelé par le contrôleur : True → table libre, False → occupée."""
        return self._occupied is False

    def order(self) -> dict[str, list[dict]]:
        """Commande sous forme de dictionnaire (prêt pour le modèle/JSON)."""
        return self._order