from typing import Dict

def create_table_resource(platform: str, table_name: str, description: str) -> Dict[str, str]:
    return {
        "prefect.resource.id": f"{platform}://analytics/marts/{table_name}",
        "prefect.resource.name": description,
        "prefect.resource.role": "table"
    }

# Raw Tables (Source Layer)
raw_customers = create_table_resource("dbt", "raw_customers", "Raw Customer Data")
raw_orders = create_table_resource("dbt", "raw_orders", "Raw Order Data")
raw_products = create_table_resource("dbt", "raw_products", "Raw Product Data")
raw_inventory = create_table_resource("dbt", "raw_inventory", "Raw Inventory Data")
raw_shipping = create_table_resource("dbt", "raw_shipping", "Raw Shipping Data")
raw_payments = create_table_resource("dbt", "raw_payments", "Raw Payment Data")

# Staging Tables
stg_customers = create_table_resource("dbt", "stg_customers", "Staged Customer Data")
stg_orders = create_table_resource("dbt", "stg_orders", "Staged Order Data")
stg_products = create_table_resource("dbt", "stg_products", "Staged Product Data")
stg_inventory = create_table_resource("dbt", "stg_inventory", "Staged Inventory Data")
stg_shipping = create_table_resource("dbt", "stg_shipping", "Staged Shipping Data")
stg_payments = create_table_resource("dbt", "stg_payments", "Staged Payment Data")

# Integration Tables
int_customer_orders = create_table_resource("dbt", "int_customer_orders", "Integrated Customer Orders")
int_order_items = create_table_resource("dbt", "int_order_items", "Integrated Order Items")
int_inventory_status = create_table_resource("dbt", "int_inventory_status", "Integrated Inventory Status")
int_shipping_status = create_table_resource("dbt", "int_shipping_status", "Integrated Shipping Status")
int_payment_status = create_table_resource("dbt", "int_payment_status", "Integrated Payment Status")

# Mart Tables - Customer Domain
fct_customer_orders = create_table_resource("dbt", "fct_customer_orders", "Customer Order Facts")
dim_customers = create_table_resource("dbt", "dim_customers", "Customer Dimension")
fct_customer_lifetime_value = create_table_resource("dbt", "fct_customer_ltv", "Customer Lifetime Value")
rpt_customer_cohorts = create_table_resource("dbt", "rpt_customer_cohorts", "Customer Cohort Analysis")

# Mart Tables - Product Domain
fct_product_sales = create_table_resource("dbt", "fct_product_sales", "Product Sales Facts")
dim_products = create_table_resource("dbt", "dim_products", "Product Dimension")
fct_product_inventory = create_table_resource("dbt", "fct_product_inventory", "Product Inventory Facts")
rpt_product_performance = create_table_resource("dbt", "rpt_product_performance", "Product Performance Analysis")

# Mart Tables - Order Domain
fct_orders = create_table_resource("dbt", "fct_orders", "Order Facts")
dim_order_status = create_table_resource("dbt", "dim_order_status", "Order Status Dimension")
fct_order_payments = create_table_resource("dbt", "fct_order_payments", "Order Payment Facts")
rpt_order_summary = create_table_resource("dbt", "rpt_order_summary", "Order Summary Analysis")

# Mart Tables - Shipping Domain
fct_shipments = create_table_resource("dbt", "fct_shipments", "Shipment Facts")
dim_shipping_methods = create_table_resource("dbt", "dim_shipping_methods", "Shipping Methods Dimension")
rpt_shipping_performance = create_table_resource("dbt", "rpt_shipping_performance", "Shipping Performance Analysis")

# Analytics Tables
analytics_customer_360 = create_table_resource("dbt", "analytics_customer_360", "Customer 360 View")
analytics_product_insights = create_table_resource("dbt", "analytics_product_insights", "Product Insights")
analytics_order_metrics = create_table_resource("dbt", "analytics_order_metrics", "Order Metrics")
analytics_shipping_metrics = create_table_resource("dbt", "analytics_shipping_metrics", "Shipping Metrics")

# Additional Data Sources
ext_web_analytics = create_table_resource("google_analytics", "web_behavior", "Website User Behavior")
ext_mobile_analytics = create_table_resource("firebase", "mobile_events", "Mobile App Analytics")
ext_social_media = create_table_resource("social", "engagement_metrics", "Social Media Engagement")
ext_email_campaigns = create_table_resource("sendgrid", "email_metrics", "Email Campaign Performance")
ext_customer_support = create_table_resource("zendesk", "support_tickets", "Customer Support Data")
ext_product_reviews = create_table_resource("reviews", "customer_feedback", "Product Reviews")
ext_inventory_forecast = create_table_resource("forecast", "inventory_predictions", "Inventory Forecasting")
ext_market_data = create_table_resource("market", "competitor_analysis", "Market Competition Data")
ext_pricing_analytics = create_table_resource("pricing", "price_elasticity", "Price Elasticity Analysis")
ext_ab_tests = create_table_resource("experimentation", "ab_test_results", "A/B Testing Results")
ext_user_segments = create_table_resource("segments", "user_clusters", "User Segmentation Data")
ext_churn_prediction = create_table_resource("ml", "churn_scores", "Churn Prediction Scores")
ext_recommendation = create_table_resource("ml", "product_recommendations", "Product Recommendations")
ext_fraud_detection = create_table_resource("security", "fraud_alerts", "Fraud Detection Results")
ext_logistics_data = create_table_resource("logistics", "delivery_analytics", "Logistics Analytics")
ext_supplier_metrics = create_table_resource("supply_chain", "supplier_performance", "Supplier Performance Metrics")

# Unified Data Mart
bigquery_unified_mart = create_table_resource("bigquery", "unified_data_mart", "Unified Enterprise Data Mart") 