def transform_data(data):
    """Simulate data transformation."""
    transformed_data = data.upper()  
    return transformed_data

if __name__ == "__main__":
    sample_data = "example data"
    transformed = transform_data(sample_data)
    print("Transformed Data:", transformed)
