from main import snowflake_transform

if __name__ == "__main__":
    snowflake_transform.serve(
        name="snowflake-transform-production",
        tags=["lineage"],
    )
