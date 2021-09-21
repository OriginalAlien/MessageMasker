from colorama import Fore, init
import re
import pyperclip
import sys
import requests
import warnings

init()

CONSOLE = True
SELFBOT = False


def generate(before_text, after_text):
    if len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', before_text)) == 1:
        before_text = "<" + before_text + ">"
    after_text = before_text + " " + ('||\u200b||' * 200) + " " + after_text
    return after_text


def execute(text, c_id, auth):
    return requests.post(f'https://discordapp.com/api/v6/channels/{c_id}/texts',
                         headers={'Authorization': auth},
                         json={'content': text})


if not CONSOLE and len(sys.argv) < 5:
    warnings.warn(f'Usage: py {sys.argv[0]} <token> <channel id> <message> <masked message>\n')
if len(sys.argv) < 5:
    original_text = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.GREEN} Enter the original text{Fore.RED} > ")
    fake_text = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.GREEN} Enter the text to be hidden{Fore.RED} > ")
    if not SELFBOT:
        after = generate(original_text, fake_text)
        pyperclip.copy(after)
        print(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN} Text copied to clipboard{Fore.RED}")
    else:
        token = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.GREEN} Enter your discord token{Fore.RED} > ")
        channel_id = input(
            f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.GREEN} Enter the channel ID to send the message to{Fore.RED} > ")
        execute(generate(original_text, fake_text), channel_id, token)
else:
    token = sys.argv[1]
    channel_id = sys.argv[2]
    message = sys.argv[3]
    hidden_message = sys.argv[4]
    execute(generate(message, hidden_message), channel_id, token)
