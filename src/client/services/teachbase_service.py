import base64

import requests
from django.core.cache import cache
from requests import Response
from rest_framework.exceptions import AuthenticationFailed

from teachbase import settings

TEACHBASE_TOKEN_CACHE_KEY = 'teachbase_token'


def get_teachbase_jwt() -> str | None:
    url: str = 'https://go.teachbase.ru/oauth/token'
    basic_str: bytes = f'{settings.TEACHBASE_CLIENT_ID}:{settings.TEACHBASE_SECRET_KEY}'.encode('ascii')
    basic: bytes = base64.b64encode(basic_str)
    data: dict = {
        'grant_type': 'client_credentials',
    }
    headers: dict = {
        'Authorization': f'Basic {basic.decode("ascii")}'
    }
    res: Response = requests.post(url, data=data, headers=headers)
    if res.status_code == 200:
        r: dict = res.json()
        cache.set(TEACHBASE_TOKEN_CACHE_KEY, r['access_token'], r['expires_in'])
        return r['access_token']
    else:
        return None


def teachbase_auth() -> dict:
    _token: str | None = cache.get(TEACHBASE_TOKEN_CACHE_KEY)
    if _token is None:
        _token: str | None = get_teachbase_jwt()
    if _token is not None:
        return {'Authorization': 'Bearer {}'.format(_token)}
    else:
        raise AuthenticationFailed(code=403, detail='Bad token Teachbase')
