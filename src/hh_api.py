import requests
from requests import Response
from src.get_vacancies import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """класс для подключения к HH.ru"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page):
        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        return requests.get(self.__url, params=self.__params)

    def get_vacancies(self, keyword, per_page):
        return self.get_response(keyword, per_page).json()["items"]
