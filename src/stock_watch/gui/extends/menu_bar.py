from PySide6.QtWidgets import QMenuBar

from src.stock_watch.gui.extends.help_menu import HelpMenu
from src.stock_watch.gui.extends.view_menu import ViewMenu


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        view_menu = ViewMenu(self)
        help_menu = HelpMenu(self)

        self.addMenu(view_menu)
        self.addMenu(help_menu)
