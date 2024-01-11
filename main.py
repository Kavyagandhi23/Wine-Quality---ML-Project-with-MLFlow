from src.MLProject import logger
from src.MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.MLProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.MLProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} comleted <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} comleted <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} comleted <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "model evaluation pipeline"
try:
    logger.info(f">>>> stage {STAGE_NAME} started<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e