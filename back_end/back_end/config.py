# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# base configuration
class Config:
    HOSTNAME = "127.0.0.1"
    PORT = 3306
    USERNAME = "root"
    PASSWORD = "123456"
    DATABASE = "bishe"
    DATABASE_DRIVER = "pymysql"

    # SECRET_KEY = os.environ.get('KEY') or '123456'

    # 数据库规则
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql+{Config.DATABASE_DRIVER}://{Config.USERNAME}:{Config.PASSWORD}@{Config.HOSTNAME}:{Config.PORT}/{Config.DATABASE}?charset=utf8mb4"

# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/test-database'

# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/product-database'

# config dict
# 生成一个字典，用来根据字符串找到对应的配置类
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

