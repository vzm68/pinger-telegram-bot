from data.config import log_path


def tail_log():
    with open(log_path, 'r') as file:
        return file.readlines()[-10:]
