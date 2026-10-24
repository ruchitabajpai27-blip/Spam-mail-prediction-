import streamlit as st
import pickle

with open("spam_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    feature_extraction = pickle.load(file)

st.title("📧 Spam Mail Prediction")
st.write("Enter a message to check whether it is Spam or Ham.")

input_mail = st.text_area("Enter your message:")

if st.button("Predict"):
    if input_mail.strip():
        input_features = feature_extraction.transform([input_mail])
        prediction = model.predict(input_features)[0]

        if prediction == 0:
            st.error("🚫 This message is Spam!")
        else:
            st.success("✅ This message is Ham (Not Spam).")
    else:
        st.warning("Please enter a message.")
