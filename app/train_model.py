import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load dataset
df = pd.read_csv("data/Final_Upwork_Dataset.csv")

# Preprocess text data (job descriptions)
df['Description'] = df['Description'].fillna('').str.lower()

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['Description'])

# Save the TF-IDF model and matrix
with open("models/job_matcher.pkl", "wb") as f:
    pickle.dump({
        'tfidf': tfidf,
        'tfidf_matrix': tfidf_matrix,
        'job_ids': df['Job_URL'].tolist()  # For reference
    }, f)

print("Model saved to models/job_matcher.pkl")