#!/usr/bin/env python3

import grp
import logging
import os
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine, QQmlEngine

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    # Insert some argv?
    if "--remote" not in sys.argv:
        # Set up for display on the 7" screen
        os.environ["QT_QPA_PLATFORM"] = "eglfs"
        os.environ["QT_QPA_EGLFS_HIDECURSOR"] = "1"
        # These have been needed on older versions of the OS
        # os.environ["DISPLAY"] = ""
        # os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = (
        #     "/usr/lib/aarch64-linux-gnu/qt5/plugins/platforms")
        # os.environ["QT_QPA_EGLFS_INTEGRATION"] = "eglfs_kms"
        # os.environ["QT_QPA_EGLFS_ALWAYS_SET_MODE"] = "1"

    # Check we're in the render group so we have HW acceleration
    render_grp = grp.getgrnam("render")
    if render_grp.gr_gid not in os.getgroups():
        logger.warning("Not in the render group so won't get HW acceleration")

    # Create an application and a Qt event loop to pass to asyncio
    app = QApplication(sys.argv)

    # find the UI code and set it up
    QML = "gui.qml"
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load(QML)

    app.exec_()
