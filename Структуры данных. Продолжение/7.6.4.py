book = {'Petr': '546810', 'Katya': '241815'}
book_keys = list(book.keys())
book_new = {}
for i in range(len(book)):
    book_new[book[book_keys[i]]] = book_keys[i]
print(book_new)
