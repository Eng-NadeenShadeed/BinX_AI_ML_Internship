from fastapi import FastAPI, UploadFile, File, HTTPException
import numpy as np
from PIL import Image
import io
import tensorflow as tf

app = FastAPI(title="Melanoma Classifier API")

# Load model once at startup
from pathlib import Path


MODEL_PATH = Path(__file__).parent.parent.parent / "Day 1" / "models" / "melanoma_cnn.keras"
model = tf.keras.models.load_model(MODEL_PATH)
IMG_SIZE = (112, 112)

@app.get("/")
def root():
    return {"message": "Melanoma Classifier API is running ✓"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=400,
            detail="Only JPEG and PNG images are accepted"
        )

    # Read and preprocess — identical to training
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    pred_prob = float(model.predict(img_array, verbose=0)[0][0])
    pred_class = "Malignant" if pred_prob >= 0.5 else "Benign"
    confidence = pred_prob if pred_prob >= 0.5 else 1 - pred_prob

    return {
        "prediction": pred_class,
        "confidence": round(confidence, 4),
        "filename": file.filename
    }