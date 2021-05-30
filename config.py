class Config:
    SECRET_KEY='eyJuYW1lIjoiTUNTIiwiYWxpYXMiOjUwMH0'
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='admin'
    MYSQL_PASSWORD='123456'
    MYSQL_DB='tienda'

config={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}