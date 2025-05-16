import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

data_dir = './'

csv_files = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_products_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
]

dfs = {}

for file in csv_files:
    file_path = f"{data_dir}{file}"
    table_name = file.replace('.csv', '').replace('olist_', '')
    try:
        dfs[table_name] = pd.read_csv(file_path)
        print(f"DataFrame '{table_name}' carregado com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado. Certifique-se de que o diretório está correto.")

# Primeira verificação de cada DataFrame
for table_name, df in dfs.items():
    print(f"\n--- Explorando o DataFrame: {table_name} ---")
    print("\nPrimeiras 5 linhas:")
    print(df.head())
    print("\nInformações gerais:")
    print(df.info())
    print("\nEstatísticas descritivas (para colunas numéricas):")
    print(df.describe())
    print("\nNúmero de valores nulos por coluna:")
    print(df.isnull().sum())
    print("\nNúmero de valores duplicados:")
    print(df.duplicated().sum())
    print("\nNomes das colunas:")
    print(df.columns)