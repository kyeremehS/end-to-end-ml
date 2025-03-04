import os
import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """Validates whether all columns in the dataset match the expected schema."""
        try:
            # Ensure the file path is correctly set
            data = pd.read_csv(self.config.unzip_data_dir)
            # Read the CSV file
    

            # Extract actual and expected columns
            actual_cols = set(data.columns)
            expected_cols = set(self.config.all_schema.keys())

            # Compare columns
            validation_status = actual_cols == expected_cols

            # Log missing or extra columns
            missing_cols = expected_cols - actual_cols
            extra_cols = actual_cols - expected_cols

            if not validation_status:
                print("❌ Column validation failed!")
                print(f"Missing columns: {missing_cols}")
                print(f"Unexpected columns: {extra_cols}")
            else:
                print("✅ All columns match!")

            # Save validation status to a file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}\n")
                f.write(f"Missing columns: {missing_cols}\n")
                f.write(f"Unexpected columns: {extra_cols}\n")

            return validation_status

        except Exception as e:
            raise Exception(f"Error during validation: {str(e)}")
