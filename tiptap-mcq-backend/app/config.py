class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/test_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
MCQ_DATA_DUMP_FILE = "mcq_data.json"