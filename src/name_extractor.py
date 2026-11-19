import re


def extract_name(text):

    pattern = r"Name:\s*(.*)"

    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    else:
        return "Name not found"