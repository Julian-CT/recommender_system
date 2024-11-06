from flask import Flask, jsonify, request
from recommendation_model import train_collaborative_model
from load_datasets import load_data
import requests

app = Flask(__name__)

# Carregar e treinar o modelo
books, ratings, users, user_item_matrix = load_data()
model = train_collaborative_model(user_item_matrix)

# Função para obter recomendações de usuários
def get_user_recommendations(user_id, n_recommendations=5):
    if user_id not in user_item_matrix.index:
        return {"error": "User not found"}
    
    distances, indices = model.kneighbors(user_item_matrix.loc[user_id].values.reshape(1, -1))
    similar_users = user_item_matrix.index[indices.flatten()].tolist()
    
    recommendations = []
    for similar_user in similar_users:
        user_ratings = user_item_matrix.loc[similar_user]
        unseen_items = user_ratings[(user_ratings > 0) & (user_item_matrix.loc[user_id] == 0)].index.tolist()
        recommendations.extend(unseen_items)

    recommendations = list(set(recommendations))[:n_recommendations]
    recommendations_info = [{"ISBN": item} for item in recommendations if item in books['ISBN'].values]
    return {"user_id": user_id, "recommendations": recommendations_info}

# Endpoint para recomendações de usuário
@app.route("/users/<int:user_id>/recommendations", methods=["GET"])
def get_recommendations(user_id):
    recommendations = get_user_recommendations(user_id)
    if "error" in recommendations:
        return jsonify(recommendations), 404
    return jsonify(recommendations)

# Endpoint para itens semelhantes via API R
@app.route("/items/<item_id>/similar", methods=["GET"])
def get_similar_items(item_id):
    try:
        response = requests.get(f"http://127.0.0.1:8000/items/{item_id}/similar")
        return response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Could not retrieve similar items from R API", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
