from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QTextEdit, QPushButton, QInputDialog

app = QApplication([])

# Основные виджеты
main_window = QWidget()
main_window.setWindowTitle('Умные заметки')
main_window.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')

field_text = QTextEdit()

# Кнопки
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

# Расположение виджетов
layout = QVBoxLayout()

# Правая колонка
right_column_layout = QVBoxLayout()
right_column_layout.addWidget(list_notes_label)
right_column_layout.addWidget(list_notes)
right_column_layout.addWidget(button_note_create)
right_column_layout.addWidget(button_note_del)
right_column_layout.addWidget(button_note_save)
right_column_layout.addWidget(field_text)

# Добавлени�� колонок в основной лэйаут
layout.addLayout(right_column_layout, stretch=1)

# Назначение лэйаута для окна
main_window.setLayout(layout)

# Инициализация переменной notes
notes = []

# Функции приложения
def show_note():
    selected_item = list_notes.selectedItems()[0].text()
    for note in notes:
        if note[0] == selected_item:
            field_text.setPlainText(note[1])

def add_note():
    note_name, ok = QInputDialog.getText(main_window, "Добавить заметку", "Название заметки:")
    if ok and note_name:
        note = [note_name, '']
        notes.append(note)
        list_notes.addItem(note[0])

def save_note():
    selected_item = list_notes.selectedItems()
    if selected_item:
        key = selected_item[0].text()
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                print(notes)

# Обработка событий
list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)

# Запуск приложения
main_window.show()

app.exec_()