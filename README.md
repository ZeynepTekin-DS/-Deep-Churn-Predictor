🛡️ ChurnGuard AI: AI-Powered Customer Loyalty and Churn Analysis System

APPLICATION LINK (Hugging Face / GitHub): 

https://huggingface.co/spaces/zeynepptkn/churn-predictor ----https://github.com/ZeynepTekin-DS/-Deep-Churn-Predictor

PROJECT SUMMARY: 📖 This study was developed on a massive telecommunications dataset of 600,000 rows to detect the probability of customers leaving the service (churn) before it happens. By focusing not only on demographic data but also on behavioral risk scores and social connections, the project constructs a decision-support mechanism that offers a proactive retention strategy for businesses.
METHODS USED:

Ensemble Learning: 🧠 Within the scope of the project, 8 different algorithms (XGBoost, LightGBM, CatBoost, RandomForest, etc.) were competed against each other. The XGBoost algorithm, which best resolved complex data structures, was selected as the champion model with a 0.9144 ROC-AUC score.

Handling Imbalance: ⚖️ Since churned customers are in the minority, the dataset was balanced during the training phase to prevent model bias, maximizing the model's ability to catch "customers at risk of leaving" (Recall: 0.82).
DATA PREPROCESSING:

Feature Engineering: 🖇️ New variables such as Risk_Score (critical risk score), AvgMonthly (average spending), and IsNewCustomer (new customer flag) were derived from raw data, increasing the model's predictive power by 70%.

Encoding & Scaling: 🧹 Categorical data (Gender, PaymentMethod, etc.) were converted into numerical formats, while numerical data were normalized to ensure faster and more stable learning for the model.

Feature Selection (The 12 Golden Columns): 🛠️ Unnecessary data were filtered out to create an optimized input set consisting of: gender, SeniorCitizen, Partner, Dependents, tenure, PaymentMethod, MonthlyCharges, TotalCharges, AvgMonthly, Risk_Score, IsNewCustomer, and TotalServices.
KEY RESULTS:

Model Success: 🏆 The champion XGBoost model can distinguish between "churn" and "loyal" customers with a 0.9144 ROC-AUC success rate, representing a 91.4% discriminatory accuracy.

Critical Insights: 📊 Analysis statistically proved that being an IsNewCustomer (New Customer) is the strongest churn trigger, while social ties such as Partner and Dependents (Spouse and Children) act as "social anchors" that bind the customer to the brand.
NOTES:

Interactive Interface: 🎨 Thanks to the "ChurnGuard AI Dashboard" developed using the Streamlit library, managers can perform real-time risk analysis by entering customer information on the main screen and receiving automatic alerts for customers exceeding a 50% threshold.

Production & Deployment: ☁️ The trained champion model (customer_model.pkl) and the app.py file have been deployed on Hugging Face Spaces, transforming data science into an operational business tool.

Prepared by: Zeynep Tekin

Date: April 8, 2026