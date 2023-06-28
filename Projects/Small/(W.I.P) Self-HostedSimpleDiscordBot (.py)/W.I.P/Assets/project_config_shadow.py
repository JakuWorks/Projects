"""
This module contains all values from the config, so it is easy to import them.

'f_' prefix that it is a folder in the config
'n_' prefix means name of the object in config
"""

from configparser import ConfigParser, SectionProxy


config: ConfigParser = ConfigParser()
config.read(r'.\config.ini')

n_config_main: str = 'MAIN'
config_main: SectionProxy = config[n_config_main]

n_ConfigPath: str = 'ConfigPath'
ConfigPath: str = config_main.get(n_ConfigPath)

n_AssetsFolderPath: str = 'AssetsFolder'
AssetsFolderPath: str = config_main.get(n_AssetsFolderPath)

n_BotScriptPath: str = 'BotScriptPath'
BotScriptPath: str = config_main.get(n_BotScriptPath)

n_first_bad_answer_wait_seconds: str = 'first_bad_answer_wait_seconds'
first_bad_answer_wait_seconds: str = config_main.get(n_first_bad_answer_wait_seconds)

n_ClearTokenIfBad: str = 'ClearTokenIfBad'
ClearTokenIfBad: bool = bool(int(config_main.get(n_ClearTokenIfBad)))

n_token_encrypted: str = 'token_encrypted'
token_encrypted: str = config_main.get(n_token_encrypted)

n_salt_base64encoded_utf8: str = 'salt_base64encoded_utf8'
salt_base64encoded_utf8: str = config_main.get(n_salt_base64encoded_utf8)

n_token_cipher_iv_base64encoded_utf8: \
    str = 'token_cipher_iv_base64encoded_utf8'
token_cipher_iv_base64encoded_utf8: \
    str = config_main.get(n_token_cipher_iv_base64encoded_utf8)

n_token_ciphered_base64encoded_utf8: \
    str = 'token_ciphered_base64encoded_utf8'
token_ciphered_base64encoded_utf8: \
    str = config_main.get(n_token_ciphered_base64encoded_utf8)
