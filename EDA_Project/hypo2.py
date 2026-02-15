import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('EDA_Project/KC_housing_data.csv')

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

# Missing Values
# print(df.isnull().sum())

monthly_trend = df.groupby('month')['price'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_trend, x='month', y='price', marker='o', color='red', linewidth=3)

plt.title('Best Time to Buy or Sell (Price Trend)', fontsize=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Price ($)', fontsize=12)
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

print("Monthly Average Price Trend:")
print(monthly_trend)

# تحلیل بر اساس نمودار:
#در بازه زمانی موجود در فایل شما (می تا جولای ۲۰۱۴)، روند قیمت‌ها کاملاً صعودی است.
#بهترین زمان برای خرید (Buying):
#ماه می (May): طبق نمودار، پایین‌ترین میانگین قیمت مربوط به ماه می است (حدود ۵۴۰ هزار دلار). بنابراین برای خریداری که به دنبال قیمت کمتر است، شروع بازه زمانی (ماه می) بهترین زمان بوده است.
#بهترین زمان برای فروش (Selling): ماه جولای (July): نمودار نشان می‌دهد که قیمت‌ها به شدت افزایش یافته و در ماه جولای به بالاترین حد خود رسیده‌اند (حدود ۶۱۹ هزار دلار). بنابراین برای فروشندگان، جولای بهترین ماه برای کسب سود بیشتر است.