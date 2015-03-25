# coding=utf-8
import os
from dojnekravy_cz.deployment.remote_version import RemoteVersion


def get_current_remote_environment():
    # Aplikace je spuštěna z Apache, tzn. přes ENV_VAR máme informaci, zda je aktivní VirtualHost "dev_" nebo "www_"
    # Pokud informaci o prostředí nemáme, tj. v proměnné je výchozí hodnota, předpokládám, že jsme v konzoli
    current_apache_environment = os.getenv('APPLICATION_ENV', None)

    # Na produkčním serveru se s konzolí pracuje:
    # $ remote_version='production' python ./manage.py......
    current_shell_environment = os.getenv('remote_version', None)

    current_apache_environment = _normalize_if_string(current_apache_environment)
    current_shell_environment = _normalize_if_string(current_shell_environment)

    if current_apache_environment == RemoteVersion.PRODUCTION or current_shell_environment == RemoteVersion.PRODUCTION:
        return RemoteVersion.PRODUCTION
    elif current_apache_environment == RemoteVersion.DEV or current_shell_environment == RemoteVersion.DEV:
        return RemoteVersion.DEV
    else:
        raise Exception('No environ variable to determine, which database use!')


def _normalize_if_string(string_to_normalize):
    if isinstance(string_to_normalize, str) or isinstance(string_to_normalize, unicode):
        return string_to_normalize.lower()
    else:
        return string_to_normalize