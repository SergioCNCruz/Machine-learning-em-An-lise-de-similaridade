from fastapi import FastAPI, File, UploadFile
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from PIL import Image
import io
import os

app = FastAPI()

# Carregando o modelo de ML (exemplo com TensorFlow)
model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False)

def extract_features(image: Image.Image):
    image = image.resize((224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = tf.keras.applications.resnet50.preprocess_input(image_array)
    features = model.predict(image_array)
    flattened_features = features.flatten()
    normalized_features = flattened_features / np.linalg.norm(flattened_features)
    return normalized_features

@app.post("/image/similarity/")
async def find_image_similarity(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    query_features = extract_features(image)

    # Implemente a lógica de comparação aqui

    return {"message": "Similarity calculated", "similar_images": similar_images}

if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(app, host=host, port=port)
