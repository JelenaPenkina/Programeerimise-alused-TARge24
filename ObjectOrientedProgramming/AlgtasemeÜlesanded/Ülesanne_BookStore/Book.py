"""Book store."""
"""
__init__(self, title: str, author: str, price: float, rating: float) - 
konstruktor, mis määrab raamatule tiitli, autori, hinna ja reitingu 
(hinnangu ehk populaarsuse).
"""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """Initialize book model."""
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __eq__(self, other) -> bool:
        """Check equality."""
        return isinstance(other, Book) and other.title == self.title and other.author == self.author

    def __repr__(self):
        """Represent book object."""
        return f'Book(title="{self.title}", author="{self.author=}", price=, {self.price=}, rating= {self.rating=})'
