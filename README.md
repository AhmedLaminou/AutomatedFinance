# 💰 Pro Finance Dashboard

![Finance Dashboard Banner](https://via.placeholder.com/1200x400.png?text=Pro+Finance+Dashboard)

> A sleek, intelligent, and interactive **financial dashboard** built with **Streamlit**, designed to help you manage, visualize, and forecast your personal or business finances. Track expenses, categorize transactions automatically, set budgets, and gain insights—all in one place!

---

## 🌟 Features

- **CSV Transaction Import:** Upload single or multiple CSV files containing your transactions.  
- **Automatic Categorization:** Fuzzy matching & keyword-based classification for quick organization.  
- **Budget Tracking:** Set budgets per category and get real-time alerts when exceeded.  
- **Data Editing:** Interactive data editor to correct or reassign categories.  
- **Advanced Analytics & Visualization:**  
  - Category pie charts  
  - Monthly expense trends  
  - Top vendors / payees  
  - Predictive suggestions for uncategorized transactions  
  - Expense forecasts for the next month  
- **Dark/Light Theme Toggle:** Customize your dashboard appearance.  
- **Download Updated CSV:** Export your categorized and cleaned transactions.  

---

## 📦 Project Structure

AutomatedFinance/
├─ main.py # Streamlit main app
├─ categorizer.py # Transaction categorization + forecasting
├─ data_loader.py # CSV loading & cleaning
├─ visuals.py # Plotly charts & data visualizations
├─ budget.py # Budget initialization & checks
├─ analytics.py # Advanced analytics functions
├─ utils.py # Session management & category handling
├─ categories.json # Persistent category storage
├─ requirements.txt # Python dependencies
└─ assets/ # Images, logos, and icons


---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AhmedLaminou/Pro-Finance-Dashboard.git
cd Pro-Finance-Dashboard

2️⃣ Install dependencies
pip install -r requirements.txt
Dependencies include:

streamlit

pandas

numpy

plotly

scikit-learn

fuzzywuzzy

statsmodels

3️⃣ Run the dashboard
streamlit run main.py
pen the URL provided in the terminal (usually http://localhost:8501) to access your dashboard.

🛠 Usage

Upload your CSV files (transactions exported from your bank).

Add new categories in the sidebar if needed.

Set budgets for each category.

Edit transactions directly in the interactive data editor.

Analyze your spending: charts, monthly trends, top vendors, and forecasts.

Download your categorized CSV for backup or further use.

🔮 Predictive Categorization

Uses fuzzy matching for smarter categorization of uncategorized transactions.

Optionally, a machine learning predictor suggests categories based on historical data.

Forecasts next month’s expenses using Holt-Winters Exponential Smoothing.

💡 Future Enhancements

Multi-user support with authentication.

Integration with bank APIs for automatic CSV retrieval.

AI-powered suggestions for budgets & saving strategies.

Export charts and reports as PDF.

📄 License

This project is MIT Licensed. See LICENSE
 for details.

 🤝 Contributions

Feel free to fork, star, and submit pull requests!
For bugs or feature requests, open an issue.

📌 Author

Ahmed Laminou
📧 Email : ahmedlaminouamadou@gmail.com

🌐 GitHub : AhmedLaminou

“Take control of your finances with data-driven insights!” 💹💰