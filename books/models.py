from django.db import models

# Create your models here.

class Author(models.Model):
    author_first_name = models.CharField(max_length=100,  
                                   null=False, 
                                   blank=False)
    author_last_name = models.CharField(max_length=100, 
                                  null=False, 
                                  blank=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        db_table = "authors"

    def __str__(self):
        return f"{self.author_first_name} {self.author_last_name}"

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    book_published_date = models.DateField()
    book_isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "books"

    def __str__(self):
        return self.book_title