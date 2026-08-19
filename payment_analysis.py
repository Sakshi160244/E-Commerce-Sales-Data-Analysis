import pandas as pd
import numpy as np

def perform_payment_analysis(mydb):

    print("\n========== PAYMENT ANALYSIS ==========")

    query = """
    SELECT
        payment_method,
        COUNT(*) AS total_payments
    FROM payments
    GROUP BY payment_method
    ORDER BY total_payments DESC
    """

    payment_df = pd.read_sql(query, mydb)

    print("\nPayment Method Distribution:")
    print(payment_df)

    return payment_df



