
def get_val_by_key(nested_dict, key, delimiter='.'):
    """
    Traverse nested dict, get value by combined key (e.g. meta.created_at)
    :param nested_dict: dictionary to be searched. 
    :param key: search key
    :param delimiter: if nested key used delimiter to infer nesting
    :return: value for key
    """
    partial_keys = key.split(delimiter)
    for k in partial_keys:
        nested_dict = nested_dict[k]
    return nested_dict

def flatten(nested_dict, delimiter='.'):
    """
    Flatten nested dict
    :param nested_dict: dictionary
    :param delimiter: nested keys connector
    :return: flat dictionary
    """
    result = {}
    def _f(d, result=result, keys=[]): # TODO find better solution without
        for k, val in d.items():
            if not isinstance(val, dict):
                key = delimiter.join(keys + [k]) if keys else k
                result[key] = val
            else:
                _f(val, result, keys + [k])
    _f(nested_dict)
    return result



