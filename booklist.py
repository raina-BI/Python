# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:32:54 2024

@author: raina
"""

class BookDetails:
  def __init__(self,booktitle,genre,author,yearofpub):
    self.booktitle=booktitle
    self.genre= genre
    self.author=author
    self.yearofpublication=yearofpub

    self.book={
        "BookTitle":self.booktitle,
        "Genre":self.genre,
        "Author":self.author,
        "Year Of Publication":self.yearofpublication
    }

  def add_books(self,book_list):
   book_list.append(self.book)
     
  def view_books(self,book_list):
   print(book_list)
     
book_list=[]

new_book = BookDetails("To kill a mockingbird","Fiction","Harper Lee",1960)
new_book.add_books(book_list)
    
new_book.view_books(book_list)
