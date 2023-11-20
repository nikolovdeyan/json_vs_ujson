import os
import json
from faker import Faker
from homework.timing import timing



@timing
def json_generator(num_items=1, filename=None):
    """Generates fake json data optionally saving to a file.

    Args:
        num_items (int, optional): The number of items to be generated. Defaults to 1.
        filename (str, optional): Filename to save the json data as. If not provided 
        the generated json is returned. Defaults to None.

    Returns:
        str: If filename is not provided else the data is saved to the file and returns None
    """
    fake = Faker()

    selected_fields = ('name', 'username', 'sex', 'job', 'company', 'ssn', 'residence', 'website', 'address')
    result = [fake.profile(selected_fields) for profile in range(num_items)]
    
    if filename is None:
        return json.dumps(result)
    else:
        if not str(filename).endswith(".json"):
            filename = filename + ".json"
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir_path, filename)
        with open(json_path, "w") as json_file:
            json_file.writelines(json.dumps(result))
