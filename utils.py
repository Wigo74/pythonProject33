import json
#from pprint import pprint as pp

DATA_PATH = "candidates.json"


def load_candidates_from_json():
    """получаем список всех кандидатов"""
    with open(DATA_PATH, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidates():
    candidates = load_candidates_from_json()
    return candidates


def get_candidates_for_id(candidate_id):
    """получаем кандидатов по его РК"""
    candidates = get_candidates()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = get_candidates()
    candidates_found = []
    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            candidates_found.append(candidate)
    return candidates_found


def candidates_get_by_skill(skill_name):
    """получаем кандидатов по навыкам"""
    candidates = get_candidates()
    skilled_candidates = []
    skill_name = skill_name.lower()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
    return skilled_candidates


#pp(get_candidates(7))
