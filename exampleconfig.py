from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 13949344
    API_HASH = "408723003ad67fa8ab01ccc7f53e24ad"
    # the name to display in your alive message
    ALIVE_NAME = "amirbechf"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://kkezimkw:g_llgfOwlK8OMrkmFDGC1hXLo3gz7ljP@peanut.db.elephantsql.com/kkezimkw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBu7ijv83rO53NSQbubowuYwYpKyOtfFah_v2fjvBj4c5q9maq5vU4jY6Btao0g021ju6VSpvOmvK7gGXSZ5R2zSvb_Y5DoB-tIflPZXjOZgypvVahe63hnDx_xjQGHLHlFVPFgDAojhCKdTz1UfbSnnXZmBzpoOwfAWNebyM6BTWvdLQYRFsOzbMtcBjdZzU1mgWNljbKOuJukYq17v7Ealv_RfP6spuvkgOO0mHvWzOcsrg4OMQ6EYGwg26p03HYPw1x-aSFQ05uhW6kwuPsdehPOMuQoziGh_qtXdQZ48WYbeJUT0sIF-bJIsHlMClEgW4iXdB98WfPut2OYUs68nk="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6443503095:AAHn0ZoH0NWbASVUqchZA5VA-KHf1G7wKi0"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001826716869
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
