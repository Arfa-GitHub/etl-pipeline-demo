import pandas as pd

# مرحله Extract - ساخت فایل CSV نمونه
data = {
    "Name": ["Ali", "Sara", "Reza"],
    "Sales": [100, 200, 150]
}
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

print("✅ CSV file created: sales_data.csv")

# مرحله Transform - محاسبه مجموع فروش
total_sales = df["Sales"].sum()
print(f"📊 Total Sales: {total_sales}")

# مرحله Load - شبیه‌سازی ذخیره خروجی
with open("output.txt", "w") as f:
    f.write(f"Total Sales = {total_sales}")

print("✅ Output saved to output.txt")
