import time
import re
from classes.vk_users import MatchingUser


def save_matching_users(data, criteria, token):
    data = filter_for_users(data, criteria)
    for user in data:
        print('Добавляем подходящего пользователя...')
        matching_user = MatchingUser(user['id'], token)
        matching_user.write_to_json()
        time.sleep(1)


def filter_for_users(data, criteria):
    scores = []
    for user in data:
        score = get_score_for_user(user, criteria)
        scores.append({'id': user['id'], 'score': score})

    scores.sort(key=lambda x: x['score'], reverse=True)
    return scores[:10]


def get_score_for_user(user, criteria):
    score = 0
    common_count = 10
    music = 5
    book = 3
    interest = 2
    movie = 1

    if user['common_count'] != 0:
        score += common_count*user['common_count']

    try:
        for i in criteria['music']:
            result = re.findall(i, user['music'], re.IGNORECASE)
            if result:
                score += music
    except KeyError:
        pass

    try:
        for i in criteria['books']:
            result = re.findall(i, user['books'], re.IGNORECASE)
            if result:
                score += book
    except KeyError:
        pass

    try:
        for i in criteria['interests']:
            result = re.findall(i, user['interests'], re.IGNORECASE)
            if result:
                score += interest
    except KeyError:
        pass

    try:
        for i in criteria['movies']:
            result = re.findall(i, user['movies'], re.IGNORECASE)
            if result:
                score += movie
    except KeyError:
        pass

    return score
