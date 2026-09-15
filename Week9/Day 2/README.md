<div align="center">

# 🌸 Week 9 — Day 2

## Serving the Model with FastAPI

**Connecting the serialized CNN model to a REST API for local prediction serving.**

![WEEK 9](https://img.shields.io/badge/WEEK%209-f8a5c2?style=flat-square) ![DAY 2](https://img.shields.io/badge/DAY%202-C44569?style=flat-square\&logoColor=white) ![FASTAPI](https://img.shields.io/badge/FASTAPI-8B1E3F?style=flat-square\&logoColor=white) ![MELANOMA](https://img.shields.io/badge/MELANOMA-C44569?style=flat-square\&logoColor=white) ![CNN](https://img.shields.io/badge/CNN-f8a5c2?style=flat-square)

</div>

---

## 🧠 Overview

Day 2 of Week 9 focused on serving the serialized CNN melanoma classifier through a **FastAPI REST API**.

The goal was to load the trained `melanoma_cnn.keras` model, create a `POST /predict` endpoint for image uploads, apply the same preprocessing used during training, validate uploaded files, and return predictions as JSON.

The API was tested locally using FastAPI's interactive **Swagger UI**.

---

## 📁 Files

| File                 | Description                                                    |
| -------------------- | -------------------------------------------------------------- |
| `app/main.py`        | FastAPI application with model loading and `/predict` endpoint |
| `Hands_On_Lab.ipynb` | Hands-on implementation, testing, and documented results       |
| `requirements.txt`   | Dependencies required to run the API                           |

---

## 🛠️ Technologies Used

| Technology             | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| **FastAPI**            | Builds the REST API and prediction endpoint |
| **Uvicorn**            | Runs the FastAPI application locally        |
| **TensorFlow / Keras** | Loads and serves the trained CNN model      |
| **Pillow**             | Reads and processes uploaded images         |
| **NumPy**              | Converts and prepares image data            |
| **python-multipart**   | Handles multipart file uploads              |

---

## 🎯 API Implementation

The application loads the serialized CNN model once when the server starts.

```python
MODEL_PATH = Path(__file__).parent.parent.parent / "Day 1" / "models" / "melanoma_cnn.keras"

model = tf.keras.models.load_model(MODEL_PATH)

IMG_SIZE = (112, 112)
```

The main endpoint is:

```text
POST /predict
```

It accepts an uploaded image and returns the predicted melanoma class, confidence, and filename.

---

## 🔄 Prediction Pipeline

The API follows the same input preprocessing used during CNN training:

```text
Image Upload
     ↓
File Type Validation
     ↓
Convert to RGB
     ↓
Resize to 112 × 112
     ↓
Convert to NumPy Array
     ↓
Normalize /255.0
     ↓
Add Batch Dimension
     ↓
CNN Prediction
     ↓
Prediction Probability
     ↓
Class + Confidence
     ↓
JSON Response
```

### Preprocessing Details

| Step | Operation                             |
| ---- | ------------------------------------- |
| 1    | Read uploaded image                   |
| 2    | Convert image to RGB                  |
| 3    | Resize to `112 × 112`                 |
| 4    | Convert to NumPy array                |
| 5    | Normalize pixel values using `/255.0` |
| 6    | Add batch dimension                   |
| 7    | Pass the image to the CNN             |

> **Note:** Data augmentation is used during training to improve generalization, but it is not applied during inference.

---

## 📤 API Response

A successful prediction returns JSON in the following format:

```json
{
  "prediction": "Malignant",
  "confidence": 0.9231,
  "filename": "skin_lesion.jpg"
}
```

The `confidence` value represents the model's confidence in the **predicted class**. It is not the overall model accuracy.

---

## ▶️ Running the API

Navigate to the application directory:

```powershell
cd "Week9\Day 2\app"
```

Start the FastAPI server using Uvicorn:

```powershell
uvicorn main:app --reload
```

The API runs locally at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing Results

The `/predict` endpoint was tested with multiple valid images and an unsupported file type.

| Test | Input    | HTTP Status | Prediction | Confidence |
| ---- | -------- | ----------- | ---------- | ---------- |
| 1    | `3.jpg`  | `200`       | Benign     | `0.6105`   |
| 2    | `22.jpg` | `200`       | Benign     | `0.9112`   |
| 3    | `64.jpg` | `200`       | Malignant  | `0.9991`   |
| 4    | PDF file | `400`       | Rejected   | —          |

### Valid Image Tests

The API successfully processed all three valid image requests and returned JSON predictions.

Both classes were successfully produced during testing:

* **Benign**
* **Malignant**

### Invalid Input Test

An unsupported PDF file was uploaded:

```text
BinX Tech AI & ML Internship Week3.pdf
```

The API rejected the request with:

```text
HTTP 400 Bad Request
```

Response:

```json
{
  "detail": "Only JPEG and PNG images are accepted"
}
```

This confirms that unsupported file types are rejected before image prediction.

---

## 📚 Key Concepts

| Concept          | What Was Applied                    |
| ---------------- | ----------------------------------- |
| REST API         | Exposed the CNN model through HTTP  |
| FastAPI          | Built the model-serving application |
| `UploadFile`     | Received uploaded image files       |
| Input Validation | Rejected unsupported file types     |
| Model Serving    | Loaded the serialized Keras model   |
| Preprocessing    | Matched training input format       |
| JSON Response    | Returned prediction results         |
| Swagger UI       | Tested the API interactively        |
| Uvicorn          | Served the FastAPI application      |

---

## ✅ Day 2 Checklist

* [x] Build FastAPI application
* [x] Load serialized CNN model
* [x] Implement `POST /predict`
* [x] Handle image uploads
* [x] Validate uploaded file types
* [x] Apply inference preprocessing
* [x] Return prediction as JSON
* [x] Run API with Uvicorn
* [x] Test through Swagger UI
* [x] Test multiple valid images
* [x] Test invalid input
* [x] Document API results

---

## 🎓 Outcome

By the end of Day 2, the trained CNN melanoma classifier was successfully connected to a local REST API.

The model can now receive an image through `POST /predict`, apply the required preprocessing, perform inference, and return the predicted class and confidence as a JSON response.

---

## ➡️ Next — Day 3

Build the next deployment layer by creating a user-facing interface for the trained model and connecting it to the FastAPI prediction service.
