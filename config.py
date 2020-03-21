import os


class DevConfig(object):
  DEV = True
  CACHE_TYPE = 'simple'
  HOSTNAME = 'http://localhost'
  ROOT_URL = 'http://localhost:5000'
  MEMCACHIER_SERVERS = ['127.0.0.1']

class ProductionConfig(object):
  DEV = False
  HOSTNAME = 'https://israeli-whist.herokuapp.com/'
  ROOT_URL = 'https://israeli-whist.herokuapp.com/'
  CACHE_TYPE = 'saslmemcached'
  MEMCACHIER_SERVERS = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
  MEMCACHIER_USERNAME = os.environ.get('MEMCACHIER_USERNAME')
  MEMCACHIER_PASSWORD = os.environ.get('MEMCACHIER_PASSWORD')

if os.environ.get('PRODUCTION'):
  Config = ProductionConfig
else:
  Config = DevConfig