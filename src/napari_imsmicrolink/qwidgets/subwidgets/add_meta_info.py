from qtpy.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy,
)


class AddMetadataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.meta_info_label = QLabel()
        self.meta_info_label.setText("You can load previously saved metadata here. These files usually"
                                     " have the extension '-meta.json' and specify all necessary information"
                                     " regarding the IMS-Microscopy registration.")
        self.meta_info_label.setWordWrap(True)
        self.layout().addWidget(self.meta_info_label)

        self.add_meta_data = QPushButton("Select metadata file")
        self.layout().addWidget(self.add_meta_data)
