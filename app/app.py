import streamlit as st
from datetime import date
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from analysis import monthly_sales
from analysis import monthly_profit
from analysis import quarterly_sales
from analysis import quarterly_profit
from analysis import yearly_profit
from analysis import yearly_sales
from analysis import monthly_quantity
from analysis import quarterly_quantity
from analysis import yearly_quantity
from analysis import day_wise_analysis
from analysis import month_wise_analysis

df = pd.read_pickle('data/cleaned-data/cleaned.pkl')
st.title('Superstore Sales Analysis')

st.sidebar.header('Filters')
with st.sidebar:
    with st.container(border=True):
        st.text('Choose time span:')
        st.text("2014/01/03   to   2017/12/30")
        from_date = st.date_input(
            "From: ",
            value=date(2014, 1, 3)
        )
        to_date = st.date_input(
            "To: ",
            value=date(2017, 12, 30)
        )
# with st.sidebar:
#     with st.container(border=True):
#         st.text('Other Filters:')

Specific_analysis, Timely_analysis, dataframe = st.tabs(['Specific Analysis', 'Timely analysis', 'Dataset'])
with Specific_analysis:
    with st.container(border=True):
        st.subheader("Overall Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            total_revenue = df['sales'].sum()
            st.metric('Total revenue:', f'${total_revenue:,.2f}')
        with col2:
            total_profit = df['profit'].sum()
            st.metric('Total profit:', f'${total_profit:,.2f}')
        with col3:
            total_quantity = df['quantity'].sum()
            st.metric('Total quantity sold:', f'${total_quantity:,.2f}')
    with st.container(border=True):
        day, month = st.tabs(['Analysis By Day', 'Analysis By Month'])
        with day:
            st.subheader('Day-wise Analysis (Overall)')            
            st.markdown("#### Total Sales by Day of Week")
            st.plotly_chart(day_wise_analysis(df, metric="sales"), use_container_width=True)
            st.markdown("#### Total Profit by Day of Week")
            st.plotly_chart(day_wise_analysis(df, metric="profit"), use_container_width=True)

        with month:
            st.subheader('Month-wise Analysis (Overall)')
            st.markdown("#### Total Sales by Month")
            st.plotly_chart(month_wise_analysis(df, metric="sales"), use_container_width=True)
            st.markdown("#### Total Profit by Month")
            st.plotly_chart(month_wise_analysis(df, metric="profit"), use_container_width=True)
            

with Timely_analysis:
    with st.container(border=True):
        st.subheader("Overall Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            total_revenue = df['sales'].sum()
            st.metric('Total revenue:', f'${total_revenue:,.2f}')
        with col2:
            total_profit = df['profit'].sum()
            st.metric('Total profit:', f'${total_profit:,.2f}')
        with col3:
            total_quantity = df['quantity'].sum()
            st.metric('Total quantity sold:', f'${total_quantity:,.2f}')

    with st.container(border=True):
        tab4, tab5, tab6 = st.tabs(['Monthly Analysis', 'Quarterly Analysis', 'Yearly Analysis'])
        with tab4:
            st.text('*Use filter for specific duration')
            st.subheader('Monthly Sales:')
            fig = monthly_sales(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)

            st.subheader('Monthly Profit:')
            fig = monthly_profit(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)

            st.subheader('Monthly Quantity Sold:')
            fig = monthly_quantity(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)
        with tab5:
            st.text('*Use filter for specific duration')
            st.subheader('Quarterly Sales:')
            fig = quarterly_sales(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader('Quarterly Profit:')
            fig = quarterly_profit(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader('Quarterly Quantity Sold:')
            fig = quarterly_quantity(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)
        with tab6:
            st.text('*Use filter for specific duration')
            st.subheader('Yearly Sales:')
            fig = yearly_sales(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader('Yearly Profit:')
            fig = yearly_profit(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader('Yeaarlt Quantity Sold:')
            fig = yearly_quantity(df, from_date, to_date)
            st.plotly_chart(fig, use_container_width=True)

with dataframe:
    st.dataframe(df)

