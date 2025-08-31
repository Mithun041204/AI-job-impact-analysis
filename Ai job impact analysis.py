#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os
import pandas as pd

os.makedirs("data", exist_ok=True)

data = {
    "job_title": [
        "AI Engineer", "Data Scientist", "Software Developer",
        "Machine Learning Engineer", "Business Analyst",
        "Cloud Architect", "AI Researcher", "HR Specialist"
    ],
    "company": [
        "Google", "Amazon", "Infosys", "Microsoft",
        "Deloitte", "TCS", "OpenAI", "Wipro"
    ],
    "location": [
        "USA", "India", "India", "UK",
        "India", "USA", "Canada", "India"
    ],
    "description": [
        "Build AI models and solutions",
        "Analyze data and implement ML models",
        "Develop backend systems",
        "Design ML pipelines",
        "Analyze business processes",
        "Manage cloud infra with AI tools",
        "Conduct AI research in NLP",
        "Recruitment and employee management"
    ]
}

df = pd.DataFrame(data)

df.to_csv("data/ai_jobs_sample.csv", index=False)
print("Sample job data saved to data/ai_jobs_sample.csv")


# In[8]:


import pandas as pd

df = pd.read_csv("data/ai_jobs_sample.csv")

ai_keywords = ["AI", "Artificial Intelligence", "Machine Learning", "Deep Learning", "NLP"]

def classify_job(title, description):
    text = (title + " " + description).lower()
    return "AI-related" if any(keyword.lower() in text for keyword in ai_keywords) else "Non-AI"

df["category"] = df.apply(lambda x: classify_job(x["job_title"], x["description"]), axis=1)

df.to_csv("data/ai_jobs_classified.csv", index=False)
print("Classified jobs saved to data/ai_jobs_classified.csv")


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/ai_jobs_classified.csv")
print(df.head())

job_counts = df["category"].value_counts()

plt.figure(figsize=(6,4))
job_counts.plot(kind="bar", color=["skyblue", "salmon"])
plt.title("AI vs Non-AI Jobs Distribution")
plt.ylabel("Number of Jobs")
plt.show()


# In[11]:


category_counts = df["category"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
        startangle=90, colors=["#4CAF50", "#FF9800"])
plt.title("AI vs Non-AI Jobs")
plt.show()


# In[13]:


import seaborn as sns

location_counts = df[df["category"]=="AI-related"]["location"].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=location_counts.index, y=location_counts.values, palette="viridis")
plt.title("AI Jobs by Location")
plt.xlabel("Location")
plt.ylabel("Number of AI Jobs")
plt.show()


# In[14]:


company_counts = df[df["category"]=="AI-related"]["company"].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=company_counts.index, y=company_counts.values, palette="coolwarm")
plt.title("Top Companies Hiring AI Roles")
plt.xlabel("Company")
plt.ylabel("Number of AI Jobs")
plt.show()


# In[ ]:





# In[ ]:




