import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
@st.cache_data
def load_data():
    # Load the Upwork dataset
    df = pd.read_csv("data/Final_Upwork_Dataset.csv")
    
    # Map Upwork categories to Kenyan gig jobs
    kenyan_job_map = {
        'Web Development': 'Digital Skills',
        'Mobile Development': 'Digital Skills',
        'Design & Creative': 'Creative',
        'Writing': 'Content Creation',
        'Admin Support': 'Office Jobs',
        'Customer Service': 'Office Jobs',
        'Marketing': 'Sales & Marketing',
        'Accounting': 'Office Jobs',
        'Engineering & Architecture': 'Construction'
    }
    
    df['kenyan_category'] = df['Category_1'].map(kenyan_job_map).fillna('Other')
    
    # Add Kenyan-specific columns
    locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret']
    df['location'] = np.random.choice(locations, size=len(df))
    
    # Add synthetic hourly rates (in KSh)
    df['hourly_rate'] = np.random.randint(200, 1500, size=len(df))
    
    return df

df = load_data()

# Text similarity function
@st.cache_data
def get_similar_jobs(query, df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['Description'].fillna(''))
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    return similarities

# Streamlit App
st.set_page_config(page_title="Kenya Gig Connect", layout="wide")

st.title("🇰🇪 Kenya Gig Connect")
st.subheader("Matching Kenyan workers with optimal job opportunities")

# Sidebar filters
st.sidebar.header("Job Filters")
selected_category = st.sidebar.selectbox(
    "Job Category",
    options=df['kenyan_category'].unique(),
    index=0
)

selected_location = st.sidebar.multiselect(
    "Location",
    options=df['location'].unique(),
    default=['Nairobi']
)

rate_range = st.sidebar.slider(
    "Hourly Rate Range (KSh)",
    min_value=200,
    max_value=1500,
    value=(400, 800)
)

# Main content
tab1, tab2 = st.tabs(["Job Board", "Worker Matching"])

with tab1:
    st.header("Available Jobs")
    
    # Filter jobs
    filtered_jobs = df[
        (df['kenyan_category'] == selected_category) &
        (df['location'].isin(selected_location)) &
        (df['hourly_rate'] >= rate_range[0]) &
        (df['hourly_rate'] <= rate_range[1])
    ]
    
    st.dataframe(
        filtered_jobs[['Job Title', 'kenyan_category', 'location', 'hourly_rate', 'Description']].head(20),
        column_config={
            "Job Title": "Job Title",
            "kenyan_category": "Category",
            "location": "Location",
            "hourly_rate": "Rate (KSh/hr)",
            "Description": "Job Details"
        },
        hide_index=True,
        use_container_width=True
    )

with tab2:
    st.header("Find Jobs Matching Your Skills")
    
    user_skills = st.text_input("Describe your skills (e.g., 'experienced plumber with 5 years experience')")
    
    if user_skills:
        similarities = get_similar_jobs(user_skills, df)
        df['similarity'] = similarities
        recommended_jobs = df.sort_values('similarity', ascending=False).head(10)
        
        st.subheader("Recommended Jobs For You")
        for idx, row in recommended_jobs.iterrows():
            with st.expander(f"{row['Job Title']} - {row['hourly_rate']} KSh/hr"):
                st.write(f"**Location:** {row['location']}")
                st.write(f"**Category:** {row['kenyan_category']}")
                st.write(f"**Similarity Score:** {row['similarity']:.2f}")
                st.write(f"**Description:** {row['Description']}")
                st.button("Apply for this job", key=f"apply_{idx}")

# Kenyan gig economy tips
st.sidebar.markdown("---")
st.sidebar.header("Kenyan Gig Tips")
st.sidebar.info("""
- **Mamafua**: Charge 300-500 KSh per bundle
- **Plumbers**: 500-1000 KSh/hour
- **Cleaners**: 200-400 KSh/hour
- **Include transport costs** in your quotes
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Kenya Gig Connect | Data from Upwork (adapted for Kenya)")