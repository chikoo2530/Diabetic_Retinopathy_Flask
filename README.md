# Diabetic Retinopathy Severity Grading from Fundus Photographs

## 📌 Overview

Diabetic Retinopathy (DR) is a diabetes-related eye disease that can lead to severe vision impairment and blindness if not detected early. This project presents an AI-powered automated diabetic retinopathy severity grading system using retinal fundus photographs and deep learning techniques.

The proposed system utilizes a **hybrid deep learning model combining EfficientNetB0 and InceptionV3 architectures** to improve feature extraction and classification performance. By leveraging the strengths of both models, the system achieves more accurate and robust diabetic retinopathy severity prediction.

The application is designed to assist ophthalmologists and healthcare professionals in early screening, diagnosis support, and large-scale diabetic retinopathy detection.

---

# 🚀 Key Features

* Automated diabetic retinopathy severity grading
* Fundus image analysis using deep learning
* Hybrid CNN model for improved accuracy
* User-friendly web application
* Fast and reliable prediction system
* Early-stage disease detection support
* Reduced manual screening effort

---

# 🩺 Severity Classification

The system classifies retinal fundus images into five diabetic retinopathy severity levels:

| Grade | Severity Level                |
| ----- | ----------------------------- |
| 0     | No Diabetic Retinopathy       |
| 1     | Mild Non-Proliferative DR     |
| 2     | Moderate Non-Proliferative DR |
| 3     | Severe Non-Proliferative DR   |
| 4     | Proliferative DR              |

---

# 🧠 Hybrid Deep Learning Model

This project uses a **hybrid deep learning architecture** that combines:

* **EfficientNetB0**
* **InceptionV3**

The hybrid model integrates the feature extraction capabilities of both pretrained convolutional neural networks to improve classification accuracy and generalization performance.

## 🔹 EfficientNetB0

EfficientNetB0 is a highly optimized convolutional neural network architecture that balances network depth, width, and resolution efficiently. It provides strong performance with fewer parameters and lower computational cost.

### Advantages:

* High accuracy with lightweight architecture
* Efficient feature extraction
* Faster training and inference
* Better scalability

## 🔹 InceptionV3

InceptionV3 is a deep convolutional neural network designed to capture multi-scale visual patterns using inception modules. It improves classification performance by extracting detailed spatial features from retinal images.

### Advantages:

* Strong feature representation
* Multi-scale image analysis
* Improved detection of retinal abnormalities
* Reduced overfitting through factorized convolutions

## 🔹 Hybrid Model Benefits

By combining EfficientNetB0 and InceptionV3, the model benefits from:

* Enhanced feature learning
* Better retinal lesion detection
* Improved classification accuracy
* Robust performance on medical imaging datasets
* Better generalization on unseen data

---

# ⚙️ Technologies and Frameworks Used

## Programming Language

* Python

## Deep Learning Frameworks

* TensorFlow
* Keras

## Image Processing Libraries

* OpenCV
* NumPy
* Pillow

## Data Visualization

* Matplotlib
* Seaborn

## Web Framework

* Flask / Streamlit

## Model Architecture

* Hybrid CNN Model
* EfficientNetB0
* InceptionV3
* Transfer Learning

---

# 📂 Dataset

The model is trained using publicly available retinal fundus image datasets such as:

* APTOS 2019 Blindness Detection Dataset
* EyePACS Dataset
* Kaggle Diabetic Retinopathy Dataset

These datasets contain labeled retinal images corresponding to different diabetic retinopathy severity levels.

---

# 🔄 System Workflow

1. Fundus image upload
2. Image preprocessing
3. Feature extraction using hybrid CNN
4. Severity classification
5. Prediction result generation
6. Output visualization

---

# 🖼️ Image Preprocessing Techniques

To improve model performance, the following preprocessing techniques are applied:

* Image resizing
* Normalization
* Noise reduction
* Contrast enhancement
* Data augmentation

---

# 🏗️ Model Training Details

The hybrid model was trained using transfer learning and fine-tuning techniques.

## Training Components

* Pretrained EfficientNetB0 and InceptionV3 models
* Feature fusion layer
* Fully connected dense layers
* Softmax classification layer

## Training Parameters

* Optimizer: Adam
* Loss Function: Categorical Crossentropy
* Epochs: 50+
* Batch Size: 32

---

# 📊 Performance Metrics

The model performance is evaluated using:

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 92%   |
| Precision | 90%   |
| Recall    | 91%   |
| F1-Score  | 90%   |

*Replace the above values with actual project results.*

---

# 💡 Benefits of the System

## 👨‍⚕️ For Doctors

* Supports faster retinal screening
* Assists in diagnosis decision-making
* Reduces manual workload

## 🏥 For Hospitals

* Enables large-scale screening programs
* Improves operational efficiency
* Reduces healthcare costs

## 👥 For Patients

* Early detection of diabetic retinopathy
* Faster diagnosis and treatment
* Reduced risk of blindness

---

# 🌍 Real-World Applications

* Ophthalmology clinics
* Hospitals and diagnostic centers
* Telemedicine systems
* Rural healthcare screening
* AI-assisted medical imaging solutions

---

# 🔐 Future Enhancements

* Explainable AI using Grad-CAM
* Mobile application deployment
* Cloud-based prediction system
* Multi-eye disease classification
* Real-time screening support

---

# 🧪 Installation

```bash
git clone https://github.com/your-username/diabetic-retinopathy-grading.git
cd diabetic-retinopathy-grading
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

---

# 📁 Project Structure

```bash
├── dataset/
├── models/
├── notebooks/
├── static/
├── templates/
├── app.py
├── train.py
├── predict.py
├── requirements.txt
└── README.md
```

---

# 📸 Output

The system provides:

* Uploaded retinal fundus image
* Predicted diabetic retinopathy severity level
* Confidence score
* Visual analysis results

---

# 🎯 Conclusion

This project demonstrates the application of hybrid deep learning techniques for automated diabetic retinopathy severity grading from retinal fundus photographs. The combination of EfficientNetB0 and InceptionV3 enhances feature extraction and classification performance, enabling accurate and efficient diabetic retinopathy detection. The proposed system can support healthcare professionals in early diagnosis and large-scale screening, ultimately helping to reduce preventable blindness caused by diabetic retinopathy.
