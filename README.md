# json_vs_ujson
Homework to compare the performance of std library JSON vs Ultra JSON module in Python.


#### Usage
The `test_data.json` file provided in the main directory contains 100,000 generated records.
```
import homework


homework.json_loads_list("test_data.json")
homework.json_loads_tuple("test_data.json")
homework.ujson_loads_list("test_data.json")
homework.ujson_loads_tuple("test_data.json")
```

#### Data Generation
A sample generation function is provided in `homework.datagen` that uses Faker to generate test data. Use the `json_generator()` as follows:

Generate json data in the terminal:
```
from homework.datagen import json_generator

json_generator(2) # generate two profiles
```

Generate json data in a file:
```
from homework.datagen import json_generator

json_generator(10000, "file_name.json")
```