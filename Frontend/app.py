import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬")

st.title("💬 Sentiment Analysis App")
st.write("Enter a product review below to analyze its sentiment.")

review_text = st.text_area("Review Text")

if st.button("Analyze Sentiment"):

    if review_text.strip() == "":
        st.warning("Please enter a review.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": review_text}
            )

            if response.status_code == 200:
                result = response.json()
                sentiment = result["sentiment"]

                if sentiment == "Positive":
                    st.success(f"✅ Sentiment: {sentiment}")
                else:
                    st.error(f"❌ Sentiment: {sentiment}")
            else:
                st.error("API error. Check if FastAPI is running.")

        except:
            st.error("Could not connect to API. Make sure FastAPI server is running.")