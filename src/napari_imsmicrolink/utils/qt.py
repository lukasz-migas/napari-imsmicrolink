"""Qt utilities."""
def confirm(parent, message: str, title: str = "Are you sure?") -> bool:
    """Confirm action"""
    from qtpy.QtWidgets import QMessageBox

    ret = QMessageBox.question(parent, title, message)  # noqa
    if ret in [QMessageBox.Yes, QMessageBox.Ok]:
        return True
    return False


def warn(parent, message: str):
    """Create pop up dialog with warning message."""
    from qtpy.QtWidgets import QMessageBox

    dlg = QMessageBox(parent=parent, icon=QMessageBox.Warning)
    dlg.setWindowTitle("Warning")
    dlg.setText(message)
    dlg.exec_()