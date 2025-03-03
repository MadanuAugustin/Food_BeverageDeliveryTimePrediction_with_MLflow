

import sys
from pathlib import Path
from src.deliverytime import logger, CustomException
from src.deliverytime.config.configuration import ConfigurationManager
from src.deliverytime.components.dataTransformation import DataTransformation

STAGE_NAME = 'Data_transformation_stage'


class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path('artifacts//data_validation//status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]

                # Here we are only starting the data_transformation_pipeline only if the status is true from our status.txt file

                if status == "True":

                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config = data_transformation_config)
                    data_transformation.data_split()
                    data_transformation.initiate_data_transformation()

                else:
                    raise Exception('Your data schema is not valid, please cross check...!')
                
                
        except Exception as e:
            raise CustomException(e, sys)