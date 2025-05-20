import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# concate multiple csv files in one csv file 
df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')

files = [file for file in os.listdir('./Sales_Data')]
all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('./Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv('all_data_manish.csv', index = False)




all_data = pd.read_csv("./all_data_manish.csv")
all_data['Months'] = all_data['Order Date'].str[0:2]
all_data.dropna(how='all', inplace = True)
all_data = all_data[all_data['Months'].str[0:2] != 'Or']     # changing the 10's digit place of months
all_data['Months'] = all_data['Months'].astype(np.int32)     # changing the data type of months 

# print('quant = ',all_data['Quantity Ordered'].dtype,'\n','price = ', all_data['Price Each'].dtype)
all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(np.int64)
all_data['Price Each'] = all_data['Price Each'].astype(np.float64)
all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
print(all_data['Sales'].dtype)
# print(all_data.head(50))
# nan = print(all_data.isnull().sum())







 
#Ques.1 - what was the month with best sales? how much was earned that month?
sales_sum = all_data.groupby('Months').sum()
print(sales_sum)

months = range(1,13)
plt.bar(months, sales_sum['Sales'])
plt.xticks(months)
plt.xlabel('Months numbers')
plt.ylabel('Sales in USD ($)')
plt.title('Total Sale in Months')
plt.ticklabel_format(style='plain',axis='y')

plt.show()






#Ques.2 -  which city had the highest number of sales?
# def get_city(address):
#     return address.split(',')[1]

# all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x))


# city_sales = all_data.groupby('City').sum()
# print(city_sales)
# cities = [city for city, df in all_data.groupby('City')]
# plt.bar(cities, city_sales['Sales'])
# plt.ticklabel_format(style='plain',axis='y')
# plt.xticks(cities, rotation=15, size=7)
# plt.yticks(size=7)
# plt.xlabel('Cities')
# plt.ylabel('Sales in USD ($)')
# plt.show()





# sales and Quantity with respected cities 
# plt.rc('figure', figsize=(50, 6))
# Fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.bar(cities, city_sales['Sales'])
# ax2.plot(cities, city_sales['Quantity Ordered'], 'b--')
# ax1.ticklabel_format(style='plain',axis='y')
# ax1.set_xlabel('Cities')
# ax1.set_ylabel('Sales in $')
# ax2.set_ylabel('Numbers of Ordered Quantity')
# ax1.set_xticklabels(cities, rotation=15, size=7)
# plt.show()









#Ques.3 - what time should we display ads to maximize likelihood of customers buying products?
# all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
# all_data['Hour'] = all_data['Order Date'].dt.hour
# time_sales = all_data.groupby('Hour').sum()
# hours = [hour for hour, df in all_data.groupby('Hour')]
# plt.plot(hours, all_data.groupby(['Hour']).count(),'b--')
# plt.xticks(hours)
# plt.xlabel('hours')
# plt.ylabel('No. of Orders')
# plt.grid()
# plt.show()







#Ques.4 - which products are most often sold ?

# prod_sales = all_data.groupby('Product')
# quant_ordered = prod_sales.sum()['Quantity Ordered']
# products = [product for product, df in prod_sales]
# plt.barh(products, quant_ordered)
# plt.yticks(products,rotation=35, size=7)
# plt.ylabel('products')

# plt.xlabel('Quantity Ordered')

# plt.show()




# Ques.5 -  Does price of each product affect the No. of Ordered Quantity?
each_prdct = all_data.groupby('Product').mean()['Price Each']
sales_prdct = all_data.groupby('Product').sum()
print(sales_prdct)
# prodcts = [product for product, df in all_data.groupby('Product')]


# Fig, ax1 = plt.subplots()
# ax2 = ax1.twiny()
# ax1.barh(prodcts, sales_prdct['Quantity Ordered'],color = 'skyblue')
# ax2.plot(each_prdct,prodcts, 'b--')

# ax2.ticklabel_format(style='plain',axis='x')
# ax1.set_ylabel('Products')
# ax1.set_xlabel('Numbers of Ordered Quantity')
# ax2.set_xlabel('Price of Each Product in $')
# leg1 = ['Quantity']
# leg2 = ['Price Each']
# ax1.legend(leg1,loc = 'lower right')
# ax2.legend(leg2,loc='right')
# ax1.set_yticklabels(prodcts, rotation=30, size=6.5)
# plt.show()


print("\n")




# sales_prdct1 = all_data.groupby('Product').sum()
# print(sales_prdct1)
# odrd_qt = sales_prdct1['Quantity Ordered']
# prodcts = [product for product, df in all_data.groupby('Product')]

# Fig, ax1 = plt.subplots()
# ax2 = ax1.twiny()
# ax1.barh(prodcts,sales_prdct1['Quantity Ordered'],color = 'skyblue')
# ax2.plot(sales_prdct1['Sales'],prodcts, 'b--')

# ax2.ticklabel_format(style='plain',axis='x')
# ax1.set_ylabel('Products')
# ax1.set_xlabel('Numbers of Ordered Quantity')
# ax2.set_xlabel('Sales in $')
# leg1 = ['Quantity']
# leg2 = ['Sales']
# ax1.legend(leg1,loc = 'lower right')
# ax2.legend(leg2,loc='right')
# ax1.set_yticklabels(prodcts, rotation=30, size=6.5)
# plt.show()


