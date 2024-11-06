import pandas as pd

def load_data():
    books = pd.read_csv("data/Books.csv", encoding='ISO-8859-1')
    ratings = pd.read_csv("data/Ratings.csv", encoding='ISO-8859-1')
    users = pd.read_csv("data/Users.csv", encoding='ISO-8859-1')
    
    # Preprocessamento básico
    user_item_matrix = ratings.pivot(index="User-ID", columns="ISBN", values="Book-Rating").fillna(0)
    
    return books, ratings, users, user_item_matrix
