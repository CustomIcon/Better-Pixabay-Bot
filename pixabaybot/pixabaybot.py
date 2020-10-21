from configparser import ConfigParser
from pyrogram import Client


class pixabaybot(Client):
    def __init__(self, name):
        config_file = f"{name}.ini"
        config = ConfigParser()
        config.read(config_file)
        name = name.lower()
        plugins = dict(root=f"{name}.plugins", )
        api_id = config.get('pyrogram', 'api_id')
        api_hash = config.get('pyrogram', 'api_hash')
        token = config.get('pyrogram', 'token')
        super().__init__(
            name,
            bot_token=token,
            api_id=api_id,
            api_hash=api_hash,
            config_file=config_file,
            workers=16,
            plugins=plugins,
            workdir="./",
            app_version="pixabay-bot v1.1",
        )
    async def start(self):
        await super().start()
        print("bot started. Hi.")
    async def stop(self, *args):
        await super().stop()
        print("bot stopped. Bye.")
