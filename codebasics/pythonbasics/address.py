book = {}

book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 8989898989
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 8222228989
}

import json
s = json.dumps(book)
with open('C://Users//archanaseelan//PycharmProjects//codebasics//book.txt', 'w') as f:
    f.write(s)