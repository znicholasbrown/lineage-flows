from prefect import flow
from prefect._experimental.lineage import emit_external_resource_lineage
from dbt_resources import (
    # Raw Tables
    raw_customers, raw_orders, raw_products, raw_inventory,
    raw_shipping, raw_payments,
    # Staging Tables
    stg_customers, stg_orders, stg_products, stg_inventory,
    stg_shipping, stg_payments,
    # Integration Tables
    int_customer_orders, int_order_items, int_inventory_status,
    int_shipping_status, int_payment_status,
    # Customer Domain
    fct_customer_orders, dim_customers, fct_customer_lifetime_value,
    rpt_customer_cohorts,
    # Product Domain
    fct_product_sales, dim_products, fct_product_inventory,
    rpt_product_performance,
    # Order Domain
    fct_orders, dim_order_status, fct_order_payments,
    rpt_order_summary,
    # Shipping Domain
    fct_shipments, dim_shipping_methods, rpt_shipping_performance,
    # Analytics
    analytics_customer_360, analytics_product_insights,
    analytics_order_metrics, analytics_shipping_metrics,
    # External Data Sources
    ext_web_analytics, ext_mobile_analytics, ext_social_media,
    ext_email_campaigns, ext_customer_support, ext_product_reviews,
    ext_inventory_forecast, ext_market_data, ext_pricing_analytics,
    ext_ab_tests, ext_user_segments, ext_churn_prediction,
    ext_recommendation, ext_fraud_detection, ext_logistics_data,
    ext_supplier_metrics,
    # Unified Data Mart
    bigquery_unified_mart
)

@flow(name="staging_layer", log_prints=True)
async def staging_layer():
    """Transform raw data into staging tables"""
    # Customer staging
    await emit_external_resource_lineage(
        upstream_resources=[raw_customers],
        downstream_resources=[stg_customers]
    )
    # Order staging
    await emit_external_resource_lineage(
        upstream_resources=[raw_orders],
        downstream_resources=[stg_orders]
    )
    # Product staging
    await emit_external_resource_lineage(
        upstream_resources=[raw_products],
        downstream_resources=[stg_products]
    )
    # Inventory staging
    await emit_external_resource_lineage(
        upstream_resources=[raw_inventory],
        downstream_resources=[stg_inventory]
    )
    # Shipping staging
    await emit_external_resource_lineage(
        upstream_resources=[raw_shipping],
        downstream_resources=[stg_shipping]
    )
    # Payment staging
    await emit_external_resource_lineage(
        upstream_resources=[raw_payments],
        downstream_resources=[stg_payments]
    )

@flow(name="integration_layer", log_prints=True)
async def integration_layer():
    """Create integrated views of staged data"""
    # Customer orders integration
    await emit_external_resource_lineage(
        upstream_resources=[stg_customers, stg_orders],
        downstream_resources=[int_customer_orders]
    )
    # Order items integration
    await emit_external_resource_lineage(
        upstream_resources=[stg_orders, stg_products],
        downstream_resources=[int_order_items]
    )
    # Inventory status integration
    await emit_external_resource_lineage(
        upstream_resources=[stg_inventory, stg_products],
        downstream_resources=[int_inventory_status]
    )
    # Shipping status integration
    await emit_external_resource_lineage(
        upstream_resources=[stg_shipping, stg_orders],
        downstream_resources=[int_shipping_status]
    )
    # Payment status integration
    await emit_external_resource_lineage(
        upstream_resources=[stg_payments, stg_orders],
        downstream_resources=[int_payment_status]
    )

@flow(name="mart_customer_domain", log_prints=True)
async def mart_customer_domain():
    """Build customer domain mart tables"""
    # Customer dimension
    await emit_external_resource_lineage(
        upstream_resources=[int_customer_orders],
        downstream_resources=[dim_customers]
    )
    # Customer order facts
    await emit_external_resource_lineage(
        upstream_resources=[int_customer_orders, int_order_items],
        downstream_resources=[fct_customer_orders]
    )
    # Customer lifetime value
    await emit_external_resource_lineage(
        upstream_resources=[fct_customer_orders, dim_customers],
        downstream_resources=[fct_customer_lifetime_value]
    )
    # Customer cohorts
    await emit_external_resource_lineage(
        upstream_resources=[fct_customer_lifetime_value],
        downstream_resources=[rpt_customer_cohorts]
    )

@flow(name="mart_product_domain", log_prints=True)
async def mart_product_domain():
    """Build product domain mart tables"""
    # Product dimension
    await emit_external_resource_lineage(
        upstream_resources=[int_order_items],
        downstream_resources=[dim_products]
    )
    # Product sales facts
    await emit_external_resource_lineage(
        upstream_resources=[int_order_items, dim_products],
        downstream_resources=[fct_product_sales]
    )
    # Product inventory facts
    await emit_external_resource_lineage(
        upstream_resources=[int_inventory_status, dim_products],
        downstream_resources=[fct_product_inventory]
    )
    # Product performance
    await emit_external_resource_lineage(
        upstream_resources=[fct_product_sales, fct_product_inventory],
        downstream_resources=[rpt_product_performance]
    )

@flow(name="mart_order_domain", log_prints=True)
async def mart_order_domain():
    """Build order domain mart tables"""
    # Order status dimension
    await emit_external_resource_lineage(
        upstream_resources=[int_shipping_status, int_payment_status],
        downstream_resources=[dim_order_status]
    )
    # Order facts
    await emit_external_resource_lineage(
        upstream_resources=[int_order_items, int_customer_orders],
        downstream_resources=[fct_orders]
    )
    # Order payment facts
    await emit_external_resource_lineage(
        upstream_resources=[int_payment_status, fct_orders],
        downstream_resources=[fct_order_payments]
    )
    # Order summary
    await emit_external_resource_lineage(
        upstream_resources=[fct_orders, fct_order_payments, dim_order_status],
        downstream_resources=[rpt_order_summary]
    )

@flow(name="mart_shipping_domain", log_prints=True)
async def mart_shipping_domain():
    """Build shipping domain mart tables"""
    # Shipping methods dimension
    await emit_external_resource_lineage(
        upstream_resources=[int_shipping_status],
        downstream_resources=[dim_shipping_methods]
    )
    # Shipment facts
    await emit_external_resource_lineage(
        upstream_resources=[int_shipping_status, fct_orders],
        downstream_resources=[fct_shipments]
    )
    # Shipping performance
    await emit_external_resource_lineage(
        upstream_resources=[fct_shipments, dim_shipping_methods],
        downstream_resources=[rpt_shipping_performance]
    )

@flow(name="analytics_layer", log_prints=True)
async def analytics_layer():
    """Build final analytics tables"""
    # Customer 360
    await emit_external_resource_lineage(
        upstream_resources=[
            dim_customers, fct_customer_orders, fct_customer_lifetime_value,
            rpt_customer_cohorts
        ],
        downstream_resources=[analytics_customer_360]
    )
    # Product insights
    await emit_external_resource_lineage(
        upstream_resources=[
            dim_products, fct_product_sales, fct_product_inventory,
            rpt_product_performance
        ],
        downstream_resources=[analytics_product_insights]
    )
    # Order metrics
    await emit_external_resource_lineage(
        upstream_resources=[
            fct_orders, fct_order_payments, rpt_order_summary,
            dim_order_status
        ],
        downstream_resources=[analytics_order_metrics]
    )
    # Shipping metrics
    await emit_external_resource_lineage(
        upstream_resources=[
            fct_shipments, dim_shipping_methods, rpt_shipping_performance
        ],
        downstream_resources=[analytics_shipping_metrics]
    )

@flow(name="unified_mart_layer", log_prints=True)
async def unified_mart_layer():
    """Build the unified BigQuery data mart"""
    await emit_external_resource_lineage(
        upstream_resources=[
            # Analytics Layer
            analytics_customer_360,
            analytics_product_insights,
            analytics_order_metrics,
            analytics_shipping_metrics,
            # Key Fact Tables
            fct_customer_orders,
            fct_product_sales,
            fct_orders,
            fct_shipments,
            # Key Dimension Tables
            dim_customers,
            dim_products,
            dim_order_status,
            dim_shipping_methods,
            # External Data Sources
            ext_web_analytics,
            ext_mobile_analytics,
            ext_social_media,
            ext_email_campaigns,
            ext_customer_support,
            ext_product_reviews,
            ext_inventory_forecast,
            ext_market_data,
            ext_pricing_analytics,
            ext_ab_tests,
            ext_user_segments,
            ext_churn_prediction,
            ext_recommendation,
            ext_fraud_detection,
            ext_logistics_data,
            ext_supplier_metrics
        ],
        downstream_resources=[bigquery_unified_mart]
    )

@flow(name="dbt_pipeline")
async def dbt_pipeline():
    """Main flow that runs the entire DBT pipeline"""
    await staging_layer()
    await integration_layer()
    await mart_customer_domain()
    await mart_product_domain()
    await mart_order_domain()
    await mart_shipping_domain()
    await analytics_layer()
    await unified_mart_layer()

if __name__ == "__main__":
    from asyncio import run
    run(dbt_pipeline()) 