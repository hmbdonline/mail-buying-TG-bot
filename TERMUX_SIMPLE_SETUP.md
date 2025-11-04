# Termux - Super Simple Setup (Copy & Paste)

Just copy and paste these commands one by one!

## Step 1: Install Termux from F-Droid

⚠️ **IMPORTANT:** Download from F-Droid, NOT Google Play!
- Go to: https://f-droid.org
- Install F-Droid
- Search "Termux" in F-Droid
- Install Termux

## Step 2: Setup Termux (Copy & Paste)

Open Termux and paste these commands:

```bash
pkg update -y && pkg upgrade -y
```

Wait for it to finish, then:

```bash
pkg install python git nano -y
```

Wait for it to finish, then:

```bash
pip install python-telegram-bot python-dotenv
```

## Step 3: Get Your Bot Files

### Option A: If you have files on phone

```bash
termux-setup-storage
```

Press "Allow" when asked.

Then copy your bot folder:
```bash
cp -r ~/storage/downloads/telegram-mail-bot ~/
cd ~/telegram-mail-bot
```

### Option B: If you have Git repository

```bash
cd ~
git clone YOUR_REPOSITORY_URL_HERE
cd telegram-mail-bot
```

## Step 4: Create .env File

```bash
nano .env
```

Type this (replace YOUR_BOT_TOKEN with your actual token):
```
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
DATABASE_PATH=/data/data/com.termux/files/home/telegram-mail-bot/data/bot.db
CONFIG_PATH=/data/data/com.termux/files/home/telegram-mail-bot/config
LOG_LEVEL=INFO
LOG_FILE=/data/data/com.termux/files/home/telegram-mail-bot/bot.log
```

To save:
1. Press `Ctrl` and `X` together
2. Press `Y`
3. Press `Enter`

## Step 5: Create Folders

```bash
mkdir data
mkdir config
```

## Step 6: Test Bot

```bash
python main.py
```

You should see:
```
INFO - Starting Telegram Mail Bot...
INFO - Bot is running...
```

✅ **If you see this, it's working!**

Test by messaging your bot on Telegram: `/start`

Press `Ctrl+C` to stop the bot.

## Step 7: Run in Background

Create start script:
```bash
nano start.sh
```

Paste this:
```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/telegram-mail-bot
nohup python main.py > output.log 2>&1 &
echo "Bot started!"
```

Save: `Ctrl+X` → `Y` → `Enter`

Make it work:
```bash
chmod +x start.sh
```

Start bot:
```bash
./start.sh
```

## Step 8: Keep Running

To prevent phone from killing the bot:

```bash
termux-wake-lock
```

## Daily Commands

**Start bot:**
```bash
cd ~/telegram-mail-bot && ./start.sh
```

**Stop bot:**
```bash
pkill -f "python main.py"
```

**Check if running:**
```bash
ps aux | grep python
```

**View logs:**
```bash
cd ~/telegram-mail-bot && tail -f bot.log
```

## ❌ If Something Goes Wrong

### Error: "No module named 'telegram'"

```bash
pip install python-telegram-bot
```

### Error: "TELEGRAM_BOT_TOKEN not found"

Your .env file is wrong. Redo Step 4.

### Error: "Permission denied"

```bash
chmod +x start.sh
```

### Bot not responding?

Check logs:
```bash
cd ~/telegram-mail-bot
cat bot.log
```

### Still not working?

Run this fix:
```bash
cd ~/telegram-mail-bot
pkill -f "python main.py"
pip install --upgrade python-telegram-bot python-dotenv
python main.py
```

Watch for errors and tell me what you see!

## ✅ Success Checklist

- [ ] Termux installed from F-Droid
- [ ] Python installed: `python --version` shows version
- [ ] Telegram library installed: `pip list | grep telegram` shows it
- [ ] .env file created with bot token
- [ ] data and config folders created
- [ ] Bot runs with `python main.py`
- [ ] Bot responds to `/start` on Telegram

## 🆘 Need Help?

Tell me:
1. Which step failed?
2. What error message did you see?
3. Run this and share output:
```bash
python --version
pip list | grep telegram
cat .env
ls -la
```

I'll help you fix it! 🚀
