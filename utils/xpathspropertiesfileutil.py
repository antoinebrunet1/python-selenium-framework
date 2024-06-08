from jproperties import Properties


def get_xpath(name_of_file, name_of_xpath):
    configs = Properties()

    with open(f"xpaths/{name_of_file}", "rb") as read_prop:
        configs.load(read_prop)

    return configs.get(name_of_xpath).data
