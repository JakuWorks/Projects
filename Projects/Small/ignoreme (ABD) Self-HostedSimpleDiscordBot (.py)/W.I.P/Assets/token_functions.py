"""
This module was written to provide two functions: save_token and get_token. It applies \
basic encryption and decryption to the TOKEN.
"""

from platform import node

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from getmac import get_mac_address
from cpuinfo import get_cpu_info
from helper_functions import predictable_shuffle_string, b64encode_utf8, \
    my_b64decode
from Assets.project_config_shadow import config, ConfigPath, config_main, \
    salt_base64encoded_utf8, \
    token_ciphered_base64encoded_utf8, n_token_ciphered_base64encoded_utf8, \
    token_cipher_iv_base64encoded_utf8, n_token_cipher_iv_base64encoded_utf8


def get_salt_bytes() -> bytes:
    """
    :return: The salt from config.ini decoded with Base64 into bytes.
    """

    return my_b64decode(salt_base64encoded_utf8)


def generate_encryption_password() -> bytes:
    """
    This function generates an encryption password based on the user's PC components.
    :return: The encryption password of the token in bytes.
    """

    secret_string1: str = r'LDg52tmeNQ59*%F957dEpT#6!mk$'
    secret_string2: str = r'Q6DtyVJ45je!NVJ*3^%&^E4uFF5Kqd7%4'
    secret_string3: str = r'NxaQVw8vu9uU9cz5WEn#jdNznk7!pPC4'

    cpu_info: dict = get_cpu_info()

    cpu_brand: str = cpu_info['brand_raw']
    cpu_model: str = str(cpu_info['model'])
    system_hostname: str = node()
    mac_info: str = get_mac_address()

    # epf - Encryption Password Foundation
    # s - Step

    epf_s1: str = secret_string1.join([cpu_brand, cpu_model])
    epf_s2: str = secret_string2.join([epf_s1, system_hostname])
    epf_s3: str = secret_string3.join([epf_s2, mac_info])
    epf_s4: str = predictable_shuffle_string(epf_s3)
    encryption_password: bytes = PBKDF2(epf_s4, dkLen=32, salt=get_salt_bytes())

    return encryption_password


def get_cipher(cipher_iv: bytes = None):
    """

    :param cipher_iv: If this argument is present (isn't None, False, etc.) the the \
    AES.new() function will be provided an IV.
    :return: The cipher for encrypting and decrypting.
    """

    if cipher_iv:
        return AES.new(generate_encryption_password(), AES.MODE_CBC, iv=cipher_iv)

    return AES.new(generate_encryption_password(), AES.MODE_CBC)


def try_get_saved_token() -> str or None:
    """
    :return: The unencrypted token as a string or None
    """

    cipher_iv: bytes = my_b64decode(token_cipher_iv_base64encoded_utf8)
    cipher_data: bytes = my_b64decode(token_ciphered_base64encoded_utf8)

    cipher = get_cipher(cipher_iv)

    if not cipher_iv or not cipher_data:
        return ''

    return unpad(cipher.decrypt(cipher_data), AES.block_size)


def save_token(token: str) -> None:
    """
    This is a simple encryption with no user input. It was written to keep out an \
    average Joe from accessing the TOKEN.
    :param token: This is the token to encrypt.
    :return: The first object of the return tuple is the IV of the encryption cipher, \
    and the second return is the actual ciphered data.
    """

    cipher = get_cipher()
    ciphered_data = cipher.encrypt(pad(token.encode('utf-8'), AES.block_size))

    config_main[n_token_cipher_iv_base64encoded_utf8] = \
        b64encode_utf8(cipher.IV)
    config_main[n_token_ciphered_base64encoded_utf8] = \
        b64encode_utf8(ciphered_data)

    with open(ConfigPath, 'w', encoding='utf-8') as file:
        config.write(file)
