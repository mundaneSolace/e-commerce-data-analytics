import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# membuat header
st.title('E-Commerce Dashboard :sparkles:')

# load berkas all_data_df.csv sebagai sebuah DataFrame menggunakan kode berikut
file_path_all_data_df_csv = r'C:\Users\yudar\file_visual_studio_code\berkas_submission_dicoding\dashboard\all_data_df.csv'
all_df = pd.read_csv(file_path_all_data_df_csv)

# mencari jumlah nunique dalam order_id
ordersum_df = all_df.groupby(by="product_category_name_english").order_id.nunique().sort_values(ascending=False) 
# membuat data frame baru dari hasil groupby
result_ordersum = ordersum_df.reset_index().copy()
# membatasi jumlah data menjadi 10
top_10_data_order = (result_ordersum.nlargest(10, 'order_id')).sort_values(by='order_id', ascending=True)

# mencari jumlah nunique dalam customer_id
customersum_df = all_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)
# membuat data frame baru dari hasil groupby
result_customersum = customersum_df.reset_index().copy()
# membatasi jumlah data menjadi 10
top_10_data_cust = (result_customersum.nlargest(10, 'customer_id')).sort_values(by='customer_id', ascending=True)

# mencari jumlah nunique dalam seller_id
sellersum_df = all_df.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False)
# membuat data frame baru dari hasil groupby
result_sellersum = sellersum_df.reset_index().copy()
# membatasi jumlah data menjadi 10
top_10_data_seller = (result_sellersum.nlargest(10, 'seller_id')).sort_values(by='seller_id', ascending=True)

# Visualisasi Kategori Produk Terjual
st.subheader('Kategori Produk Paling Banyak Terjual')
fig_produk = plt.figure(figsize=(10, 6))
plt.barh(top_10_data_order['product_category_name_english'], top_10_data_order['order_id'], color='skyblue')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Kategori Produk')
plt.title('10 Penjualan Terbanyak Berdasarkan Kategori Produk')
st.pyplot(fig_produk)

# Visualisasi distribusi geografis pelanggan
st.subheader('Distribusi Geografis Pelanggan')
fig_geografis = plt.figure(figsize=(10, 6))
plt.barh(top_10_data_cust['customer_city'], top_10_data_cust['customer_id'], color='skyblue')
plt.xlabel('Jumlah Pelanggan')
plt.ylabel('City')
plt.title('Distribusi Geografis Pelanggan')
st.pyplot(fig_geografis)

# Visualisasi distribusi geografis penjual
st.subheader('Distribusi Geografis Penjual')
fig_geografis = plt.figure(figsize=(10, 6))
plt.barh(top_10_data_seller['seller_city'], top_10_data_seller['seller_id'], color='skyblue')
plt.xlabel('Jumlah Penjual')
plt.ylabel('City')
plt.title('Distribusi Geografis Penjual')
st.pyplot(fig_geografis)