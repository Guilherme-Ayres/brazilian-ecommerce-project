import pandas as pd

dfs = {}

# --- Etapa de Preparação e Limpeza dos Dados ---
# --- Conversão de Tipos de Dados ---

print("\n--- Iniciando a conversão de tipos de dados ---")

# DataFrame: customers
print("\n--- DataFrame: customers ---")
if 'customers' in dfs:
    # Manter customer_id e customer_unique_id como object

    # Converter customer_city para category
    dfs['customers']['customer_city'] = dfs['customers']['customer_city'].astype('category')
    print("Coluna 'customer_city' convertida para category.")

    # Converter customer_state para category
    dfs['customers']['customer_state'] = dfs['customers']['customer_state'].astype('category')
    print("Coluna 'customer_state' convertida para category.")

    print("\nTipos de dados após conversão em 'customers':")
    print(dfs['customers'].info())
else:
    print("DataFrame 'customers' não encontrado.")

# DataFrame: geolocation
print("\n--- DataFrame: geolocation ---")
if 'geolocation' in dfs:
    # Converter geolocation_city para category
    dfs['geolocation']['geolocation_city'] = dfs['geolocation']['geolocation_city'].astype('category')
    print("Coluna 'geolocation_city' convertida para category.")

    # Converter geolocation_state para category
    dfs['geolocation']['geolocation_state'] = dfs['geolocation']['geolocation_state'].astype('category')
    print("Coluna 'geolocation_state' convertida para category.")

    print("\nTipos de dados após conversão em 'geolocation':")
    print(dfs['geolocation'].info())
else:
    print("DataFrame 'geolocation' não encontrado.")

# DataFrame: orders
print("\n--- DataFrame: orders ---")
if 'orders' in dfs:
    # Converter order_status para category
    dfs['orders']['order_status'] = dfs['orders']['order_status'].astype('category')
    print("Coluna 'order_status' convertida para category.")

    # Converter colunas de data para datetime64
    date_cols_orders = ['order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
    for col in date_cols_orders:
        dfs['orders'][col] = pd.to_datetime(dfs['orders'][col])
        print(f"Coluna '{col}' convertida para datetime64.")

    print("\nTipos de dados após conversão em 'orders':")
    print(dfs['orders'].info())
else:
    print("DataFrame 'orders' não encontrado.")

# DataFrame: order_items
print("\n--- DataFrame: order_items ---")
if 'order_items' in dfs:
    # Converter order_item_id para int64
    dfs['order_items']['order_item_id'] = dfs['order_items']['order_item_id'].astype('int64')
    print("Coluna 'order_item_id' convertida para int64.")

    # Converter shipping_limit_date para datetime64
    dfs['order_items']['shipping_limit_date'] = pd.to_datetime(dfs['order_items']['shipping_limit_date'])
    print("Coluna 'shipping_limit_date' convertida para datetime64.")

    # Converter price para float64
    dfs['order_items']['price'] = dfs['order_items']['price'].astype('float64')
    print("Coluna 'price' convertida para float64.")

    # Converter freight_value para float64
    dfs['order_items']['freight_value'] = dfs['order_items']['freight_value'].astype('float64')
    print("Coluna 'freight_value' convertida para float64.")

    print("\nTipos de dados após conversão em 'order_items':")
    print(dfs['order_items'].info())
else:
    print("DataFrame 'order_items' não encontrado.")

# DataFrame: order_payments
print("\n--- DataFrame: order_payments ---")
if 'order_payments' in dfs:
    # Converter payment_sequential para int64
    dfs['order_payments']['payment_sequential'] = dfs['order_payments']['payment_sequential'].astype('int64')
    print("Coluna 'payment_sequential' convertida para int64.")

    # Converter payment_type para category
    dfs['order_payments']['payment_type'] = dfs['order_payments']['payment_type'].astype('category')
    print("Coluna 'payment_type' convertida para category.")

    # Converter payment_installments para int64
    dfs['order_payments']['payment_installments'] = dfs['order_payments']['payment_installments'].astype('int64')
    print("Coluna 'payment_installments' convertida para int64.")

    # Converter payment_value para float64
    dfs['order_payments']['payment_value'] = dfs['order_payments']['payment_value'].astype('float64')
    print("Coluna 'payment_value' convertida para float64.")

    print("\nTipos de dados após conversão em 'order_payments':")
    print(dfs['order_payments'].info())
else:
    print("DataFrame 'order_payments' não encontrado.")

# DataFrame: order_reviews
print("\n--- DataFrame: order_reviews ---")
if 'order_reviews' in dfs:
    # Converter review_score para int64
    dfs['order_reviews']['review_score'] = dfs['order_reviews']['review_score'].astype('int64')
    print("Coluna 'review_score' convertida para int64.")

    # Converter review_creation_date para datetime64
    dfs['order_reviews']['review_creation_date'] = pd.to_datetime(dfs['order_reviews']['review_creation_date'])
    print("Coluna 'review_creation_date' convertida para datetime64.")

    # Converter review_answer_timestamp para datetime64
    dfs['order_reviews']['review_answer_timestamp'] = pd.to_datetime(dfs['order_reviews']['review_answer_timestamp'])
    print("Coluna 'review_answer_timestamp' convertida para datetime64.")

    print("\nTipos de dados após conversão em 'order_reviews':")
    print(dfs['order_reviews'].info())
else:
    print("DataFrame 'order_reviews' não encontrado.")

# DataFrame: products
print("\n--- DataFrame: products ---")
if 'products' in dfs:
    # Converter product_category_name para category
    dfs['products']['product_category_name'] = dfs['products']['product_category_name'].astype('category')
    print("Coluna 'product_category_name' convertida para category.")

    # Converter colunas de comprimento para float64
    len_cols_products = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty',
                         'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
    for col in len_cols_products:
        dfs['products'][col] = dfs['products'][col].astype('float64')
        print(f"Coluna '{col}' convertida para float64.")

    print("\nTipos de dados após conversão em 'products':")
    print(dfs['products'].info())
else:
    print("DataFrame 'products' não encontrado.")

# DataFrame: sellers
print("\n--- DataFrame: sellers ---")
if 'sellers' in dfs:
    # Converter seller_city para category
    dfs['sellers']['seller_city'] = dfs['sellers']['seller_city'].astype('category')
    print("Coluna 'seller_city' convertida para category.")

    # Converter seller_state para category
    dfs['sellers']['seller_state'] = dfs['sellers']['seller_state'].astype('category')
    print("Coluna 'seller_state' convertida para category.")

    print("\nTipos de dados após conversão em 'sellers':")
    print(dfs['sellers'].info())
else:
    print("DataFrame 'sellers' não encontrado.")

# DataFrame: product_category_name_translation
print("\n--- DataFrame: product_category_name_translation ---")
if 'product_category_name_translation' in dfs:
    # Converter product_category_name para category
    dfs['product_category_name_translation']['product_category_name'] = \
        dfs['product_category_name_translation']['product_category_name'].astype('category')
    print("Coluna 'product_category_name' convertida para category.")

    # Converter product_category_name_english para category
    dfs['product_category_name_translation']['product_category_name_english'] = \
        dfs['product_category_name_translation']['product_category_name_english'].astype('category')
    print("Coluna 'product_category_name_english' convertida para category.")

    print("\nTipos de dados após conversão em 'product_category_name_translation':")
    print(dfs['product_category_name_translation'].info())
else:
    print("DataFrame 'product_category_name_translation' não encontrado.")

print("\n--- Conversão de tipos de dados concluída ---")