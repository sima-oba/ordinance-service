from json.decoder import JSONDecodeError

import dataclasses as dtclass
import json
import re


def rm_punct(string: str) -> str:
    return re.sub(r'\D', '', str(string))


def to_json(string: str) -> dict:
    try:
        return json.loads(string)
    except JSONDecodeError:
        return None
    except TypeError:
        return None


def export_feature_collection(objects: list, include_geometry=True):
    if not objects:
        return None

    features = []

    for index in range(len(objects)):
        obj = objects[index]

        if dtclass.is_dataclass(obj):
            obj = dtclass.asdict(obj)

        geometry = obj.pop('geometry', None)
        properties = {key: value for key, value in obj.items()}
        feat = {
            'id': index,
            'type': 'Feature',
            'properties': properties
        }

        if include_geometry:
            feat['geometry'] = geometry

        features.append(feat)

    return {
        'type': 'FeatureCollection',
        'features': features
    }
