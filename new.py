import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import time

# Initialize dark mode in session state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Button to toggle dark mode
if st.button("Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode

# Apply dark mode styles
if not st.session_state.dark_mode:
    st.markdown("""
    <style>
        * {
            background-color: white;
            color: black;
        }
        .stButton button {
            color: black;
        }
    </style>
    """, unsafe_allow_html=True)

# Add content to your page to observe the change
st.title("Dark Mode Toggle Example")
st.write("Click the button to switch between dark and light mode.")

# Custom CSS for Gojo Satoru vibes
st.markdown("""
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
        }
        h1, h2, h3 {
            color: #00d4ff;
            text-align: center;
            font-size: 3rem;
        }
        #progress-bar {
            background-color: #1b1f3a;
        }
    </style>
""", unsafe_allow_html=True)

# Gojo intro
st.markdown('<h1>👁️ the gojo satoru experience 🌌</h1>', unsafe_allow_html=True)

# Gojo progress animation
progress_bar = st.progress(0)
message_placeholder = st.empty()
message_placeholder.write("starting the infinite void...")
time.sleep(1)
progress_bar.progress(50)
message_placeholder.write("tapping into limitless...")
time.sleep(1)
progress_bar.progress(100)
message_placeholder.write("you've mastered gojo's power! 🌀")

# Tabs for interactions
tab1, tab2, tab3 = st.tabs(["🌀 infinity hub", "⚙️ power settings", "📊 analysis zone"])

with tab1:
    st.header("🌀 enter the void")
    st.write("embrace infinity and unlock limitless possibilities")
    if st.button("💥 unleash power"):
        st.balloons()
        st.success("you've entered gojo's domain expansion!")

with tab2:
    st.header("⚙️ customize your abilities")
    st.slider("🎚️ control your energy", 0, 100, 50)
    st.selectbox("choose your technique", ["blue", "red", "hollow purple"])

with tab3:
    st.header("📊 analyze your potential")
    st.text_area("describe your experience in the void")

# Data table
data = pd.DataFrame({
    "technique": ["blue", "red", "hollow purple"],
    "power": [9001, 10000, 15000],
    "effect": ["attraction", "repulsion", "obliteration"]
})
st.table(data)

# CSV download
csv_data = data.to_csv(index=False)
st.download_button(
    label="download gojo technique data",
    data=csv_data,
    file_name="gojo_techniques.csv",
    mime="text/csv"
)

# Dynamic plot
x = np.linspace(0, 10, 100)
y = np.sin(x) * 2

fig, ax = plt.subplots()
ax.plot(x, y, color='#00d4ff', linestyle='dotted', marker='o')
plt.grid()
plt.title("energy wave simulation 🌌", color='white' if st.session_state.dark_mode else 'black')
st.write(fig)

# Sidebar feature for iris flower app
st.sidebar.header("🌺 iris analysis (powered by gojo)")

def user_input_features():
    sepal_length = st.sidebar.slider('sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('petal width', 0.1, 2.5, 0.2)
    
    data = {
        'sepal length': sepal_length,
        'sepal width': sepal_width,
        'petal length': petal_length,
        'petal width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("🌺 input parameters")
st.write(df)

iris = load_iris()
X = iris.data
y = iris.target

rf = RandomForestClassifier()
rf.fit(X, y)

pred = rf.predict(df)
pred_prob = rf.predict_proba(df)

st.subheader("class labels and their corresponding index numbers")
st.write(iris.target_names)

# Divider
st.divider()
st.write("below this divider is an iris predictor by scikit dataset")
 
st.subheader("prediction")
st.write(iris.target_names[pred])

st.subheader('prediction probability')
st.write(pred_prob)

# 🎈 Balloons animation
time.sleep(1)
st.balloons()

# Anime image upload
uploaded_file = st.file_uploader("upload an image (of gojo maybe 😉)", type=["png", "jpg"])
if uploaded_file:
    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image, caption="your upload 🌌")

# Watch party scheduling
st.time_input("⏰ watch jujutsu kaisen at:")
st.date_input("📅 set your next binge-watch date")

# Markdown lists  
st.markdown("""
## **gojo's commandments**
- never blink during a fight 🌀  
- embrace infinity 🌌  
- always protect the weak 💎
""")

# Divider
st.divider()

st.markdown("""
### 👁️ **the void awaits... enter whenever you dare!** 🌀  
""")
