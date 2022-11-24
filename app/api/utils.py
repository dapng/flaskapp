def config_parser(config_path):
    with open(config_path, 'r') as config_file:
        config = dict()
        lines = config_file.readlines()
        for line in lines:
            k, v = line.spli(' = ')
            config[k] = v
        return config