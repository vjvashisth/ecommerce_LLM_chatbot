import requests

def fetch_customer_orders(customer_id):
    try:
        response = requests.get(f"http://localhost:8000/data/customer/{customer_id}")
        return response.json()
    except Exception as e:
        return f"Error fetching orders: {e}"