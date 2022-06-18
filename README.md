Discrod bot sample code.

This repository using local poetry environment.
But in Heroku it not support poetry, so you need create requirements too.

### Setup

1. Create discord app
2. Grant bellow permissions

- OAuth2
  - SCOPES
    - bot
  - BOT PERMISSIONS
    - Send Messages
    - Read Messages/View Channels

3. Access to GENERATED URL to connect discord
4. Open Bot section and click Reset Token and copy displayed token
5. Create .envrc and paste token

※.envrc is controlled by direnv. You can use any other env manage package.

### How to local debug

Please use Poetry virtual env by the bellow command.

```
poetry run python3 bot.py
```

### How to Setup Heroku

1. Login Heroku
2. Deploy from Github repository
3. Set Discord bot token to env config
4. Turn on bot Dynos to start server
