## SETUP

### Setting Up Discord Bot
1. Firstly you have to create a discord application at `https://discord.com/developers/applications`
2. Click New Application and create give a name and create.
3. Create a guild where you will add the bot for testing.
4. Now go to the `OAUTH2 SETTINGS` and under the `OAUTH2 URL GENERATOR` select `bot` and under the Geneeral Permissions select `Administrator`.
5. Installation Type -> `Guild Install`
6. Copy the link and paste it in the browser and you will get an option to add it to a server listed in a drop-down and click on `Authorize`.
7. In the `Bot Settings` under the `Privileged Gateway Intents` check all the Intents to ensure no errors.
8. Now in the `Bot Settings`, copy the Token and add it to the .env file in the root directory of the project like `DISCORD_TOKEN="token_here"`

### Setting Up libraries
1. In the root directory, create a python venv by using `python -m venv ./name-of-venv`.
2. Activate the venv in the terminal using `source ./venv-name/bin/activate` for bash or zsh based terminals or `venv-name\Scripts\activate.ps1` in Powershell or `venv-name\Scripts\activate.bat` in cmd.
3. Now install the following packages `pip3 install requests discord python-dotenv`