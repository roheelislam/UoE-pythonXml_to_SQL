from xml.dom import minidom

# parse an xml file by name
# mydoc = minidom.parse("books.xml")


doc = minidom.parse("books.xml")

name = doc.getElementsByTagName("catalog")[0]
print(name.firstChild.data)

books =doc.getElementsByTagName("book")
for book in books:
    author = book.getElementsByTagName("author")[0]
    title = book.getElementsByTagName("title")[0]
    genre = book.getElementsByTagName("genre")[0]
    price = book.getElementsByTagName("price")[0]
    publish_date = book.getElementsByTagName("publish_date")[0]
    description = book.getElementsByTagName("description")[0]
    print("author:%s,\n title:%s,\n genre:%s,\n price:%s, \n publish_date:%s, \n description:%s \n\n" %
        (author.firstChild.data, title.firstChild.data, genre.firstChild.data, price.firstChild.data, publish_date.firstChild.data, description.firstChild.data))



    





# print(mydoc.nodeName)
# print(mydoc.fir)

# items = mydoc.getElementsByTagName('author')
# print(items.values)
# one specific item attribute
# print('Item #2 attribute:')
# print(items.)

# # all item attributes
# print('\nAll attributes:')
# for elem in items:
#     print(elem.attributes['author'].value)

# # one specific item's data
# print('\nItem #2 data:')
# print(items[1].firstChild.data)
# print(items[1].childNodes[0].data)

# # all items data
# print('\nAll item data:')
# for elem in items:
#     print(elem.firstChild.data)