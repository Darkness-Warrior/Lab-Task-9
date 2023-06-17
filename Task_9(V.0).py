from abc import ABC, abstractmethod


class GUIFactory(ABC): # Абстрактная фабрика
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory): # Конкретная фабрика для Windows
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory): # Конкретная фабрика для Mac
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Button(ABC): # Абстрактный продукт "Кнопка"
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button): # Конкретный продукт "Кнопка" для Windows
    def paint(self):
        print("Отрисовка кнопки для Windows")


class MacButton(Button): # Конкретный продукт "Кнопка" для Mac
    def paint(self):
        print("Отрисовка кнопки для Mac")


class Checkbox(ABC): # Абстрактный продукт "Флажок"
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox): # Конкретный продукт "Флажок" для Windows
    def paint(self):
        print("Отрисовка флажка для Windows")


class MacCheckbox(Checkbox):   # Конкретный продукт "Флажок" для Mac
    def paint(self):
        print("Отрисовка флажка для Mac")



class DialogBuilder(ABC): # Строитель диалогового окна
    def __init__(self):
        self.dialog = Dialog()

    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_message(self, message):
        pass

    @abstractmethod
    def set_button(self):
        pass

    @abstractmethod
    def set_checkbox(self):
        pass



class WindowsBuilder(DialogBuilder): # Конкретный строитель диалогового окна для Windows
    def set_title(self, title):
        self.dialog.title = title

    def set_message(self, message):
        self.dialog.message = message

    def set_button(self):
        factory = WindowsFactory()
        self.dialog.button = factory.create_button()

    def set_checkbox(self):
        factory = WindowsFactory()
        self.dialog.checkbox = factory.create_checkbox()


class MacBuilder(DialogBuilder): # Конкретный строитель диалогового окна для Mac
    def set_title(self, title):
        self.dialog.title = title

    def set_message(self, message):
        self.dialog.message = message

    def set_button(self):
        factory = MacFactory()
        self.dialog.button = factory.create_button()

    def set_checkbox(self):
        factory = MacFactory()
        self.dialog.checkbox = factory.create_checkbox()


class Dialog: # Объект диалогового окна
    def __init__(self):
        self.title = ""
        self.message = ""
        self.button = None
        self.checkbox = None

    def show(self):
        print("Заголовок:", self.title)
        print("Сообщение:", self.message)
        if self.button is not None:
            self.button.paint()
        if self.checkbox is not None:
            self.checkbox.paint()



class Primer:
    def __init__(self, builder):
        self.builder = builder

    def create_simple_dialog(self):
        self.builder.set_title("Простой диалог")
        self.builder.set_message("Добро пожаловать!")
        self.builder.set_button()

    def create_complex_dialog(self):
        self.builder.set_title("Сложный диалог")
        self.builder.set_message("Выберите настройки:")
        self.builder.set_button()
        self.builder.set_checkbox()


if __name__ == "__main__":
    os_name = "Windows"
    if os_name == "Windows":
        builder = WindowsBuilder()
    elif os_name == "Mac":
        builder = MacBuilder()
    director = Primer(builder)
    director.create_complex_dialog()
    dialog = builder.dialog
    dialog.show()