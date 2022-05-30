import json


DATA_PATH = "candidates.json"


def load_data(path=DATA_PATH):
    """загружаем данные с кандидатами"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def candidates_get_all():
    """получаем список всех кандидатов"""
    data = load_data()
    return data


def candidates_get_by_pk(pk):
    """получаем кандидатов по его РК"""
    candidates = load_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate


def candidates_get_by_skill(skill_name):
    """получаем кандидатов по навыкам"""
    candidates = load_data()
    skilled_candidates = []
    skill_name = skill_name.lower()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
    return skilled_candidates



