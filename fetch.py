import json
import sys
from typing import Any, AnyStr, Tuple, List, Union, Dict, Iterable, Optional, Callable
import requests

def fetch(url: AnyStr, params: Dict={}) -> Optional[requests.models.Response]:
    res: requests.models.Response = requests.get(url, params=params)
    if res.status_code == 200:
        return res
    else:
        return None

def res_to_string(input_: requests.models.Response) -> Dict:
    output: Dict = input_.text
    
    return output

def decode(input_: AnyStr) -> Dict:
    output: Dict = json.loads(input_)

    return output

def encode(input_: Dict, indent: int=4) -> AnyStr:
    output: AnyStr = json.dumps(input_, ensure_ascii=True, indent=indent)

    return output

def pipe_parser(input_: Any, *args: Optional[Callable]) -> Any:
    funcs: Iterable = args
    output: Any = None
    for func in funcs:
        try:
            if output is not None:
                output = func(output)
            else:
                output = func(input_)
        except:
            sys.stderr(f'{func.__repr__} does not support the pipe.')
    
    return output

def tinify_response(input_: requests.models.Response, types: Union[dict, str]) -> Union[AnyStr, Dict]:
    if types == dict:
        funcs: List[Callable] = [res_to_string, decode]
    elif types == str:
        funcs: List[Callable] = [res_to_string, decode, encode]
    else:
        raise ValueError('types; dict or str')
    output: Union[AnyStr, Dict] = pipe_parser(input_, res_to_string, decode, encode)

    return output