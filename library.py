class Book:   # use uppercase
  def __init__(self, title, author, isbn):   # self refers to a specific instance, rest after are parameters
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_borrowed = False

    # the class is a blueprint in which can be used to create all other objects.

    def __str__(self):    # how the object as its alr defined, shld be represented as a string.
         


# this below is an instance, which is an object made using the class which is the blueprint.
book1 = Book("It ends with us", "Colleen Hoover", "978-1-5011-1036-8")



# from michael coding instructor channel, he explains SO WELL omg
# just me 2am core

