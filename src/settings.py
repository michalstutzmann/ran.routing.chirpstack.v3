from lib.environs import Env

env = Env()
env.read_env()


LOG_LEVEL = env("LOG_LEVEL", "info")
LOG_COLORS = env.bool("LOG_COLORS", True)

CHIRPSTACK_API_TOKEN = env("CHIRPSTACK_API_TOKEN")
CHIRPSTACK_API_GRPC_HOST = env("CHIRPSTACK_API_GRPC_HOST")
CHIRPSTACK_API_GRPC_PORT = env.int("CHIRPSTACK_API_GRPC_PORT", 433)
CHIRPSTACK_API_GRPC_SECURE = env.bool("CHIRPSTACK_API_GRPC_SECURE", False)
CHIRPSTACK_API_GRPC_CERT_PATH = env("CHIRPSTACK_API_GRPC_CERT_PATH", None)

CHIRPSTACK_MQTT_SERVER_URI = env("CHIRPSTACK_MQTT_SERVER_URI")

CHIRPSTACK_MATCH_TAGS = env("CHIRPSTACK_MATCH_TAGS", "everynet=true")
CHIRPSTACK_GATEWAY_ID = env("CHIRPSTACK_GATEWAY_ID", "000000000000c0de")
CHIRPSTACK_DEVICES_REFRESH_PERIOD = env.int("CHIRPSTACK_DEVICES_REFRESH_PERIOD", 60 * 5)
CHIRPSTACK_ORGANIZATION_ID = env.int("CHIRPSTACK_ORGANIZATION_ID", 0)

RAN_TOKEN = env("RAN_TOKEN")
RAN_API_URL = env("RAN_API_URL")


HEALTHCHECK_SERVER_HOST = env("HEALTHCHECK_SERVER_HOST", "0.0.0.0")
HEALTHCHECK_SERVER_PORT = env.int("HEALTHCHECK_SERVER_PORT", 9090)
