"""
example_usage.py -- Demonstrates CheckoutFraudDetectorClient
"""
from client import CheckoutFraudDetectorClient

def main():
    client = CheckoutFraudDetectorClient()
    result = client.audit_transaction(
        shipping_country="US",
        billing_country="CA",
        ip_country="US",
        order_amount_usd=1250.00
    )
    print("[Fraud Prevention Audit]")
    print(f"Risk Score: {result['fraud_score']}")
    print(f"Decision Status: {result['status'].upper()}")
    print(f"Flags: {result['reasons']}")

if __name__ == "__main__":
    main()
