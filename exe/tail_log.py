from data.config import log_path


def tail_log():
    """
    I need this func to get last ten
    logs strings.
    """
    with open(log_path, 'r') as file:
        return file.readlines()[-10:]
