import os
import json

_basedir = os.path.abspath(os.path.dirname(__file__))

# Load strings from json
# Russian language
_strings_ru = json.loads(open(os.path.join(_basedir, 'strings_ru.json'), 'r', encoding='utf8').read())

# Uzbek language
_strings_uz = json.loads(open(os.path.join(_basedir, 'strings_uz.json'), 'r', encoding='utf8').read())


def get_string(key, language='ru') -> str:
    if language == 'ru':
        return _strings_ru.get(key, 'no_string')
    elif language == 'uz':
        return _strings_uz.get(key, 'no_string')
    else:
        raise Exception('Invalid language')


def from_help_request_distance(request: dict, language: str) -> str:
    distance = request['distance']
    request = request['request']
    return get_string('help_request.template', language).format(distance=distance, name=request.user.name, 
                                                                type=request.help_type,
                                                                description=request.description)