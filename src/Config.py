from pathlib import Path

import yaml
from yaml.parser import ParserError

from Exceptions import InvalidCredentialException
from Exceptions.InvalidCredentialException import InvalidCredentialsException


class Config:

    def __init__(self, configPath: str) -> None:
        """
        加载配置文件到Config类型对象中
        :param configPath:
        """
        self.accounts = {}
        try:
            configPath = self.__findConfig(configPath)
            with open(configPath, 'r',encoding='utf-8') as f:
                config = yaml.safe_load(f)
                accs = config.get("accounts")
                for account in accs:
                    if "username" != accs[account]["username"]:
                        self.accounts[account] = {
                            "username": accs[account]["username"],
                            "password": accs[account]["password"],
                        }
                if not self.accounts:
                    raise InvalidCredentialException
        except FileNotFoundError as ex:
            print(f"[red]CRITICAL ERROR: The configuration file cannot be found at {configPath}\nHave you extacted the ZIP archive and edited the configuration file?")
            raise ex
        except InvalidCredentialsException as ex:
            print(f"[red]CRITICAL ERROR: There are only default credentials in the configuration file.\nYou need to add you Riot account login to config.yaml to receive drops.")
            print("Press any key to exit...")
            input()
            raise ex
        except Exception as ex:
            print(f"[red]CRITICAL ERROR: 有些错误你看着办")
            input()
            raise ex


    def getAccount(self, account: str) -> dict:
        return self.accounts[account]


    def __findConfig(self,configPath):
        """
        查找配置文件是否在其他路径
        :param cofigPath:
        :return:
        """
        configPath = Path(configPath)
        if configPath.exists():
            return configPath
        if Path("config/config.yaml").exists():
            return Path("config/config.yaml")
        if Path("config/config.yaml").exists():
            return Path("config/config.yaml")
        return configPath