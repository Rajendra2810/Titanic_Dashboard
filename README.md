# Titanic_Dashboard

# 🚢 Titanic Survival Analytics Dashboard

An interactive **Titanic data analysis and visualization dashboard** built using **Python, Streamlit, Pandas, Matplotlib, and Seaborn**.

The dashboard allows users to explore passenger survival patterns based on **gender, passenger class, age, fare, embarkation port, and other numerical variables**.

---

## 📌 Project Overview

The **Titanic Survival Analytics Dashboard** provides an interactive way to analyze the famous Titanic dataset.

Users can apply filters from the sidebar and dynamically explore:

* Passenger survival by class
* Survival rate by gender
* Passenger fare distribution
* Fare differences by class and gender
* Age distribution by survival
* Age distribution by class and gender
* Correlations between numerical variables
* Age vs. fare relationship
* Filtered passenger data

---

## 🛠️ Technologies Used

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| 🐍 Python     | Programming language            |
| 🎨 Seaborn    | Statistical data visualization  |
| 📊 Matplotlib | Plot creation and customization |
| 🐼 Pandas     | Data manipulation and analysis  |
| 🖥️ Streamlit | Interactive web dashboard       |

---

## 📂 Project Structure

```text
Titanic-Analytics-Dashboard/
│
├── Titanic_Dashboard.py
├── titanic_dataset.csv
├── README.md
└── requirements.txt
```

> Change `Titanic_Dashboard.py` to your actual Python filename if it is different.

---

## 📊 Dashboard Features

### 🔎 1. Interactive Filters

The sidebar provides filters for:

* Gender
* Passenger Class
* Embarkation Port

The dashboard automatically updates the charts and metrics according to the selected filters.

---

### 📊 2. Passenger Overview

The dashboard displays four important metrics:

* **Total Passengers**
* **Survived Passengers**
* **Survival Rate**
* **Average Age**

Example:

```text
Total Passengers    Survived    Survival Rate    Average Age
       891             342          38.38%          29.7 Years
```

The values change dynamically when filters are applied.

---

### 📈 3. Survival Analysis

The Survival Analysis tab shows passenger survival based on **Passenger Class**.

It uses a Seaborn `countplot()` to compare:

* Survived passengers
* Non-survived passengers
* First class
* Second class
* Third class

---

### 👨‍👩‍👧 4. Gender Analysis

The Gender Analysis tab displays the average survival rate for:

* Male passengers
* Female passengers

A Seaborn `barplot()` is used to visualize the difference.

---

### 💰 5. Fare Analysis

The Fare Analysis tab contains two visualizations.

#### Fare Distribution

A histogram with KDE shows the distribution of passenger fares.

#### Fare by Passenger Class

A box plot compares fares across passenger classes and gender.

---

### 🎂 6. Age Analysis

The Age Analysis tab contains two visualizations.

#### Age Distribution by Survival

A histogram shows the age distribution of passengers based on survival status.

#### Age Distribution by Class and Gender

A violin plot shows how passenger ages are distributed across different classes and genders.

---

### 🔥 7. Correlation Analysis

A correlation heatmap is used to analyze relationships between numerical variables:

```text
survived
pclass
age
sibsp
parch
fare
```

The heatmap displays correlation coefficients between the variables.

---

### 💰 8. Age vs Fare Relationship

A scatter plot analyzes the relationship between:

* Passenger Age
* Fare

The plot also uses:

* Color → Survival status
* Point size → Passenger class

This helps identify patterns between age, ticket fare, passenger class, and survival.

---

### 📋 9. Dataset Viewer

Users can select **"Show Dataset"** to display the filtered Titanic dataset.

The dashboard displays:

```text
survived
pclass
sex
age
fare
class
embarked
```

The dataset automatically updates according to the selected filters.

---

## 📁 Dataset

The project uses the Titanic dataset provided by **Seaborn**.

The dataset is loaded using:

```python
titanic = sns.load_dataset("titanic")
```

The application also saves the dataset locally as:

```python
titanic.to_csv("titanic_dataset.csv", index=False)
```

This creates:

```text
titanic_dataset.csv
```

in the project folder.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Titanic-Analytics-Dashboard.git
```

### 2. Open the Project Folder

```bash
cd Titanic-Analytics-Dashboard
```

### 3. Install Required Libraries

```bash
pip install streamlit seaborn matplotlib pandas
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

Run:

```bash
streamlit run Titanic_Dashboard.py
```

After running the command, Streamlit will provide a local address such as:

```text
http://localhost:8501
```

Open the address in your web browser.

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
seaborn
matplotlib
pandas
```

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Learning Objectives

This project helped me practice:

* Python programming
* Pandas data manipulation
* Seaborn data visualization
* Matplotlib plotting
* Streamlit dashboard development
* Interactive sidebar filters
* Data aggregation
* Correlation analysis
* Statistical visualization
* Working with the Titanic dataset
* Creating reusable data-analysis dashboards
* Exporting datasets to CSV

---

## 💡 Key Insights

The dashboard can be used to explore questions such as:

* Which passenger class had better survival outcomes?
* How did survival differ between male and female passengers?
* What was the distribution of passenger fares?
* How did age vary among passengers?
* Is fare related to survival?
* What relationships exist between the numerical Titanic variables?

---

## 🚀 Future Improvements

Some possible improvements for future versions:

* Add more interactive filters
* Add a passenger-name search
* Add survival percentage charts
* Add downloadable filtered data
* Add Plotly interactive charts
* Add KPI cards with additional statistics
* Add machine-learning survival prediction
* Add passenger survival prediction form
* Deploy the dashboard online using Streamlit Community Cloud

---

## 📸 Dashboard Preview

Add your Streamlit dashboard screenshot here:

```markdown
![Titanic Dashboard](dashboard_screenshot.png)
```

You can take a screenshot of your running Streamlit application and save it as:

```text
dashboard_screenshot.png
```

inside your GitHub project folder.

---

## 👨‍💻 Author

### Rajendra Sahoo

This project was developed as part of my learning journey in **Python, Pandas, Seaborn, Matplotlib, and Streamlit**, with a focus on practical data analysis and visualization.

---

## ⭐ Project Support

If you found this project useful, please consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is created for **educational and learning purposes**.
