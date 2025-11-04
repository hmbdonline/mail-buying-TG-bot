# Telegram Mail Bot

A dynamic Telegram bot for managing mail purchases with a hierarchical admin system and complete in-bot configuration.

## Features

- **Hierarchical Admin System**: Main admin (@s00s22) with full control, plus secondary admins with customizable permissions
- **Dynamic Configuration**: Manage all bot elements (buttons, messages, workflows) through Telegram interface
- **Transaction Management**: Handle mail purchase transactions with full tracking
- **User Management**: Track users, block/unblock, and view transaction history
- **Audit Trail**: Complete logging of all admin actions
- **Persistent Storage**: SQLite database and JSON configuration files

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd telegram-mail-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your configuration:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   DATABASE_PATH=data/bot.db
   CONFIG_PATH=config
   LOG_LEVEL=INFO
   LOG_FILE=bot.log
   ```

4. **Initialize the bot**
   
   On first run, the bot will automatically:
   - Create the database schema
   - Initialize default configuration files
   - Set up the main admin (@s00s22)
   
   ```bash
   python main.py
   ```

## Configuration

### Environment Variables

- `TELEGRAM_BOT_TOKEN` (required): Your Telegram bot token from @BotFather
- `DATABASE_PATH` (optional): Path to SQLite database file (default: `data/bot.db`)
- `CONFIG_PATH` (optional): Path to configuration directory (default: `config`)
- `LOG_LEVEL` (optional): Logging level (default: `INFO`)
- `LOG_FILE` (optional): Log file path (default: `bot.log`)

### Configuration Files

The bot uses JSON files for dynamic configuration:

- `config/bot_config.json`: Main bot settings
- `config/buttons.json`: Button definitions
- `config/messages.json`: Message templates

These files are automatically created on first run and can be modified through the Telegram interface by admins.

## Usage

### For Main Admin (@s00s22)

The main admin has unrestricted access to all bot functions:

1. Start a chat with your bot
2. Use `/admin` to access the admin panel
3. Manage buttons, messages, admins, users, and view analytics

**Main Admin Capabilities:**
- Create, edit, and delete buttons
- Create, edit, and delete messages
- Add and remove secondary admins
- Manage admin permissions
- View all transactions
- Block/unblock users
- View analytics and export data

### For Secondary Admins

Secondary admins have access based on their assigned permissions:

1. Start a chat with the bot
2. Use `/admin` to access available admin functions
3. Perform actions within your permission scope

**Available Permissions:**
- `manage_buttons`: Create, edit, delete buttons
- `manage_messages`: Create, edit, delete messages
- `view_transactions`: View user purchase history
- `manage_users`: Block/unblock users, view user list
- `view_analytics`: Access bot statistics

### For Users

Regular users can:

1. Start the bot with `/start`
2. Navigate using the dynamic button interface
3. Complete mail purchase transactions
4. View their transaction history

## Project Structure

```
telegram-mail-bot/
├── bot/
│   ├── __init__.py
│   ├── bot_main.py              # Main bot class
│   ├── handlers/                # Command and callback handlers
│   │   └── __init__.py
│   ├── managers/                # Business logic managers
│   │   ├── __init__.py
│   │   ├── admin_manager.py     # Admin management
│   │   ├── button_manager.py    # Button CRUD operations
│   │   ├── message_manager.py   # Message CRUD operations
│   │   ├── ui_builder.py        # Keyboard builder
│   │   ├── transaction_manager.py
│   │   ├── transaction_logger.py
│   │   └── user_manager.py
│   ├── database/                # Database layer
│   │   ├── __init__.py
│   │   ├── db_manager.py        # Database operations
│   │   └── schema.py            # Database schema
│   └── utils/                   # Utility modules
│       ├── __init__.py
│       ├── config_manager.py    # Configuration file management
│       ├── config_initializer.py
│       ├── permissions.py       # Permission system
│       ├── admin_logger.py      # Admin action logging
│       ├── validators.py        # Input validation
│       └── error_handler.py     # Error handling
├── config/                      # Configuration files (JSON)
│   ├── bot_config.json
│   ├── buttons.json
│   └── messages.json
├── data/                        # Database files
│   └── bot.db
├── .env                         # Environment variables
├── .env.example                 # Example environment file
├── requirements.txt             # Python dependencies
├── main.py                      # Entry point
└── README.md                    # This file
```

## Database Schema

### Tables

- **admins**: Admin users and their permissions
- **users**: Regular users and their information
- **transactions**: Mail purchase transactions
- **admin_actions**: Audit log of admin actions

## Development

### Adding New Features

1. Create manager classes in `bot/managers/` for business logic
2. Add handlers in `bot/handlers/` for user interactions
3. Update the UI builder in `bot/managers/ui_builder.py` for new interfaces
4. Add validation in `bot/utils/validators.py` for new inputs

### Testing

The bot includes comprehensive error handling and logging. Check `bot.log` for detailed operation logs.

## Troubleshooting

### Bot doesn't start

- Check that `TELEGRAM_BOT_TOKEN` is set correctly in `.env`
- Verify Python version is 3.9 or higher
- Ensure all dependencies are installed: `pip install -r requirements.txt`

### Database errors

- Check that the `data/` directory exists and is writable
- Delete `data/bot.db` to reset the database (will lose all data)
- Check logs in `bot.log` for specific error messages

### Configuration errors

- Verify JSON files in `config/` are valid
- Delete configuration files to regenerate defaults
- Check file permissions on the `config/` directory

### Permission issues

- Only the main admin (@s00s22) can manage other admins
- Secondary admins can only perform actions within their assigned permissions
- Check admin_actions table in database for audit trail

## Security Considerations

- Keep your bot token secret and never commit it to version control
- The bot uses parameterized queries to prevent SQL injection
- All user inputs are validated and sanitized
- Admin actions are logged for accountability
- Rate limiting should be implemented for production use

## Support

For issues or questions:
1. Check the logs in `bot.log`
2. Review the troubleshooting section above
3. Contact the main admin (@s00s22)

## License

[Add your license information here]

## Credits

Built with:
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLite
- Python 3.9+
