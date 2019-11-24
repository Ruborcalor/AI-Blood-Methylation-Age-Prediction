#!/usr/bin/env python3

# Running the script
# 1. Install necessary packages by running "pip install -r requirements.txt"
# 2. Run parse.py
# 3. The bar graph will be written to bar_chart.png and the table will be written to table.png

import csv
import plotly.graph_objects as go

mortgage_loan_sum = 0
mortgage_loan_counter = 0
own_loan_sum = 0
own_loan_counter = 0
rent_loan_sum = 0
rent_loan_counter = 0

# Populating loan_sum and loan_counter for mortgage, own, and rent
with open('home_ownership_data.csv', 'rt') as home_ownership_csv:
    home_ownership_data_reader = csv.reader(home_ownership_csv)
    header = next(home_ownership_data_reader)

    loan_amount = 0

    for home_ownership_row in home_ownership_data_reader:

        with open('loan_data.csv', 'rt') as loan_data_csv:
            loan_data_reader = csv.reader(loan_data_csv)
            header = next(loan_data_reader)

            for loan_data_row in loan_data_reader:
                if int(home_ownership_row[0]) == int(loan_data_row[0]):
                    loan_amount = int(loan_data_row[1])

            if home_ownership_row[1] == 'MORTGAGE':
                mortgage_loan_sum += loan_amount
                mortgage_loan_counter += 1
            elif home_ownership_row[1] == 'OWN':
                own_loan_sum += loan_amount
                own_loan_counter += 1
            elif home_ownership_row[1] == 'RENT':
                rent_loan_sum += loan_amount
                rent_loan_counter += 1

# Calculate Averages
mortgage_loan_average = mortgage_loan_sum  / mortgage_loan_counter
own_loan_average = own_loan_sum  / own_loan_counter
rent_loan_average = rent_loan_sum  / rent_loan_counter

loan_types = ["MORTGAGE", "OWN", "RENT"]
loan_averages = [mortgage_loan_average, own_loan_average, rent_loan_average]

# Creating Bar Chart
bar_chart = go.Figure([go.Bar(x=loan_types, y=loan_averages, name="Mortgage Averages")])
bar_chart.update_layout(
    title='Average loan amounts per home ownership',
    yaxis=dict(
        title='Average loan amount ($)',
    ),
    xaxis=dict(
        title='Home ownership',
    )
)
bar_chart.write_image('bar_chart.png')

# Creating Table
table = go.Figure(data=[go.Table(header=dict(values=['home_ownership', 'loan_amnt']),
                 cells=dict(values=[loan_types, loan_averages]))
                     ])
table.write_image('table.png')

