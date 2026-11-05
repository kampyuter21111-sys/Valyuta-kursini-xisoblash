from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


# ---------- umumiy stillar (bir joyda, hamma oynada ishlatiladi) ----------
FON_STIL = "#oyna { background-color: #f8f7f1; }"

SARLAVHA_STIL = "font-size: 26px; font-weight: bold; color: #1f3d2f;"

YASHIL_STIL = (
    "font-size: 20px; color: black; background-color: #96c8af; "
    "border-radius: 10px;"
)

COMBO_STIL = """
    QComboBox {
        font-size: 20px;
        color: black;
        background-color: #96c8af;
        border-radius: 10px;
        padding-left: 10px;
    }
    QComboBox QAbstractItemView {
        font-size: 18px;
        background-color: #f8f7f1;
        selection-background-color: #96c8af;
        selection-color: black;
    }
"""

INPUT_STIL = (
    "font-size: 20px; color: black; background-color: white; "
    "border: 2px solid #96c8af; border-radius: 10px; padding-left: 8px;"
)

NATIJA_STIL = (
    "font-size: 20px; font-weight: bold; color: #1f3d2f; "
    "background-color: #e8f3ed; border: 2px solid #96c8af; border-radius: 10px;"
)

TUGMA_STIL = """
    QPushButton {
        font-size: 20px;
        color: black;
        background-color: #8fbfa7;
        border-radius: 20px;
    }
    QPushButton:hover {
        background-color: #7aaf95;
    }
    QPushButton:pressed {
        background-color: #679c82;
    }
"""

JADVAL_STIL = """
    QTableWidget {
        font-size: 16px;
        color: black;
        background-color: white;
        alternate-background-color: #eef6f1;
        border: 2px solid #96c8af;
        border-radius: 10px;
    }
"""

JADVAL_BOSH_STIL = """
    QHeaderView::section {
        background-color: #96c8af;
        color: black;
        font-size: 16px;
        font-weight: bold;
        padding: 8px;
        border: none;
    }
"""


# 2-oyna
class PricesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("oyna")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(FON_STIL)

        self.setWindowTitle("Currency prices")
        self.setGeometry(700, 150, 600, 420)

        # sarlavha
        self.sarlavha = QLabel(self)
        self.sarlavha.setText("Currency prices")
        self.sarlavha.setGeometry(0, 10, 600, 50)
        self.sarlavha.setAlignment(Qt.AlignCenter)
        self.sarlavha.setStyleSheet(SARLAVHA_STIL)

        # jadval
        malumotlar = [
            ("AQSh dollari", "12460", "-21", "03.09.2025"),
            ("EVRO", "14545", "+4", "03.09.2025"),
            ("Rossiya rubli", "155", "-0", "03.09.2025"),
            ("Funt sterling", "16772", "-81", "03.09.2025"),
            ("Yaponiya iyenasi", "84", "-0", "03.09.2025"),
        ]

        self.jadval = QTableWidget(self)
        self.jadval.setGeometry(20, 70, 560, 330)
        self.jadval.setRowCount(len(malumotlar))
        self.jadval.setColumnCount(4)
        self.jadval.setHorizontalHeaderLabels(["Name", "Price", "Diff", "Date"])
        self.jadval.verticalHeader().setVisible(False)
        self.jadval.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.jadval.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.jadval.setSelectionMode(QAbstractItemView.NoSelection)
        self.jadval.setFocusPolicy(Qt.NoFocus)
        self.jadval.setShowGrid(False)
        self.jadval.setAlternatingRowColors(True)
        self.jadval.setStyleSheet(JADVAL_STIL)
        self.jadval.horizontalHeader().setStyleSheet(JADVAL_BOSH_STIL)
        self.jadval.horizontalHeader().setFixedHeight(45)

        for qator, satr in enumerate(malumotlar):
            self.jadval.setRowHeight(qator, 55)
            for ustun, qiymat in enumerate(satr):
                item = QTableWidgetItem(qiymat)
                item.setTextAlignment(Qt.AlignCenter)

                # Diff ustuni: o'sish yashil, kamayish qizil
                if ustun == 2:
                    if qiymat.startswith("+"):
                        item.setForeground(QColor("#2e8b57"))
                    elif qiymat.startswith("-") and qiymat != "-0":
                        item.setForeground(QColor("#d64545"))

                self.jadval.setItem(qator, ustun, item)


# 1-oyna
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("oyna")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(FON_STIL)

        self.setWindowTitle("Currency Convertor")
        self.setGeometry(150, 150, 510, 500)

        # 1-oyna sarlavha
        self.label = QLabel(self)
        self.label.setText("Currency Convertor")
        self.label.setGeometry(0, 15, 510, 50)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(SARLAVHA_STIL)

        # qiymat kiriting yozuvi
        self.qiymat = QLabel(self)
        self.qiymat.setText("Qiymat kiriting")
        self.qiymat.setGeometry(50, 100, 200, 40)
        self.qiymat.setAlignment(Qt.AlignCenter)
        self.qiymat.setStyleSheet(YASHIL_STIL)

        # qiymat kiritish maydoni
        self.qiymat_kiritish = QLineEdit(self)
        self.qiymat_kiritish.setGeometry(260, 100, 200, 40)
        self.qiymat_kiritish.setPlaceholderText("Summa (so'm)")
        self.qiymat_kiritish.setStyleSheet(INPUT_STIL)

        # valyuta tanlang menyusi
        self.valyuta = QComboBox(self)
        self.valyuta.setGeometry(50, 200, 200, 40)
        self.valyuta.setStyleSheet(COMBO_STIL)

        self.valyuta.addItem("Valyuta tanlang")
        self.valyuta.addItem("Aqsh dollari")
        self.valyuta.addItem("Evro")
        self.valyuta.addItem("Rubl")
        self.valyuta.addItem("Funt sterling")
        self.valyuta.addItem("Yapon iyenasi")

        # kurslar
        self.kurslar = {
            "Aqsh dollari": 12460,
            "Evro": 14545,
            "Rubl": 155,
            "Funt sterling": 16772,
            "Yapon iyenasi": 84,
        }

        # kurs chiqadigan QLabel
        self.kurs_label = QLabel(self)
        self.kurs_label.setText("")
        self.kurs_label.setGeometry(260, 200, 200, 40)
        self.kurs_label.setAlignment(Qt.AlignCenter)
        self.kurs_label.setStyleSheet(NATIJA_STIL)

        # kursni ulash
        self.valyuta.currentTextChanged.connect(self.kursni_korsat)

        # somdan yozuvi
        self.som = QLabel(self)
        self.som.setText("So'mdan \u2192")
        self.som.setGeometry(50, 300, 200, 40)
        self.som.setAlignment(Qt.AlignCenter)
        self.som.setStyleSheet(YASHIL_STIL)

        # natija ko'rsatish
        self.natija_label = QLabel(self)
        self.natija_label.setText("")
        self.natija_label.setGeometry(260, 300, 200, 40)
        self.natija_label.setAlignment(Qt.AlignCenter)
        self.natija_label.setStyleSheet(NATIJA_STIL)

        # hisoblash tugmasi
        self.hisoblash_tugmasi = QPushButton("Hisoblash", self)
        self.hisoblash_tugmasi.setGeometry(50, 420, 200, 40)
        self.hisoblash_tugmasi.setCursor(Qt.PointingHandCursor)
        self.hisoblash_tugmasi.setStyleSheet(TUGMA_STIL)
        self.hisoblash_tugmasi.clicked.connect(self.hisobla)

        # Valyutalar narxlari tugmasi
        self.narxlar_tugmasi = QPushButton("Valyutalar narxlari", self)
        self.narxlar_tugmasi.setGeometry(260, 420, 200, 40)
        self.narxlar_tugmasi.setCursor(Qt.PointingHandCursor)
        self.narxlar_tugmasi.setStyleSheet(TUGMA_STIL)

        self.prices_window = PricesWindow()
        self.narxlar_tugmasi.clicked.connect(self.narxlarni_och)

        self.show()

    # funksiya
    def kursni_korsat(self, text):
        kurs = self.kurslar.get(text, "")
        self.kurs_label.setText(str(kurs))

    # funksiya hisoblash
    def hisobla(self):
        son = float(self.qiymat_kiritish.text())
        kurs = self.kurslar.get(self.valyuta.currentText())
        natija = son / kurs
        self.natija_label.setText(str(round(natija, 2)))

    # ikkinchi oynani ochish
    def narxlarni_och(self):
        self.prices_window.show()


app = QApplication([])
window = MainWindow()
app.exec_()