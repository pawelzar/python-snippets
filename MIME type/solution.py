import re


def get_extensions(extensions, files):
    """
    Provide list of known extensions and list of files.
    Returns list of corresponding extension for each file.
    """
    mime = {ext.lower(): mt for ext, mt in [e.split() for e in extensions]}
    assigned = []

    for name in files:
        extension = re.search("\w*\.*(.\w+|.)$", name)
        assigned.append(mime.get(extension.group(1).lower(), "UNKNOWN"))

    return assigned

if __name__ == "__main__":
    n = int(input())
    q = int(input())
    mime = {ext.lower(): mt for ext, mt in [input().split() for i in range(n)]}

    for j in range(q):
        extension = re.search("\w*\.*(.\w+|.)$", input())
        print(mime.get(extension.group(1).lower(), "UNKNOWN"))
