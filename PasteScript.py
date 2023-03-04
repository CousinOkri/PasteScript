from googlesearch import search
import pyfiglet

print(pyfiglet.figlet_format("-------------"))
print(pyfiglet.figlet_format("PasteScript", font="bulbhead"))
print(pyfiglet.figlet_format("-------------"))

paste_sites = ["pastebin.com", "pastie.org","paste.bingner.com", "justepaste.it", "paste4btc.com"]
domain = input(" Enter a domain:\n")
for psite in paste_sites:
    for i in search('site:{} "{}"'.format(psite, domain)):
        print(i)
