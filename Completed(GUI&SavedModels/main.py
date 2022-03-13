# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:33:26 2021

@author: utku
"""

import sys
from PyQt5.QtWidgets import QApplication
from carpred_window import PredWindow

app = QApplication(sys.argv)
carpred = PredWindow()
sys.exit(app.exec())