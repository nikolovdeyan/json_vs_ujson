import json
import ujson
from homework.timing import timing


@timing
def ujson_loads_list(filepath):
    with open(filepath) as f:
        ujson_list = ujson.load(f)

@timing
def ujson_loads_tuple(filepath):
    with open(filepath) as f:
        ujson_tuple = tuple(ujson.load(f))

@timing
def json_loads_list(filepath):
    with open(filepath) as f:
        json_list = json.load(f)

@timing
def json_loads_tuple(filepath):
    with open(filepath) as f:
        json_tuple = tuple(json.load(f))