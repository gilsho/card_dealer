import config
import bmemcached

mc = bmemcached.Client(
  config.Config.MEMCACHIER_SERVERS,
  config.Config.MEMCACHIER_USERNAME,
  config.Config.MEMCACHIER_PASSWORD)

# if config.Config.DEV:
#   mc = pylibmc.Client(
#     config.Config.MEMCACHIER_SERVERS,
#     binary=True)
# else:
#   mc = pylibmc.Client(
#     config.Config.MEMCACHIER_SERVERS,
#     binary=True,
#     username=config.Config.MEMCACHIER_USERNAME,
#     password=config.Config.MEMCACHIER_PASSWORD,
#     behaviors=behaviors)
