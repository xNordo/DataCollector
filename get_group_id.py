from telethon import TelegramClient

print('''
Ten program zbierze wszystkie nazwy i id grup i konwersacji do jakiś należysz.
By tego dokonać będzie potrzebne api_id oraz api_hash, by je uzyskać wykonaj poniższe kroki: 
1. Zaloguj się do swojego konta Telegram pod tym linkiem: https://my.telegram.org/auth.
2. Kliknij API Development tools.
3. Wypełnij dwa pierwsze pola frazą „MessageCollector”.
4. Naciśnij Create application. Po przeładowaniu strony powinno pojawić się okno z App api_id oraz App api_hash. 
Pamiętaj żeby trzymać api_hash w sekrecie.  
''')


api_id = int(input('API ID: '))
api_hash = input('API HASH: ')

client = TelegramClient("anon", api_id, api_hash)

with open("groups_id.txt", "w+") as f:
    async def main():

        async for dialog in client.iter_dialogs():
            f.write(dialog.name + ' has ID ' + str(dialog.id) + "\n")

with client:
    client.loop.run_until_complete(main())