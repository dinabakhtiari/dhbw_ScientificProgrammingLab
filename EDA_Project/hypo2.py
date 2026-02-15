import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('EDA_Project/KC_housing_data.csv')

df = df[df['price'] > 0]

#df['date'] = pd.to_datetime(df['date'])
#df['month'] = df['date'].dt.month

# Missing Values
# print(df.isnull().sum())

#monthly_trend = df.groupby('month')['price'].mean().reset_index()

#plt.figure(figsize=(10, 6))
#sns.lineplot(data=monthly_trend, x='month', y='price', marker='o', color='red', linewidth=3)

#plt.title('Best Time to Buy or Sell (Price Trend)', fontsize=15)
#plt.xlabel('Month', fontsize=12)
#plt.ylabel('Average Price ($)', fontsize=12)
#plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
#plt.grid(True, linestyle='--', alpha=0.6)

#plt.show()

#print("Monthly Average Price Trend:")
#print(monthly_trend)

# تحلیل بر اساس نمودار:
#در بازه زمانی موجود در فایل شما (می تا جولای ۲۰۱۴)، روند قیمت‌ها کاملاً صعودی است.
#بهترین زمان برای خرید (Buying):
#ماه می (May): طبق نمودار، پایین‌ترین میانگین قیمت مربوط به ماه می است (حدود ۵۴۰ هزار دلار). بنابراین برای خریداری که به دنبال قیمت کمتر است، شروع بازه زمانی (ماه می) بهترین زمان بوده است.
#بهترین زمان برای فروش (Selling): ماه جولای (July): نمودار نشان می‌دهد که قیمت‌ها به شدت افزایش یافته و در ماه جولای به بالاترین حد خود رسیده‌اند (حدود ۶۱۹ هزار دلار). بنابراین برای فروشندگان، جولای بهترین ماه برای کسب سود بیشتر است.

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# --- نمودار اول: تأثیر موقعیت (Waterfront) بر قیمت ---
sns.boxplot(ax=axes[0], x='waterfront', y='price', data=df, palette="husl")
axes[0].set_title('Impact of Location: Waterfront vs Regular', fontsize=15)
axes[0].set_xlabel('Waterfront (0 = No, 1 = Yes)', fontsize=12)
axes[0].set_ylabel('Price (Log Scale)', fontsize=12)
axes[0].set_yscale('log') # استفاده از مقیاس لگاریتمی برای نمایش بهتر اختلاف قیمت‌های میلیونی

# --- نمودار دوم: تأثیر اندازه (Bedrooms) بر قیمت ---
sns.barplot(ax=axes[1], x='bedrooms', y='price', data=df, palette="viridis")
axes[1].set_title('Impact of Size: Number of Bedrooms vs Price', fontsize=15)
axes[1].set_xlabel('Number of Bedrooms', fontsize=12)
axes[1].set_ylabel('Average Price ($)', fontsize=12)

plt.tight_layout()
plt.show()

corr_rooms = df['price'].corr(df['bedrooms'])
corr_waterfront = df['price'].corr(df['waterfront'])

print(f"Correlation between Price and Bedrooms: {corr_rooms:.2f}")
print(f"Correlation between Price and Waterfront: {corr_waterfront:.2f}")
