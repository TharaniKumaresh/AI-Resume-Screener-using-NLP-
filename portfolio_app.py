import streamlit as st

st.set_page_config(page_title="Tharani's Portfolio", page_icon="🌟", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=150)
    st.title("Tharani Kumaresh")
    st.write("🎓 B.E. Electronics & Communication Engineering")
    st.write("📍 India")
    st.markdown("[📄 Download Resume](https://example.com/resume.pdf)", unsafe_allow_html=True)
    st.markdown("[💌 Contact Me](mailto:tharanikumaresh@gmail.com)", unsafe_allow_html=True)

# --- About Me ---
st.title("👋 Hey, I'm Tharani!")
st.write(
    """
    I'm a passionate engineering student focused on **Data Science**, **AI**, and **NLP** projects.  
    I love building intelligent tools and solving real-world problems using technology.
    """)

# --- Projects ---
st.subheader("🧠 My Projects")

st.markdown("### 📄 Resume Screener using NLP")
st.write("An intelligent tool that reads `.docx` resumes and matches them with job descriptions using NLP and cosine similarity.")
st.markdown("[▶️ Launch Streamlit App](https://example.com/resume-screener)", unsafe_allow_html=True)
st.markdown("[💻 View Code on GitHub](https://github.com/tharani/resume-screener)", unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🧹 Data Cleaner for CSVs")
st.write("A simple web tool that allows you to upload CSV files and clean missing values, duplicates, and format them for ML.")
st.markdown("[▶️ Launch Streamlit App](https://example.com/csv-cleaner)", unsafe_allow_html=True)
st.markdown("[💻 View Code on GitHub](https://github.com/tharani/csv-cleaner)", unsafe_allow_html=True)

# --- Contact ---
st.subheader("📬 Get in Touch")
with st.form("contact_form"):
    name = st.text_input("Tharani K")
    email = st.text_input("tharanikumaresh@gmail.com")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks! I'll get back to you soon. 💌")