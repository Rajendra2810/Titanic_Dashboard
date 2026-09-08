import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="Titanic Analytics Dashboard",
    page_icon="🚢",
    layout="wide"
)

sns.set_theme(style="whitegrid")

# Load Titanic dataset
titanic = sns.load_dataset("titanic")
titanic.to_csv("titanic_dataset.csv", index=False)

st.title("🚢 Titanic Survival Analytics Dashboard")

st.write(
    "Interactive data visualization project using "
    "Python, Streamlit, Pandas, Matplotlib and Seaborn."
)

st.markdown("---")

# Sidebar filters
st.sidebar.header("🔎 Filter Passengers")

selected_sex = st.sidebar.multiselect(
    "Select Gender",
    options=titanic["sex"].dropna().unique(),
    default=titanic["sex"].dropna().unique()
)

selected_class = st.sidebar.multiselect(
    "Select Passenger Class",
    options=titanic["class"].dropna().unique(),
    default=titanic["class"].dropna().unique()
)

selected_embarked = st.sidebar.multiselect(
    "Select Embarkation Port",
    options=titanic["embarked"].dropna().unique(),
    default=titanic["embarked"].dropna().unique()
)

# Filter data
filtered_data = titanic[
    (titanic["sex"].isin(selected_sex)) &
    (titanic["class"].isin(selected_class)) &
    (titanic["embarked"].isin(selected_embarked))
]

# Dashboard metrics
st.subheader("📊 Passenger Overview")

col1, col2, col3, col4 = st.columns(4)

total_passengers = len(filtered_data)
survived = filtered_data["survived"].sum()

survival_rate = (
    filtered_data["survived"].mean() * 100
    if len(filtered_data) > 0
    else 0
)

average_age = filtered_data["age"].mean()

col1.metric("Total Passengers", total_passengers)
col2.metric("Survived", int(survived))
col3.metric("Survival Rate", f"{survival_rate:.2f}%")
col4.metric("Average Age", f"{average_age:.1f} Years")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Survival Analysis",
    "👨‍👩‍👧 Gender Analysis",
    "💰 Fare Analysis",
    "🎂 Age Analysis",
    "🔥 Correlation"
])

# Survival Analysis
with tab1:

    st.subheader("Survival by Passenger Class")

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=filtered_data,
        x="class",
        hue="survived",
        palette="Set2",
        ax=ax
    )

    ax.set_title("Passenger Survival by Class")
    ax.set_xlabel("Passenger Class")
    ax.set_ylabel("Number of Passengers")

    st.pyplot(fig)

    plt.close(fig)


# Gender Analysis
with tab2:

    st.subheader("Survival Rate by Gender")

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        data=filtered_data,
        x="sex",
        y="survived",
        palette="pastel",
        ax=ax
    )

    ax.set_title("Average Survival Rate by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Survival Rate")

    st.pyplot(fig)

    plt.close(fig)


# Fare Analysis
with tab3:

    st.subheader("Passenger Fare Analysis")

    col1, col2 = st.columns(2)

    with col1:

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.histplot(
            data=filtered_data,
            x="fare",
            bins=30,
            kde=True,
            ax=ax
        )

        ax.set_title("Distribution of Passenger Fares")
        ax.set_xlabel("Fare")

        st.pyplot(fig)

        plt.close(fig)

    with col2:

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.boxplot(
            data=filtered_data,
            x="class",
            y="fare",
            hue="sex",
            palette="Set3",
            ax=ax
        )

        ax.set_title("Fare by Passenger Class")
        ax.set_xlabel("Passenger Class")
        ax.set_ylabel("Fare")

        st.pyplot(fig)

        plt.close(fig)


# Age Analysis
with tab4:

    st.subheader("Age and Survival Analysis")

    col1, col2 = st.columns(2)

    with col1:

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.histplot(
            data=filtered_data,
            x="age",
            hue="survived",
            kde=True,
            multiple="stack",
            palette="Set1",
            ax=ax
        )

        ax.set_title("Age Distribution by Survival")
        ax.set_xlabel("Age")

        st.pyplot(fig)

        plt.close(fig)

    with col2:

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.violinplot(
            data=filtered_data,
            x="class",
            y="age",
            hue="sex",
            split=True,
            palette="muted",
            ax=ax
        )

        ax.set_title("Age Distribution by Class and Gender")

        st.pyplot(fig)

        plt.close(fig)


# Correlation
with tab5:

    st.subheader("🔥 Correlation Heatmap")

    numerical_data = filtered_data[
        [
            "survived",
            "pclass",
            "age",
            "sibsp",
            "parch",
            "fare"
        ]
    ]

    correlation = numerical_data.corr()

    fig, ax = plt.subplots(figsize=(9, 6))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title("Correlation Between Titanic Variables")

    st.pyplot(fig)

    plt.close(fig)


# Scatter Plot
st.markdown("---")

st.subheader("💰 Age vs Fare Relationship")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=filtered_data,
    x="age",
    y="fare",
    hue="survived",
    size="pclass",
    sizes=(30, 200),
    alpha=0.7,
    palette="deep",
    ax=ax
)

ax.set_title("Age vs Fare Based on Survival")
ax.set_xlabel("Passenger Age")
ax.set_ylabel("Fare")

st.pyplot(fig)

plt.close(fig)


# Dataset
st.markdown("---")


if st.checkbox("Show Dataset"):

    st.dataframe(
        filtered_data[
            [
                "survived",
                "pclass",
                "sex",
                "age",
                "fare",
                "class",
                "embarked"
            ]
        ],
        use_container_width=True
    )


st.markdown("---")

st.info(
    "Project developed by Rajendra Sahoo | "
    "Python • Streamlit • Pandas • Seaborn • Matplotlib"
)