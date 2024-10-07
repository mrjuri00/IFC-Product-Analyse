import streamlit as st
import ifcopenshell
import pandas as pd
import matplotlib.pyplot as plt

st.header('IFC Product Analyse')
st.write('Dieses Script analysiert die Anzahl IFC-Products in einem IFC.')

uploaded_file = st.file_uploader('Upload your IFC here')

if uploaded_file:

    # Load IFC file (replace 'path_to_ifc_file.ifc' with the actual path)
    model = ifcopenshell.file.from_string(uploaded_file.getvalue().decode("utf-8"))

    # Dictionary to store type counts
    type_counts = {}

    # Get all IfcProduct entities (including subtypes)
    products = model.by_type('IfcProduct')

    # Iterate over all products in the model
    for product in products:
        product_type = product.is_a()
        if product_type in type_counts:
            type_counts[product_type] += 1
        else:
            type_counts[product_type] = 1

    # Create DataFrame
    df = pd.DataFrame(list(type_counts.items()), columns=['IFC Type', 'Count'])
    st.dataframe(df, use_container_width=True)

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['IFC Type'], df['Count'], color='skyblue')
    ax.set_xlabel('IFC Type')
    ax.set_ylabel('Anzahl')
    ax.set_title('Anzahl der IFC-Produkte nach Typ')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the chart in Streamlit
    st.pyplot(fig)