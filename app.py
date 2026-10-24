import streamlit as st
import pickle

# Load the trained model

with open("spam_model.pkl", "rb") as file:
model = pickle.load(file)

# Load the TF-IDF vectorizer

with open("vectorizer.pkl", "rb") as file:
feature_extraction = pickle.load(file)

# Website title

st.title("📧 Spam Mail Prediction")
st.write("Enter an email message to check whether it is Spam or Ham.")

# Input box

input_mail = st.text_area("Enter your email message:")

# Prediction button

if st.button("Predict"):
if input_mail.strip():
# Convert text into numerical features
input_features = feature_extraction.transform([input_mail])

```
    # Make prediction
    prediction = model.predict(input_features)[0]

    # Display result
    if prediction == 0:
        st.error("🚫 This email is Spam Mail")
    else:
        st.success("✅ This email is Ham Mail (Not Spam)")
else:
    st.warning("Please enter an email message.")
```
