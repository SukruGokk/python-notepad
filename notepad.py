# -*- coding: utf-8 -*-
######################
# TÜRKÇE NOT DEFTERİ #
######################

# @author : SukruGokk
# @date : 28/06/2020
# @os : Windows 10
# @version : Python 3.8
# @description: Kodlar dışında yorumları ve uygulamanı görünen kısmını tamamen türkçe yaptım. Umarım işinize yarar.

# GÖK DEFTER

# Kütüphaneler

# PyQt5
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPlainTextEdit, QToolBar, QAction, QApplication, QWidget, \
    QStatusBar, QFontDialog, QColorDialog, QFileDialog, QMessageBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtPrintSupport import QPrintDialog

# Resimleri kullanabilmek için:
from os import path

# Pencere kapatıldığında programın kapanması için:
from sys import argv, exit

# Tarayıcıyı açmak için webbrowser kütüphanesinin open fonksiyonunu kullandım
from webbrowser import open as wbopen

# Window class'ı
class MainWindow(QMainWindow):

    # Class'ın contructor'ı
    def __init__(self):
        super(MainWindow, self).__init__()

        # Layout düzeni
        layout = QVBoxLayout()

        # Editor
        self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)

        # Default font olarak MS Shell dlg'yi ayarladım
        default_font = QFont("MS Shell dlg")
        default_font.setPointSize(12)
        self.editor.setFont(default_font)

        # self.path mevcut dosyanın yolunu tutuyor
        # Şu an None verdim çünkü şuan açık bir dosya yok
        self.path = None

        # Text edit widget'ını layout'a ekliyorum
        layout.addWidget(self.editor)

        # Container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Pencereye status bar ekliyorum mesela toolbar'daki bir action'un açıklaması alttaki status barda gözüküyor
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # Dosya ile alakalı işlemlerin olucağı bir toolbar ekliyorum
        file_toolbar = QToolBar("Dosya")
        file_toolbar.setIconSize(QSize(35, 35)) # Icon'ların boyutunu 35x35 pixel yapıyorum
        self.addToolBar(file_toolbar)

        # File menu'de üstteki açılır menu file toolbar ile aynı şeyler olucak file menu'de
        file_menu = self.menuBar().addMenu("Dosya")

        # Cursor file menu'nün üstüne gelince tarayıcıdaki bir linkin üstüne gelince aldığı şekli almasını ayarlıyoruz
        file_menu.setCursor(Qt.PointingHandCursor)

        # Bir dosya açılmak veya yeni bir dosya oluşturulmak istendiğinde bu harekete geçecek
        open_file_action = QAction(QIcon(path.join('images', 'open')), "Dosya aç veya yeni oluştur", self)

        # Status barda gözükecek olan açıklamayı ayarlıyoruz
        open_file_action.setStatusTip("Dosya aç veya yeni oluştur (Ctrl+o)")

        # Bu da kısayol
        open_file_action.setShortcut("Ctrl+o")

        # Action'a tıklandığında file_open method'u çalıştırılacak
        open_file_action.triggered.connect(self.file_open)

        # Action'u File menu ve file toolbar'a ekliyoruz
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        # Tekrardan açıklama yapmayacağım
        save_file_action = QAction(QIcon(path.join('images', 'save')), "Kaydet", self)
        save_file_action.setStatusTip("Bu dosyayı kaydet (Ctrl+s)")
        save_file_action.setShortcut("Ctrl+s")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        print_action = QAction(QIcon(path.join('images', 'print')), "Yazdır", self)
        print_action.setStatusTip("Bu dosyayı yazdır (Ctrl+p)")
        print_action.setShortcut("Ctrl+p")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        edit_toolbar = QToolBar("Düzenle")
        edit_toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("Düzenle")
        edit_menu.setCursor(Qt.PointingHandCursor)

        help_toolbar = QToolBar("Yardım")
        help_toolbar.setIconSize(QSize(40, 40))
        self.addToolBar(help_toolbar)
        help_menu = self.menuBar().addMenu("Yardım")
        help_menu.setCursor(Qt.PointingHandCursor)

        appearance_toolbar = QToolBar("Görünüm")
        appearance_toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(appearance_toolbar)
        appearance_menu = self.menuBar().addMenu("Görünüm")
        appearance_menu.setCursor(Qt.PointingHandCursor)
        self.addToolBar(appearance_toolbar)

        theme_action = QAction(QIcon(path.join('images', 'theme')), "Temayı değiştir", self)
        theme_action.setShortcut("Ctrl+t")
        theme_action.setStatusTip("Temayı ayarla (Ctrl+t)")
        theme_action.triggered.connect(self.set_theme)
        appearance_toolbar.addAction(theme_action)
        appearance_menu.addAction(theme_action)

        # Appearance toolbar'a ve Appearance menu'ye bir ayırıcı ekliyorum böylece iconlar arasında | şöyle bir çizgi oluyor
        appearance_toolbar.addSeparator()
        appearance_menu.addSeparator()

        font_action = QAction(QIcon(path.join('images', 'font')), "Yazı tipini değiştir", self)
        font_action.setStatusTip("Yazı tipini ayarla (Ctrl+f)")
        font_action.setShortcut("Ctrl+F")
        font_action.triggered.connect(self.set_font)
        appearance_toolbar.addAction(font_action)
        appearance_menu.addAction(font_action)

        color_font_action = QAction(QIcon(path.join('images', 'coloredFont')), "Yazı rengini değiştir", self)
        color_font_action.setStatusTip("Yazı rengini ayarla (Ctrl+g)")
        color_font_action.setShortcut("Ctrl+g")
        color_font_action.triggered.connect(self.set_text_color)
        appearance_toolbar.addAction(color_font_action)
        appearance_menu.addAction(color_font_action)

        telegram_action = QAction(QIcon(path.join('images', 'telegram')), "Geri bildirim gönder", self)
        telegram_action.setStatusTip("Geliştiriciye Telegram ile ulaş (Ctrl+Shift+t)")
        telegram_action.setShortcut("Ctrl+Shift+t")
        telegram_action.triggered.connect(self.open_telegram)
        help_menu.addAction(telegram_action)
        help_toolbar.addAction(telegram_action)

        undo_action = QAction(QIcon(path.join('images', 'undo')), "Geri Al", self)
        undo_action.setStatusTip("Son değişikliği geri al (Ctrl+z)")
        undo_action.setShortcut("Ctrl+z")
        undo_action.triggered.connect(self.editor.undo)
        edit_toolbar.addAction(undo_action)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(path.join('images', 'redo')), "İleri Al", self)
        redo_action.setStatusTip("Son değişikliği ileri al (Ctrl+y)")
        redo_action.setShortcut("Ctrl+y")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_toolbar.addSeparator()
        edit_menu.addSeparator()

        cut_action = QAction(QIcon(path.join('images', 'cut')), "Kes", self)
        cut_action.setStatusTip("Seçili metni kes (Ctrl+x)")
        cut_action.setShortcut("Ctrl+x")
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(path.join('images', 'copy')), "Kopyala", self)
        copy_action.setStatusTip("Seçili metni kopyla (Ctrl+c)")
        copy_action.setShortcut("Ctrl+c")
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = QAction(QIcon(path.join('images', 'paste')), "Yapıştır", self)
        paste_action.setStatusTip("Yapıştır (Ctrl+v)")
        paste_action.setShortcut("Ctrl+v")
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        select_all_action = QAction(QIcon(path.join("images", "selectall")), "Hepsini seç", self)
        select_all_action.setStatusTip("Tüm metni seç (Ctrl+a)")
        select_all_action.setShortcut("Ctrl+a")
        select_all_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_all_action)
        edit_toolbar.addAction(select_all_action)

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        self.editor.setStatusTip("Sözcük kaydırma: açık")
        word_wrap_action = QAction(QIcon(path.join("images", "wordwrap")), "Sözcük kaydırmayı aç yada kapat", self)
        word_wrap_action.setStatusTip("Sözcük kaydırmayı aç yada kapat (Ctrl+r)")
        word_wrap_action.setShortcut("Ctrl+r")
        word_wrap_action.triggered.connect(self.change_word_wrap)
        edit_menu.addAction(word_wrap_action)
        edit_toolbar.addAction(word_wrap_action)

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        web_action = QAction(QIcon(path.join('images', 'webbrowser.png')), "Tüm metni web'de ara", self)
        web_action.setStatusTip("Tüm metni web'de ara (Ctrl+w)")
        web_action.setShortcut("Ctrl+w")
        web_action.triggered.connect(self.search_text)
        edit_menu.addAction(web_action)
        edit_toolbar.addAction(web_action)

        url_action = QAction(QIcon(path.join('images', 'urlOpen.png')), "Tüm metni web'de url olarak aç", self)
        url_action.setStatusTip("Tüm metni web'de url olarak aç (Ctrl+u)")
        url_action.setShortcut("Ctrl+u")
        url_action.triggered.connect(self.open_link)
        edit_menu.addAction(url_action)
        edit_toolbar.addAction(url_action)

        # Pencereyi boyutlandırıyoruz
        self.setGeometry(200, 100, 1000, 700)

        # Update title methodu'nun amacı şu; eğer yeni bir dosya açıldıysa başlığında o dosyanın adı olarak değişmesi
        self.update_title()
        self.show()

    # Hata veren method
    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    # Font seçme dialoğunu açan ve seçilen fontu ayarlayan method
    def set_font(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.editor.setFont(font)

    # Renk seçme dialoğunu açan ve seçilen rengi yazı rengi olarak ayarlayan method
    def set_text_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.editor.setStyleSheet("color: {};".format(color.name()))

    # Renk seçme dialoğunu açan ve seçilen rengi arka plan rengi olarak ayarlayan method
    def set_theme(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.setStyleSheet("background-color: {};".format(color.name()))

    # Yazılı olan metni internette arayan method
    def search_text(self):
        if self.editor.document().toPlainText() == "":
            self.dialog_critical("Web'de aranacak metin yok")
            return

        wbopen("https://yandex.com/search?text={}".format(self.editor.document().toPlainText()))

    # Yazılı olan metni link olarak açan method
    def open_link(self):
        if self.editor.document().toPlainText() == "":
            self.dialog_critical("Link olarak açılacak metin yok")
            return

        wbopen(self.editor.document().toPlainText())

    # Yeni dosya oluşturan veya bir dosyayı açan method
    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Dosya aç", "", "Text documents (*.txt)")

        if path:
            try:

                with open(path, mode='r') as f:

                    text = f.read()
                    text1 = text

                    try:
                        text = text.encode("ansi").decode("utf-8")

                        self.path = path
                        self.editor.setPlainText(text)
                        self.update_title()

                    except:
                        self.path = path
                        self.editor.setPlainText(text1)
                        self.update_title()

            except Exception as e:
                self.dialog_critical(str(e))

    # Dosyayı kaydeden method
    def file_save(self):

        # Eğer dosya oluşturulmadıysa, program yeni açıldıysa path. None olacağından dolayı dosyayı kaydederken
        # önce kullanıcıdan FileDialog ile bir yol alıcak ve one kaydedecek ama eğer dosya zaten kaydedildiyse
        # save_to_path mothodunu çalıştıracak
        if self.path == None:

            path, _ = QFileDialog.getSaveFileName(self, "Dosyayı kaydet", ".txt", "Text files (*.txt)")

            if not path:
                # If dialog is cancelled, will return ''
                return

            self.path = path
            self.save_to_path(self.path)
        else:
            self.save_to_path(self.path)

    # Dosya üzerinde yapılan değişiklikleri kaydeden method
    def save_to_path(self, path):
        text = str(self.editor.toPlainText())
        try:
            with open(str(path), encoding="ansi", mode='w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        self.update_title()

    # Dosya yazdırılmak istenirse bu method çalışacak
    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    # Bir dosya açıldığında başlığı o dosyanın adı olarak değiştiren method
    def update_title(self):
        self.setWindowTitle("%s ~ GÖK DEFTER" % (path.basename(self.path) if self.path else "İsimsiz"))

    # Eğer satır sonu sözcük kaydırma açıksa kapatan, kapalıysa açan method
    def change_word_wrap(self):

        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)
        if self.editor.lineWrapMode():self.editor.setStatusTip("Sözcük kaydırma: kapalı")
        else:self.editor.setStatusTip("Sözcük kaydırma: açık")

    # Telegramı açan method
    def open_telegram(self):
        wbopen("https://t.me/SukruGokk")

if __name__ == '__main__':
    app = QApplication(argv)
    app.setApplicationName("Gök Defter")

    window = MainWindow()
    exit(app.exec_())
