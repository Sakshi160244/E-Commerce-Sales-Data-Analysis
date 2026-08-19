import pandas as pd


def load_data(mydb):

    query = """
    SELECT
        o.order_id,
        o.customer_id,
        c.customer_name,
        c.gender,
        c.age,
        c.city,
        c.state,
        o.product_id,
        p.product_name,
        p.category,
        o.quantity,
        o.unit_price,
        o.discount,
        o.total_amount,
        o.order_status,
        o.order_date
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN products p
        ON o.product_id = p.product_id
    """

    df = pd.read_sql(query, mydb)

    return df