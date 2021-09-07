import re

def is_admin_user_file(filepath):
    if re.search('\/[^/]*admin[^/]*.php$|\/[^/]*user[^/]*.php$', filepath):
        return True
    return False


if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    for log in logs.split('\n'):
        log = log.replace(', ', ' ')
        log_split = log.split(' ')

        path = log_split[0]

        if is_admin_user_file(path):
            print(path)
