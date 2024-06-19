# Sample user data (assuming ratings and genre preference)
users = {
  "user1": [
    {"title": "Book A", "genre": "Fantasy", "author": "Author1", "rating": 4},
    {"title": "Book B", "genre": "Sci-Fi", "author": "Author2", "rating": 5},
  ]
}

# Sample book data
books = {
  "book1": {"title": "Book C", "genre": "Fantasy", "author": "Author3"},
  "book2": {"title": "Book D", "genre": "Sci-Fi", "author": "Author1"},
  "book3": {"title": "Book E", "genre": "Mystery", "author": "Author4"},
}

# Recommend books for user1 (M=2 top recommendations)
def recommend_books(user_id, user_data, book_data, num_recommendations):
  user_genres = [book["genre"] for book in user_data]
  user_authors = [book["author"] for book in user_data]
  recommendations = []
  for book_id, book_details in book_data.items():
    genre_score = sum(genre in user_genres for genre in book_details["genre"])
    author_score = sum(author in user_authors for author in book_details["author"])
    similarity_score = genre_score + author_score
    recommendations.append((book_id, similarity_score))
  recommendations.sort(key=lambda x: x[1], reverse=True)
  return [book_data[book_id]["title"] for book_id, _ in recommendations[:num_recommendations]]

recommended_books = recommend_books("user1", users["user1"], books, 2)
print(f"Recommended books for user1: {recommended_books}")
