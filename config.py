from pathlib import Path

ROOT_PATH = Path(__file__).parent
VACANCIES_PATH_JSON = ROOT_PATH.joinpath("data", "vacancies.json")
VACANCIES_PATH_TXT = ROOT_PATH.joinpath("data", "vacancies.txt")