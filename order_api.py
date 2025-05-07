import requests

def fetch_customer_orders(customer_id):
    """
    Fetches order information for a given customer ID using the FastAPI backend.

    This function makes an HTTP GET request to the local FastAPI server's endpoint
    at `/data/customer/{customer_id}` to retrieve order records.

    Args:
        customer_id (int): The ID of the customer whose order history is being requested.

    Returns:
        dict or str: JSON response containing order data if successful,
                     or an error message string if the request fails.
    
    Example:
        >>> fetch_customer_orders(37077)
        [{'Order_Date': '2018-01-02', 'Product': 'Car Media Players', ...}]
    """
    try:
        response = requests.get(f"http://localhost:8000/data/customer/{customer_id}")
        return response.json()
    except Exception as e:
        return f"Error fetching orders: {e}"
