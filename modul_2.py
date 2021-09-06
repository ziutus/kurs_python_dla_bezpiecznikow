import re

if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    for log in logs.split('\n'):
        log = log.replace(', ', ' ')
        log_split = log.split(' ')

        path = log_split[0]

        if re.search('\/[^/]*admin.php$|\/[^/]*user.php$', path) and not re.search('.*admin.*\/|.*user.*\/', path):
            print(path)
