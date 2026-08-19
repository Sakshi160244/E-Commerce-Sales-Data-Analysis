from database import create_connection
from data_loading import load_data
from data_cleaning import clean_data
from eda import perform_eda
from numpy_analysis import perform_numpy_analysis
from customer_analysis import *
from product_analysis import *
from order_analysis import *
from payment_analysis import perform_payment_analysis
from kpi_analysis import perform_kpi_analysis
from visualization import *
from business_insights import generate_business_insights


# ==========================================
# MAIN PROGRAM
# ==========================================

# 1. Database Connection
mydb = create_connection()

# 2. Load Data
df = load_data(mydb)

# 3. Data Cleaning
df, delivered_df = clean_data(df)

# ==========================================
# MENU
# ==========================================

print("\n==========================================")
print("       E-COMMERCE SALES ANALYSIS")
print("==========================================")
while True:
    print("1. EDA")
    print("2. NumPy Analysis")
    print("3. Customer Analysis")
    print("4. Product Analysis")
    print("5. Order Analysis")
    print("6. Payment Analysis")
    print("7. KPI Analysis")
    print("8. Visualizations")
    print("9. Business Insights")
    print("0. Exit")

    choice = input("\nEnter your choice: ")
    # print(type(choice))
    # 1. EDA
    if choice == "1":
        perform_eda(df)

    # 2. NumPy Analysis
    elif choice=="2":
        perform_numpy_analysis(delivered_df)

    # 3. Customer Analysis
    elif choice =="3":
        (customer_spending_df, customer_order_count, top_customer, repeat_customers, repeat_customer_rate, average_orders_per_customer) =perform_customer_analysis(delivered_df)
        (gender_revenue, gender_avg_spending) = gender_analysis(delivered_df)
        (age_revenue, age_avg_spending) = age_analysis(delivered_df)
        state_revenue = state_analysis(delivered_df)

    # 4. Product Analysis
    elif choice =="4":
        (category_performance, top_category, top_product, top_revenue_product, top_products_quantity) = perform_product_analysis(delivered_df)

    # 5. Order Analysis
    elif choice== "5":
        status_revenue = perform_order_analysis(df)
        (average_discount, maximum_discount, minimum_discount, discount_correlation) = discount_analysis(delivered_df)

    # 6. Payment Analysis
    elif choice =="6":
        payment_df = perform_payment_analysis(mydb)


    # 7. KPI Analysis
    elif choice == "7":
        kpis = perform_kpi_analysis(df, delivered_df)

    # 8. Visualizations
    elif choice == "8":
        while True:

            print("\n==========================================")
            print("          VISUALIZATION MENU")
            print("==========================================")

            print("1. Monthly Revenue Chart")
            print("2. Category Revenue Chart")
            print("3. Category Quantity Chart")
            print("4. Top Products Chart")
            print("5. Payment Method Chart")
            print("6. Top Customers Chart")
            print("7. Order Status Chart")
            print("8. Customer Segment Chart")
            print("9. Gender Revenue Chart")
            print("10. Gender Average Spending Chart")
            print("11. Age Revenue Chart")
            print("12. Age Average Spending Chart")
            print("13. State Revenue Chart")
            print("14. Discount Revenue Chart")
            print("0. Back to Main Menu")

            chart_choice = input("\nEnter your chart choice: ")

            if chart_choice == "1":

                monthly_revenue_chart(delivered_df)
            elif chart_choice == "2":
                category_revenue_chart(category_performance)
            elif chart_choice == "3":
                category_quantity_chart(category_performance)
            elif chart_choice == "4":
                top_products_chart(top_products_quantity)
            elif chart_choice =="5":
                payment_method_chart(payment_df)
            elif chart_choice == "6":
                top_customers_chart(customer_spending_df)
            elif chart_choice == "7":
                order_status_chart(df)
            elif chart_choice == "8":
                customer_segment_chart(customer_spending_df)
            elif chart_choice == "9":
                gender_revenue_chart(gender_revenue)
            elif chart_choice == "10":
                gender_avg_spending_chart(gender_avg_spending)
            elif chart_choice == "11":
                age_revenue_chart(age_revenue)
            elif chart_choice == "12":
                age_avg_spending_chart(age_avg_spending)
            elif chart_choice == "13":
                state_revenue_chart(state_revenue)
            elif chart_choice == "14":
                discount_revenue_chart(delivered_df)
            elif chart_choice == "0":

                break
            else:

                print("Invalid chart choice!")


    # 9. Final Business Insights
    elif choice == "9":
        (customer_spending_df,customer_order_count,top_customer,repeat_customers,repeat_customer_rate,average_orders_per_customer) = perform_customer_analysis(delivered_df)

        (category_performance,top_category,top_product, top_revenue_product, top_products_quantity) = perform_product_analysis(delivered_df)

        kpis = perform_kpi_analysis(df, delivered_df)

        generate_business_insights(delivered_df, kpis, top_category, top_product, top_revenue_product, top_customer, repeat_customers,repeat_customer_rate) # type: ignore

    # ==========================================
    # 0. EXIT
    # ==========================================

    elif choice == "0":
        print("Program exited.")
        break

    # ==========================================
    # INVALID CHOICE
    # ==========================================

    else:

        print("Invalid choice!")