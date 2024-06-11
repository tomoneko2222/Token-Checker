import os
from requests import get, post
from random import randint
from colorama import Fore, Style, init
import shutil
import requests

# coloramaを初期化
init()

# バナーを中央に表示する関数
def print_banner(banner):
    # 現在のターミナルのサイズを取得
    columns, rows = shutil.get_terminal_size()
    for line in banner.split('\n'):
        # バナーの各行を中央に配置
        print(line.center(columns))

# バナーのテキスト
banner_text = """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗            
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║            
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║            
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║            
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║            
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝            
                                                        
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

# バナーを緑色で表示
print(Fore.GREEN + Style.BRIGHT)
print_banner(banner_text)
print(Style.RESET_ALL)

def validate_token(token: str) -> bool:
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers={'Authorization': token})
        return r.status_code == 200
    except requests.RequestException as e:
        return False

if __name__ == "__main__":
    try:
        checked = []
        # tokens.txtファイルが存在しない場合、新規作成します
        if not os.path.exists('tokens.txt'):
            with open('tokens.txt', 'w') as f:
                pass
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and validate_token(token):
                    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} Token: {token} is Valid')
                    checked.append(token)
                else:
                    print(f'{Fore.RED}[-]{Style.RESET_ALL} Token: {token} is Invalid')
        if len(checked) > 0:
            save = input(f'{len(checked)} valid tokens\nSave valid tokens. (y/n)').lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'Tokens Save To {name}.txt File!')
        input('Press Enter For Exit...')
    except:
        input('Can`t Open "tokens.txt" File!')
