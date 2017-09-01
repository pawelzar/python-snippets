import re


def mime_type(extensions, files):
    """
    Determines mime types after files extensions.

    :param extensions: list of extensions and corresponding mime types
    separated by space
    :param files: list of file names
    :return: list of mime types for each of given file names
    """
    mime = {ext.lower(): mt for ext, mt in [e.split() for e in extensions]}
    assigned = []

    for name in files:
        extension = re.search(r'\w*\.*(.\w+|.)$', name)
        assigned.append(mime.get(extension.group(1).lower(), 'UNKNOWN'))

    return assigned


if __name__ == '__main__':
    N = int(input())
    Q = int(input())
    EXTENSIONS = [input() for i in range(N)]
    FILES = [input() for i in range(Q)]

    print('\n'.join(mime_type(EXTENSIONS, FILES)))
