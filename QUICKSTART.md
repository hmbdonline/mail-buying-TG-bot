# Quick Start Guide

Get your Telegram Mail Bot up and running in 5 minutes!

## Prerequisites

- Python 3.9+
- A Telegram account
- A bot token from [@BotFather](https://t.me/BotFather)

## Step 1: Get Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the instructions
3. Copy the bot token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 2: Install

```bash
# Clone or download the project
cd telegram-mail-bot

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Configure

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your bot token
# On Windows: notepad .env
# On Mac/Linux: nano .env
```

Add this line to `.env`:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

## Step 4: Run

```bash
python main.py
```

You should see:
```
INFO - Starting Telegram Mail Bot...
INFO - Database initialization completed successfully
INFO - Configuration initialization completed successfully
INFO - Bot is running...
```

## Step 5: Test

1. Open Telegram and find your bot (search for the username you gave it)
2. Send `/start` to your bot
3. You should see a welcome message with buttons!

## Admin Access

If your Telegram username is **@s00s22**, you have full admin access:

1. Send `/admin` to your bot
2. You'll see the admin panel with all management options

If you're not @s00s22, you'll need the main admin to add you as a secondary admin.

## Common Issues

### "Bot doesn't respond"
- Check that the bot token is correct in `.env`
- Make sure the bot is running (you should see "Bot is running..." in the console)
- Try stopping and restarting: Press Ctrl+C, then run `python main.py` again

### "TELEGRAM_BOT_TOKEN not found"
- Make sure you created the `.env` file
- Make sure the token line doesn't have spaces around the `=`
- Correct: `TELEGRAM_BOT_TOKEN=123456:ABC`
- Wrong: `TELEGRAM_BOT_TOKEN = 123456:ABC`

### "Module not found"
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct directory

## What's Next?

- Read the [README.md](README.md) for full documentation
- Check [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for technical details
- Start customizing buttons and messages through the admin panel!

## Quick Commands

- `/start` - Start the bot (all users)
- `/help` - Show help message (all users)
- `/admin` - Open admin panel (admins only)

## Need Help?

Check the logs in `bot.log` for detailed error messages.

---

**That's it! Your bot is ready to use! 🎉**
