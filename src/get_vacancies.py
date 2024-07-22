from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вокансий с HH.ru"""

    @abstractmethod
    def get_response(self, keyword, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass
