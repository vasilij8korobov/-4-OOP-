class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        """ Конструктор класса """
        self._name: str = name
        self._alternate_url: str = alternate_url
        self._salary_from: int = salary_from
        self._salary_to: int = salary_to
        self._area_name: str = area_name
        self._requirement: str = requirement
        self._responsibility: str = responsibility

    def __str__(self) -> str:
        """ Строковое представление вакансии """

        return (f"Наименование вакансии: {self._name}\n"
                f"Ссылка на вакансию: {self._alternate_url}\n"
                f"Зарплата: от {self._salary_from} до {self._salary_to}\n"
                f"Место работы: {self._area_name}\n"
                f"Краткое описание: {self._requirement}\n"
                f"{self._responsibility}\n")

    def __lt__(self, other) -> bool:
        """ Метод сравнения от большего к меньшему """

        return other._salary_from > self._salary_from

    @classmethod
    def from_hh_dict(cls, vacancy_data: dict):
        """ Метод возвращает экземпляр класса в виде списка """

        salary = vacancy_data.get("salary")

        return cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"]["requirement"],
            vacancy_data["snippet"]["responsibility"],
        )

    def to_dict(self) -> dict:
        """ Метод возвращает вакансию в виде словаря """

        return {
            "name": self._name,
            "alternate_url": self._alternate_url,
            "salary_from": self._salary_from,
            "salary_to": self._salary_to,
            "area_name": self._area_name,
            "requirement": self._requirement,
            "responsibility": self._responsibility,
        }
