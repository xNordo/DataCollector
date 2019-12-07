MessageCollector is a software that works with Telegram.
It allows you to collect messages from multiple groups (without adding bot to them) and resend them as a bot to another group.

SETUP
1. Create a bot by messageing to BotFather on Telegram.
2. Add bot to group where you want it to resend messages.
3. In order to collect messages you'll need api_id and api_hash.
    3.1 Sign up for Telegram if you don't have account already
    3.2 Log in to your Telegram core: https://my.telegram.org.
    3.3 Go to ‘API development tools’ and fill out the form.
    3.4 You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.
    3.5 Remember to keep your api_hash in secret.
4. Use get_group_id.py to get all IDs from your contact book.
5. Run main.py
6. Fill everything as instructions on screen tells you to.
7. Congratulations everything is set! Your MessageCollector is waiting for first messages.
