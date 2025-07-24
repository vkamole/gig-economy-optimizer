# **Kenya Gig Economy Optimizer**  
### **Connecting Informal Workers with Opportunities Using AI**  

![Streamlit App Demo](https://img.shields.io/badge/Platform-Streamlit-FF4B4B?logo=streamlit)  
![SDG 8](https://img.shields.io/badge/SDG-8_Decent_Work-0A97D9?logo=united-nations)  

## **📌 Overview**  
This project leverages **AI-driven job matching** to optimize Kenya’s informal gig economy (e.g., *mamafua*, plumbers, cleaners, drivers*) by:  
- **Matching workers** with nearby jobs using **TF-IDF and cosine similarity**.  
- **Predicting fair wages** based on skills, location, and demand.  
- **Increasing income stability** through data-driven job allocation.  

**Alignment with SDG 8 (Decent Work & Economic Growth)**:  
✅ Reduces unemployment in informal sectors  
✅ Promotes fair wages and financial inclusion  
✅ Improves access to consistent work opportunities  

Here is the deployed application link: https://gig-worker.streamlit.app/

Here is the pitch deck presentation for the application: https://gamma.app/docs/KaziBora-AI-Powered-Gig-Economy-Optimization-for-Kenya-4p6e2xku0jeyvqt?mode=doc


---

## **✨ Key Features**  
| Feature | Impact |  
|---------|--------|  
| **Skills-Based Job Matching** | Uses NLP to match worker profiles with job descriptions |  
| **Location Optimization** | Prioritizes jobs within the worker’s locality to reduce transport costs |  
| **Income Analytics Dashboard** | Tracks earnings and suggests high-demand skills for upskilling |  
| **Real-Time Pricing Suggestions** | Recommends competitive rates based on market data |  

---

## **🛠️ Setup & Installation**  
### **1. Prerequisites**  
- Python 3.8+  
- Git Bash (for Windows users)  

### **2. Run Locally**  
```bash  
# Clone the repo  
git clone https://github.com/yourusername/kenya-gig-optimizer.git  

# Navigate to project  
cd kenya-gig-optimizer  

# Create and activate virtual environment (Git Bash)  
python -m venv myenv  
source myenv/Scripts/activate  

# Install dependencies  
pip install -r requirements.txt  

# Run the Streamlit app  
streamlit run app/main.py  
```  

---

## **📂 Project Structure**  
```  
kenya-gig-optimizer/  
├── app/  
│   ├── main.py               # Streamlit app logic  
│   ├── assets/               # Images/CSS  
├── data/  
│   ├── Final_Upwork_Dataset.csv  # Sample job data  
├── models/  
│   ├── job_matcher.pkl       # Trained TF-IDF model  
├── requirements.txt          # Dependencies  
└── README.md  
```  

---

## **📈 Impact Metrics (SDG 8 Alignment)**  
| Metric | Target |  
|--------|--------|  
| **Jobs Matched/Month** | 1,000+ informal workers |  
| **Income Increase** | 20-30% via optimized pricing |  
| **Reduced Job Search Time** | 50% faster matching |  

**Why This Works for Kenya**:  
- 83% of Kenya’s workforce is in the informal sector (*World Bank, 2023*)  
- AI reduces friction in connecting workers with clients  

---

## **🌍 Future Roadmap**  
- **M-Pesa Integration**: Direct in-app payments for gigs  
- **SMS Notifications**: For workers without smartphones  
- **Upskilling Recommendations**: Partner with online courses (e.g., Coursera)  

---

## **📜 License**  
MIT License - Open source for non-profit use.  

**Developed with ❤️ for Kenya’s Gig Workers**  

--- 

### **🚀 How to Contribute**  
1. Fork the repo  
2. Add features (e.g., M-Pesa API)  
3. Submit a PR!  

**Let’s build economic resilience together!**  

--- 

🔗 **Live Demo**: [Coming Soon] | **Kaggle Dataset**: [Upwork Jobs Data](https://www.kaggle.com/datasets/ahmedmyalo/upwork-freelance-jobs-60k)  

--- 

**#DigitalHustle #SDG8 #KenyaGigEconomy**  

---
