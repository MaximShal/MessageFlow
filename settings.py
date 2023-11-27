from environs import Env


env = Env()
env.read_env()

TELEGRAM_API_TOKEN = env.str('MF_TELEGRAM_API_TOKEN')
EXTERNAL_API_URL = env.str('EXTERNAL_API_URL')

AMQP_CREDENTIALS = {
    'host': env.str('AMQP_ADDRESS'),
    'port': env.int('AMQP_PORT'),
    'login': env.str('AMQP_USER'),
    'password': env.str('AMQP_PASSWORD'),
    'virtualhost': env.str('AMQP_VHOST')
}
AMQP_QUEUE_NAME = env.str('AMQP_QUEUE_NAME')
