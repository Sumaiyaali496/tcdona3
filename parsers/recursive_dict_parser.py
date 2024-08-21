def dict_parser(dict_, out={}, prefix=""):

    if isinstance(dict_, list):
        for num, value in enumerate(dict_):
            key = ""
            if value == 0:
                key = prefix + "_ILA_AB"
            elif value == 1:
                key = prefix + "_ILA_BA"
            else:
                key = prefix + str(num)
            out = dict_parser(value, out, key)

    elif isinstance(dict_, dict):
        for key, value in dict_.items():
            if prefix != "":
                key = prefix + "_" + str(key)
            else:
                key = str(key)
            out = dict_parser(value, out, key)
    else:
        out[prefix] = dict_

    return out
