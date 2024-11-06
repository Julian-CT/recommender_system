library(plumber)
library(dplyr)
library(textTinyR)
library(tm)

load_books_data <- function() {
  books <- read.csv("data/Books.csv", stringsAsFactors = FALSE, encoding = "UTF-8")
  books$item_id <- 1000 + 1:nrow(books)
  books$content <- paste(books$Book.Title, books$Book.Author)
  return(books)
}

books <- load_books_data()

calculate_similarity_matrix <- function(data) {
  tfidf_matrix <- textTinyR::sparse_matrix(
    data = data$content, 
    stopword_vec = tm::stopwords("en"), 
    transform_vec_text = TRUE, 
    method = 'tfidf'
  )
  cosine_sim <- textTinyR::SIMILARITY(tfidf_matrix, method = "cosine")
  return(cosine_sim)
}

similarity_matrix <- calculate_similarity_matrix(books)

get_similar_items <- function(item_id, n = 5) {
  item_index <- which(books$item_id == item_id)
  if (length(item_index) == 0) {
    return(list(error = "Item not found"))
  }
  item_similarities <- similarity_matrix[item_index, ]
  similar_indices <- order(item_similarities, decreasing = TRUE)[2:(n+1)]
  similar_items <- books[similar_indices, c("item_id", "Book.Title", "Book.Author")]
  return(similar_items)
}

#* @get /items/<item_id>/similar
function(item_id) {
  item_id <- as.numeric(item_id)
  similar_items <- get_similar_items(item_id)
  return(similar_items)
}

#* @plumber
function(pr) {
  pr$setDebug(TRUE)
  pr
}
