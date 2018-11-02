import requests

api_key = ''  # Your API key here
base_url = 'https://steamladder.com/api/v1'
steam_id = ''  # The SteamID64 you want to lookup here


def get_worldwide_xp_rank(steam_id):
    r = requests.get('{}/profile/{}/'.format(base_url, steam_id), headers={
        'Authorization': 'Token {}'.format(api_key)
    })

    print("[GET] {}".format(r.url))
    if r.status_code == 200:
        worldwide_xp_rank = r.json()['ladder_rank']['worldwide_xp']
        print("Worldwide XP rank: {}".format(worldwide_xp_rank))
    elif r.status_code == 429:
        print("Request rate limited: {}".format(r.text))
    elif r.status_code == 401:
        print("Not authorized: {}".format(r.text))
    elif r.status_code == 404:
        print("Not found: {}".format(r.text))


get_worldwide_xp_rank(steam_id)
