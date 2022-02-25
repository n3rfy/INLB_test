#Функция принимает на вход список сводной информации по абитуриентам (candidates)
#и возвращает список с именами 20 человек, набравших наибольшее СУММАРНОЕ 
#количество баллов (с учетом extra баллов), которые станут студентами 
#университета. Пример входных данных приведен ниже.
#Пример входных данных:

candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
]

def find_top_20(candidates: list) -> list:
    s_candidates = sorted(
        candidates,
        key = lambda c: (
            -sum(c['scores'].values()),
            -sum([c['scores']['math'], c['scores']['computer_science']])
        )
    )
    return [candidate['name'] for candidate in s_candidates[:20]]

