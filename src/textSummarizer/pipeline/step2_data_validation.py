from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.chech_status_file()
        