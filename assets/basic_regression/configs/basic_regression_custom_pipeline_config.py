basic_regression_config = {
    "pipelines_configs": [{
        "data_settings": {
            "local_file_path": "data/diabetes.csv",  # data source
            "variable_to_predict": "target",  # column name of variable to predict
            # features handling configurations
            "data_handling": {
                "features_for_train": [],  # leave empty for selecting all features
                "set_features_index": [],  # leave empty for indexing by row index
                # features to remove
                "features_to_remove": ["sex"],
                "feature_remove_by_null_percentage": 0.3
            }
        },
        # task settings
        "job_settings": {
            "asset_name": "basic_regression",
            "pipeline": ['load_train_data', 'clean_train_data', 'cache_features']
        }
    }]
}
