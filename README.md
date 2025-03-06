# **🍓 Strawberry Disease Detection**  
A deep learning-powered **web application** to detect **strawberry leaf diseases** using **image classification**.  

![Sample Detection](static/sample.png)  

---

## **📌 Project Description**  
Strawberries are prone to **various diseases** that affect their **growth and quality**. This project uses a **Convolutional Neural Network (CNN)** to classify strawberry leaves into:  
✅ **Healthy** 🌿  
✅ **Leaf Spot Disease** 🍂  
✅ **Other Diseases** 🦠  

Built with:  
- **TensorFlow/Keras** (Deep Learning)  
- **Flask** (Web Deployment)  
- **HTML + CSS + JavaScript** (UI & Animations)  

---

## **📂 Dataset**  
🔗 **[Kaggle Dataset](https://www.kaggle.com/datasets/sandeepmopidevi/strawberry-disease) (Private Repo)**  

- **Healthy Leaves** (91 images) ✅  
- **Leaf Spot Disease** (100 images) 🍂  
- **Other Diseases** (42 images) 🦠  

---

## **🎯 Features**  
✅ **AI-powered Disease Detection**  
✅ **Trained CNN Model (`strawberry_model.h5`)**  
✅ **Flask Web App for Easy Use**  
✅ **Stylish UI with Transparent Background**  
✅ **Supports Image Upload & Real-time Predictions**  

---

## **🛠️ Installation & Setup**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Sandeepmopidevi/Strawberry-Disease-Detection.git
cd Strawberry-Disease-Detection
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**
```bash
python app.py
```
📌 Open **`http://127.0.0.1:5000`** in your browser.  

---

## **📜 Usage**
1️⃣ **Upload a Strawberry Leaf Image**  
2️⃣ **Click "Upload & Detect"**  
3️⃣ **View the Prediction Result** 🎯  

---

## **📁 Project Structure**
```
/Strawberry-Disease-Detection
│── /static
│   ├── background.png  # Transparent Background
│   ├── sample.png      # Demo Image (For README)
│   ├── uploads         # Uploaded Images
│── /templates
│   ├── index.html      # Upload Page
│   ├── result.html     # Prediction Result Page
│── /models
│   ├── strawberry_model.h5  # Trained CNN Model
│── app.py              # Flask API
│── train_model.ipynb   # Model Training Notebook
│── requirements.txt    # Python Dependencies
│── README.md           # Project Documentation
```

---

## **🚀 Model Training (Optional)**
To train the model in **Kaggle**, use `train_model.ipynb`.  
It will generate a **`strawberry_model.h5`** file for Flask.  

---

## **🔗 Demo**  
🚀 **Live Demo:** _[To be hosted soon]_  

---

## **🤝 Credits**  
👨‍💻 Developed by **Sandeep Mopidevi**  
🌱 **Data Source:** Kaggle by Sandeep Mopidevi  

📩 Feel free to **fork**, **contribute**, or **open issues**!  
