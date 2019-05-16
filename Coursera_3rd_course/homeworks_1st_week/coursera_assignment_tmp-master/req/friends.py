
import requests
import json

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

def get_id(uid):
    response_id = requests.get('https://api.vk.com/method/users.get',
                                params={'v': 5.71,
                                        'access_token': ACCESS_TOKEN,
                                        'user_ids': uid})

    user_id = response_id.json()['response'][0]['id']
    return user_id


def get_friends_bdate(uid):
    response_bday = requests.get('https://api.vk.com/method/friends.get',
                                    params={'v': 5.71,
                                            'access_token': ACCESS_TOKEN,
                                            'user_id': get_id(uid), 'fields': 'bdate'})

    friends_list = response_bday.json()['response']['items']
    friends_bdate = []
    for friend in friends_list:
        try:
            day, month, year = friend['bdate'].split('.')
            friends_bdate.append(year)
        except:
            pass
    return friends_bdate


def calc_age(uid):
    ages = [(2019 - int(year), 1) for year in get_friends_bdate(uid)]
    age_count = {}
    i = 0
    while len(ages) > i:
        age = ages[i]
        if age[0] not in age_count:
            age_count[age[0]] = age[1]
        else:
            age_count[age[0]] += age[1]
        i += 1

    age_count = [(key, value) for key, value in age_count.items()]

    age_count = sorted(age_count, key=lambda x: x[0])
    age_count.reverse()
    age_count.sort(key=lambda x: x[1])
    age_count.reverse()
    
    return age_count


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
