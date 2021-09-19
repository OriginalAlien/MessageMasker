# MessageMasker
This exploit gives you the ability to mask messages (hide messages inside other messages)


## Examples
If the information isnt specified via the command line - you will be asked it via inputs

---

**Spoofed URL**
```
$ py example.py <token> <channel id> https://discord.com https://pornhub.com
```
![](https://i.snipboard.io/QwDk03.jpg)


**Masked mention**
```
$ py example.py <token> <channel id> "Hello there!" @everyone
```
![](https://i.snipboard.io/PT6QNe.jpg)


**Spoofed vanity URL**
```
$ py example.py <token> <channel id> discord.gg/checksum discord.gg/YOURSERVER
```
![](https://i.snipboard.io/5tUnQu.jpg)


## Options

Requires your discord token and automatically sends the message using discords API
```
SELFBOT = False
```
Specifies that you will not be using command line arguments in the program and doesnt give you a usage warning.
```
CONSOLE = True
```
