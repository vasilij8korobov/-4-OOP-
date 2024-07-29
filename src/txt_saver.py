from src.saver import Saver


class TXTSaver(Saver):
    """ Класс для записи в txt-файл """

    def __init__(self, filename):
        """ Конструктор класса """

        super().__init__(filename)

    def write_data(self, vacancies):
        """ Запись данных в txt """

        with open(self._filename, "a", encoding="utf=8") as file:
            file.write(vacancies)

    def get_data(self):
        """ Получение данных txt """

        with open(self._filename, encoding="utf-8") as file:
            return file.readlines()

    def del_data(self):
        """ Удаление данных из файла """

        with open(self._filename, "w", encoding="utf-8"):
            pass
