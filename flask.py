# Module Name : lec_flask_test.py

## DEFAULT
# static: 정적 파일
# templates: html 파일 

from flask import Flask, render_template
from dbconnect import get_table
import pandas as pd

app = Flask(__name__)

#http://localhost:8078/
@app.route('/')
def index():
    
    # Table Data
    query = 'SELECT * FROM avg_revenue order by 증가율 desc'
    avg_revenue = get_table(query)
    avg_revenue.update(avg_revenue.select_dtypes(include='int64').applymap('{:,}'.format))

    # Bar Chart Data
        # 매출 건수
    query = "SELECT * FROM online_item order by prod_category"
    q_cnt = get_table(query)
   

        # 매출
    query = "SELECT * FROM online_sales_rate order by prod_category"
    q_sales = get_table(query)
    q_sales['prod_category'] = q_sales['prod_category'].replace({"및": ","}, regex = True)

    #total Data
    query = "SELECT prod_category, sum(sales_amount) as sum FROM online_sales_new " \
            "WHERE extract(year from sales_date) = '2020' GROUP BY prod_category ORDER BY SUM(sales_amount) DESC"
    q_sales_money = get_table(query)

    #Pie chart Data
    query  = "SELECT * FROM annual_sales_amount order by 예상매출건수2020 desc"
    q_sales_amount  = get_table(query)
    


    return render_template("index.html", avg_df = avg_revenue, q_cnt = q_cnt, q_sales = q_sales, sales_amount = q_sales_amount, sales_money = q_sales_money)

# http://localhost:8078/info  
@app.route('/info')
def info():
    return 'Info'

if __name__ == '__main__':
    app.run(host='localhost', port=8078, debug=True)  
