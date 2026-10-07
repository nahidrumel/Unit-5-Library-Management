# CS 1101-01 Assignment Activity Unit 5
# Library management: four separate exercises
# Run this file to see all four outputs in order.


# Question 1
# List methods: Parker (2021, ch. 3); Python Software Foundation (n.d.).
book_titles = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
# Add arrivals separately, then withdraw the damaged title.
book_titles.append("A Golden Age")
book_titles.append("Lalsalu")
book_titles.remove("Moby Dick")
# Sort the existing list before showing the current catalogue.
book_titles.sort()
print("Final book list:", book_titles)


# Question 2
# Tuple item assignment: Parker (2021, ch. 3).
borrower = ("John Doe", "B1023", "2025-10-15")
print("Original borrower:", borrower)
try:
    borrower[0] = "Jane Doe"
except TypeError as error:
    print("Modification attempt:", error)
# The same record is inspected after the rejected change.
print("Borrower after attempt:", borrower)
print("Number of fields:", len(borrower))
for detail in borrower:
    print(detail)


# Question 3
# Unpacking: Parker (2021, ch. 3); Python Software Foundation (n.d.).
# First publication year: Paulo Coelho and Christina Oiticica Foundation (n.d.).
book_info = ("The Alchemist", "Paulo Coelho", 1988)
title, author, publication_year = book_info
print("Title:", title)
print("Author:", author)
print("Publication year:", publication_year)


# Question 4
# Indexing and slicing: Parker (2021, ch. 3).
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
# Week 1 uses index 0; the slice stop excludes week 6.
borrowed_books[0] = 20
first_week = borrowed_books[0]
weeks_2_to_5 = borrowed_books[1:5]
print("Week 1 after correction:", first_week)
print("Updated weekly borrowing:", borrowed_books)
print("Weeks 2 to 5:", weeks_2_to_5)
