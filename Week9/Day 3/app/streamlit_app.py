import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path


st.set_page_config(
    page_title="ISIC Melanoma Classifier",
    layout="centered"
)


MODEL_PATH = (
    Path(__file__).parent.parent.parent
    / "Day 1"
    / "models"
    / "melanoma_cnn.keras"
)

IMG_SIZE = (112, 112)


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


model = load_model()


st.title("ISIC Melanoma Classifier")

st.write(
    "Upload an ISIC skin lesion image to classify it as "
    "Benign or Malignant."
)


uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        width="stretch"
    )

    if st.button("Predict"):

        img = image.resize(IMG_SIZE)

        img_array = np.array(img) / 255.0

        img_array = np.expand_dims(img_array, axis=0)

        pred_prob = float(
            model.predict(
                img_array,
                verbose=0
            )[0][0]
        )

        pred_class = (
            "Malignant"
            if pred_prob >= 0.5
            else "Benign"
        )

        confidence = (
            pred_prob
            if pred_prob >= 0.5
            else 1 - pred_prob
        )

        benign_prob = 1 - pred_prob
        malignant_prob = pred_prob

        if pred_class == "Malignant":
            st.error(f"Prediction: {pred_class}")
        else:
            st.success(f"Prediction: {pred_class}")

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.subheader("Prediction Probabilities")

        st.write(
            f"Benign: {benign_prob * 100:.2f}%"
        )
        st.progress(benign_prob)

        st.write(
            f"Malignant: {malignant_prob * 100:.2f}%"
        )
        st.progress(malignant_prob)