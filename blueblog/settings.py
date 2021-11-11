# 使用类组织开发、测试、生产上线等不同环境的配置

import os

# 获取绝对路径，用于文件绝对路径的拼接
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Blueblog Admin', MAIL_USERNAME)

    BLUEBLOG_EMAIL = os.getenv('BLUEBLOG_EMAIL')
    BLUEBLOG_POST_PER_PAGE = 10
    BLUEBLOG_MANAGE_POST_PER_PAGE = 15
    BLUEBLOG_COMMENT_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.db'))

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}