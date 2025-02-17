from textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from textSummarizer.utils.common import read_yaml, create_dirs
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
class ConfigurationManager:
    def __init__(
            self, 
            config_file_path = CONFIG_FILE_PATH,
            params_file_path =  PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_dirs([self.config.artifacts_root])

    def data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_dirs([config.root_dir])
        
        return DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
    def get_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_dirs([config.root_dir])

        return DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_dirs([config.root_dir])

        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )