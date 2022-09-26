def list_urls_from_file(file: str) -> [str]:
    """
    parses files in order to find all urls in it and returns a list of them
    :param file: filename
    :return: list of urls
    """

    with open(f'data/{file}') as f:
        text = f.read()

    return list_urls(text)


def list_urls(text: str) -> [str]:
    """
    parses a string in order to find all urls in it and returns a list of them
    :param text: string to parse
    :return: list of urls
    """

    import re

    return re.findall(r'((?:(?:https|http)://)?(?:\S*)(?:\.com|\.ru)(?:[^\s\.\[]*))', text)


def list_isbn_from_file(file: str) -> [str]:
    """
    parses files in order to find all ISBN codes in it and returns a list of them
    :param file: filename
    :return: list of ISBN codes
    """

    with open(f'data/{file}') as f:
        text = f.read()

    return list_isbn(text)


def list_isbn(text: str) -> [str]:
    """
    parses a string in order to find all ISBN codes in it and returns a list of them
    :param text: string to parse
    :return: list of ISBN codes
    """

    import re

    return re.findall(r'((?:-?\d){10}(?:-?\d){3}?)', text)
