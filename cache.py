import config
import pylibmc

behaviors = {
  # Faster IO
  'tcp_nodelay': True,
  # Keep connection alive
  'tcp_keepalive': True,
  # Timeout for set/get requests
  'connect_timeout': 2000, # ms
  'send_timeout': 750 * 1000, # us
  'receive_timeout': 750 * 1000, # us
  '_poll_timeout': 2000, # ms
  # Better failover
  'ketama': True,
  'remove_failed': 1,
  'retry_timeout': 2,
  'dead_timeout': 30
}

if config.Config.DEV:
  mc = pylibmc.Client(
    config.Config.MEMCACHIER_SERVERS,
    binary=True)
else:
  mc = pylibmc.Client(
    config.Config.MEMCACHIER_SERVERS,
    binary=True,
    username=config.Config.MEMCACHIER_USERNAME,
    password=config.Config.MEMCACHIER_PASSWORD,
    behaviors=behaviors)
