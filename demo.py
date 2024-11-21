import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Lưu Lượng Truy Cập Trang Web')
st.image('dataset-thumbnail.jpg', width=500) 
form = st.form('information_key')
st.header('1.Giới thiệu')
st.subheader('Tổng quan về dữ liệu')
st.markdown('Bộ dữ liệu này cung cấp thông tin chi tiết về lưu lượng truy cập trang web, bao gồm lượt xem trang, thời lượng phiên, tỷ lệ thoát, nguồn lưu lượng truy cập, thời gian dành trên trang, các lượt truy cập trước đó và tỷ lệ chuyển đổi.')
st.subheader('Mô tả dữ liệu')
st.markdown('Lượt xem trang : Số trang được xem trong một phiên.')
st.markdown('Thời lượng phiên : Tổng thời lượng của phiên tính bằng phút.')
st.markdown('Tỷ lệ thoát : Tỷ lệ phần trăm khách truy cập thoát khỏi trang web sau khi chỉ xem một trang.')
st.markdown("Nguồn lưu lượng truy cập : Nguồn gốc của lưu lượng truy cập (ví dụ: Tự nhiên, Xã hội, Trả phí).")
st.markdown('Thời gian trên trang : Lượng thời gian dành cho một trang cụ thể.')
st.markdown("Lượt truy cập trước : Số lượt truy cập trước đó của cùng một khách truy cập.")
st.markdown("Tỷ lệ chuyển đổi : Tỷ lệ phần trăm khách truy cập hoàn tất hành động mong muốn (ví dụ: mua hàng)")

st.header('2.Đọc dữ liệu')
# Đọc dữ liệu từ file CSV
df = pd.read_csv('website_wata.csv')

# Hiển thị thông tin DataFrame
st.write(df.info())

# Hiển thị một số dữ liệu mẫu
st.write(df.head())

st.header('3. Data Visualization')

st.subheader('Sự phân bố của nguồn lưu lượng truy cập')
# Sự phân bố của nguồn lưu lượng truy cập
traffic_counts = df['Traffic Source'].value_counts()
fig = plt.figure(figsize=(10, 5))
plt.bar(traffic_counts.index, traffic_counts.values, color='skyblue')
plt.title('Traffic Source Distribution')
plt.xlabel('Traffic Source')
st.pyplot(fig)
st.markdown('Dựa trên biểu đồ bên dưới, có năm loại nguồn lưu lượng truy cập: Trực tiếp, Không phải trả tiền, Trả phí, Giới thiệu và Xã hội. Trong số này, Lưu lượng truy cập không phải trả tiền là cao nhất, trong khi Lưu lượng truy cập trực tiếp thấp nhất. Phân bổ này nêu bật Lưu lượng truy cập không phải trả tiền là nguồn khách truy cập quan trọng nhất, trong khi Lưu lượng truy cập trực tiếp đóng góp ít nhất')

st.subheader('Thời lượng phiên trung bình theo nguồn lưu trữ truy cập')
# Thời lượng phiên trung bình theo nguồn lưu trữ truy cập
session_duration = round(df.groupby('Traffic Source')['Session Duration'].mean().reset_index(name = 'avg_session_duration'),2)
fig2 = plt.figure(figsize = (10, 6))
ax = sns.barplot(data = session_duration, x = 'Traffic Source', y = 'avg_session_duration', color = 'skyblue')
ax.bar_label(ax.containers[0], fontsize = 10)
plt.title('Avg Session Duration')
plt.xlabel('Traffic Source')
plt.ylabel = ('Average duration (in secs)')
st.pyplot(fig2)
st.markdown('với Organic, Referral và Social là những nguồn hiệu quả nhất trong việc giữ chân người dùng. Điều này có thể ảnh hưởng đến chiến lược marketing và tối ưu hóa nội dung của website.')


st.subheader('Mối quan hệ giữa tỷ lệ thoát và thời lượng phiên')
# Mối quan hệ giữa tỷ lệ thoát và thời lượng phiên
fig3 = plt.figure(figsize = (10, 6))
sns.regplot(x = 'Session Duration', y = 'Bounce Rate', data = df)
plt.title('Session Duration vs Bounce Rate')
st.pyplot(fig3)
st.markdown('Tỷ lệ thoát có xu hướng giảm khi thời gian phiên tăng. Điều này cho thấy rằng người dùng ở lại lâu hơn trên trang thì khả năng thoát của họ cũng thấp hơn.')


st.subheader('Phân phối lượt xem trang')
#Phân phối lượt xem trang
fig4 = plt.figure(figsize = (10, 6))
sns.histplot(df['Page Views'], bins = 15, kde = True)
plt.title('Distribution of page Views')
st.pyplot(fig4)
st.markdown('Dựa trên biểu đồ trên, tần suất xem trang mỗi phiên chiếm ưu thế trong khoảng từ 4 đến 5. Xu hướng này cho thấy hai giá trị này phổ biến nhất đối với người dùng, cho thấy một phiên thông thường bao gồm việc điều hướng qua 4 đến 5 trang')

#Tần suất thời gian trên trang
st.subheader('Tần suất thời gian trên trang')
fig6 = plt.figure(figsize=(10, 5))
plt.hist(df['Time on Page'], 
         bins=range(int(df['Time on Page'].min()), 
                     int(df['Time on Page'].max()) + 1, 1))
plt.title('Frequency of Time on Page')
plt.xlabel('Time On Page')
st.pyplot(fig6)
st.markdown('Dựa trên biểu đồ trên, thời gian cao nhất dành cho một trang là 2 phút, với thời gian dài hơn sẽ giảm dần. Xu hướng này chỉ ra rằng mặc dù một số người dùng tương tác với nội dung tối đa 2 phút nhưng lượng thời gian dành cho mỗi trang thường giảm đi')

st.subheader('Thời gian trên trang so với tỷ lệ chuyển đổi')
# Thời gian trên trang so với tỷ lệ chuyển đổi
df_new = df[(df['Conversion Rate'] == 1) | (df['Conversion Rate'] == 0)]
df_new['Conversion Rate'].value_counts()
fig5 = plt.figure(figsize=(8,4))
sns.scatterplot(x='Time on Page', y='Conversion Rate', data=df)
plt.title('Time On Page vs Conversion Rate')
plt.xlabel('Time On Page')
st.pyplot(fig5)

