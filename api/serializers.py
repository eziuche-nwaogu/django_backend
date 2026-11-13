from rest_framework import serializers
from books.models import Book, Author


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['id', 'author_first_name', 'author_last_name']


# class BookSerializer(serializers.ModelSerializer):
#     book_author = AuthorSerializer(read_only=True)

#     class Meta:
#         model = Book
#         fields = ['id', 'book_title', 'book_author', 'book_published_date', 'book_isbn', 'price', 'is_available', 'created_at']







class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        # write_only=True
    )

    author_details = AuthorSerializer(
        source='author',
        read_only=True
    )

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        # Add any custom validation logic here if needed
        if data['book_title'] == '':
            raise serializers.ValidationError("Title cannot be empty.")
        elif len(data['book_title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        elif data['book_title'] == data['author'].author_first_name or data['book_title'] == data['author'].author_last_name:
            raise serializers.ValidationError("Title and content cannot be the same.")
        return data