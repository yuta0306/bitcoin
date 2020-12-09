from requests.models import Response, parse_header_links
from fetch import *
import requests
from typing import Dict, Final

def get_ticker(types: Union[str, dict]) -> Union[AnyStr, Dict, Response]:
    ENDPOINT: Final[AnyStr] = 'https://coincheck.com/api/ticker'

    res = requests.get(ENDPOINT, params={'timestamp': 1607498523})

    if types == str:
        output: AnyStr = tinify_response(res, str)
    elif types == dict:
        output: Dict = tinify_response(res, dict)
    else:
        output = None

    return output