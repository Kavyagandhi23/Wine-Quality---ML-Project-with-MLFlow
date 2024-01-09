from MLProject import logger
from src.MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} comleted <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

