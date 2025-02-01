import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import time

# page config
st.set_page_config(page_title="gojo's domain expansion", page_icon="🌀")

# custom css for aesthetics
st.markdown("""
    <style>
        body {
            font-family: 'helvetica', sans-serif;
            background-color: #0e1117;
            color: #f0f0f0;
        }
        h1, h2, h3 {
            color: #00d4ff;
            text-align: center;
            font-size: 3rem;
            text-transform: lowercase;
        }
        .st-bq {
            color: #00d4ff;
        }
        .st-cb {
            background-color: #1b1f3a;
        }
        .st-markdown {
            text-transform: lowercase;
        }
    </style>
""", unsafe_allow_html=True)

# title
st.markdown('<h1>👁️ the gojo satoru experience 🌌</h1>', unsafe_allow_html=True)

# progress bar and messages
progress_bar = st.progress(0)
message_placeholder = st.empty()
message_placeholder.write("starting the infinite void...")
time.sleep(1)
progress_bar.progress(50)
message_placeholder.write("tapping into limitless...")
time.sleep(1)
progress_bar.progress(100)
message_placeholder.write("you've mastered gojo's power! 🌀")

# tabs
tab1, tab2, tab3 = st.tabs(["🌀 infinity hub", "⚙️ power settings", "📊 analysis zone"])

with tab1:
    st.header("🌀 enter the void")
    st.write("embrace infinity and unlock limitless possibilities")
    if st.button("💥 unleash power"):
        st.balloons()
        st.success("you've entered gojo's domain expansion!")

with tab2:
    st.header("⚙️ customize your abilities")
    energy_level = st.slider("🎚️ control your energy", 0, 100, 50)
    technique = st.selectbox("choose your technique", ["blue", "red", "hollow purple"])

with tab3:
    st.header("📊 analyze your potential")
    experience = st.text_area("describe your experience in the void")

# data table
data = pd.DataFrame({
    "technique": ["blue", "red", "hollow purple"],
    "power": [9001, 10000, 15000],
    "effect": ["attraction", "repulsion", "obliteration"]
})
st.table(data)

# download button
csv_data = data.to_csv(index=False)
st.download_button(
    label="download gojo technique data",
    data=csv_data,
    file_name="gojo_techniques.csv",
    mime="text/csv"
)

# plot
x = np.linspace(0, 10, 100)
y = np.sin(x) * 2

fig, ax = plt.subplots()
ax.plot(x, y, color='#00d4ff', linestyle='dotted', marker='o')
plt.grid()
plt.title("energy wave simulation 🌌", color='white')
st.pyplot(fig)

# sidebar
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

# iris prediction
iris = load_iris()
X = iris.data
Y = iris.target

rf = RandomForestClassifier()
rf.fit(X, Y)

pred = rf.predict(df)
pred_prob = rf.predict_proba(df)

st.subheader("class labels and their corresponding index numbers")
st.write(iris.target_names)

st.divider()
st.write("below this divider is an iris predictor by scikit dataset")

st.subheader("prediction")
st.write(iris.target_names[pred])

st.subheader('prediction probability')
st.write(pred_prob)

time.sleep(1)
st.balloons()
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

st.write("wanna see ur own pic like this then upload below")
st.image("https://github.com/HelloKeerthana/streamlit_gojostyle/blob/main/random.jpeg", caption="Your upload 🌌 if u upload")

# File uploader
uploaded_file = st.file_uploader("Upload an image (of Gojo maybe 😉)", type=["png", "jpg"])

# Store the uploaded image in session state if it's not already stored
if uploaded_file and st.session_state.uploaded_image is None:
    st.session_state.uploaded_image = Image.open(uploaded_file)

# Display the uploaded image (only if it exists in session state)
if st.session_state.uploaded_image:
    st.image(st.session_state.uploaded_image, caption="Your upload 🌌")


# time and date inputs
st.time_input("⏰ watch jujutsu kaisen at:")
st.date_input("📅 set your next binge-watch date")

# markdown content
st.markdown("""
## **gojo's commandments**
- never blink during a fight 🌀  
- embrace infinity 🌌  
- always protect the weak 💎
""")

st.divider()

st.markdown("""
### 👁️ **the void awaits... enter whenever you dare!** 🌀  
""")
