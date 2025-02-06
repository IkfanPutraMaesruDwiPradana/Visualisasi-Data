import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#judul
st.title("Visualisasi Data")

#sidebar untuk memilih datasets
datasets = sns.get_dataset_names()
dataset_name = st.sidebar.selectbox("Pilih Dataset", datasets)

#load dataset
data = sns.load_dataset(dataset_name)

#menampilkan informasi
st.subheader("Informasi Dataset")
st.write(f"Dataset: {dataset_name}")
st.write("Dimensi data:", data.shape)
st.write(data.tail())

#Membuat visualization
graph_type = st.sidebar.selectbox("Pilih Visualisasi", ["Histogram", "Boxplot", "Scatterplot", "Korelasi"])

#memilih kolom dataset
columns = data.columns

#visualisasi histogram
if graph_type == "Histogram":
    columns = st.sidebar.selectbox("pilih Visualisasi", columns)
    bins =st.sidebar.slider("jumlah bin", min_value=5, max_value=50, value=20)
    
    #plot histogram
    fig, ax=plt.subplots()
    sns.histplot(data[columns], bins=bins, kde=False, ax=ax)
    st.pyplot(fig)

#visualisasi boxplot
if graph_type == "Boxplot":
    x_column = st.sidebar.selectbox("Kolom X", columns)
    y_column = st.sidebar.selectbox("Kolom Y", columns, disabled=True)
    
    #plot boxplot
    fig, ax=plt.subplots()
    sns.boxplot(x=x_column, y=y_column, data=data, ax=ax)
    st.pyplot(fig)
    
#visualisasi scatterplot
if graph_type == "Scatterplot":
    x_column = st.sidebar.selectbox("Kolom X", columns)
    y_column = st.sidebar.selectbox("Kolom Y", columns)
    hue_column = st.sidebar.selectbox("pilih kolom hue (opsional)",[None] + list(columns))
   #plot scatterplot
    fig, ax=plt.subplots()
    sns.scatterplot(data=data, x=x_column, y=y_column, hue=hue_column, ax=ax)
    st.pyplot(fig)