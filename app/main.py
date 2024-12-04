from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the saved BERTopic model
with open("model/bertopic_model.pkl", "rb") as file:
    topic_model = pickle.load(file)

# Initialize FastAPI
app = FastAPI()

# Request model for input data
class DatasetDescription(BaseModel):
    description: str

@app.post("/predict-topic/")
def predict_topic(data: DatasetDescription):
    # Transform the new description to predict its topic
    new_topic, new_prob = topic_model.transform([data.description])
    
    if new_topic[0] != -1:  # If not an outlier
        topic_keywords = topic_model.get_topic(new_topic[0])
        keywords_nl = ", ".join([word for word, _ in topic_keywords])
        return {
            "topic_id": int(new_topic[0]),
            "keywords": keywords_nl,
            "probability": float(new_prob[0]),
        }
    else:
        return {
            "topic_id": "Outlier",
            "keywords": "No clear topic",
            "probability": float(new_prob[0]),
        }
