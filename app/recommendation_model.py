from sklearn.neighbors import NearestNeighbors

def train_collaborative_model(user_item_matrix):
    model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=5)
    model.fit(user_item_matrix)
    return model
