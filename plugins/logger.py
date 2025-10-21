from pyrogram import Client
from config import LOG_CHANNEL
from datetime import datetime

class Logger:
    """Centralized logging system for all bot activities"""
    
    @staticmethod
    async def log_link_change(client: Client, channel_id: int, old_link: str, new_link: str, status: str):
        """Log link change events"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>🔗 Link Changed</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>Channel ID:</b> <code>{channel_id}</code>
<b>Old Link:</b> <code>@{old_link}</code>
<b>New Link:</b> <code>@{new_link}</code>
<b>Status:</b> {'✅ Success' if status == 'success' else '❌ Failed'}
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging link change: {e}")

    @staticmethod
    async def log_channel_added(client: Client, user_id: int, channel_id: int, base_username: str, interval: int):
        """Log when a channel is added"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>➕ Channel Added</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Channel ID:</b> <code>{channel_id}</code>
<b>Base Username:</b> <code>{base_username}</code>
<b>Interval:</b> <code>{interval}s</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging channel added: {e}")

    @staticmethod
    async def log_channel_stopped(client: Client, user_id: int, channel_id: int):
        """Log when a channel rotation is stopped"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>⏹️ Channel Stopped</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Channel ID:</b> <code>{channel_id}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging channel stopped: {e}")

    @staticmethod
    async def log_channel_resumed(client: Client, user_id: int, channel_id: int):
        """Log when a channel rotation is resumed"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>▶️ Channel Resumed</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Channel ID:</b> <code>{channel_id}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging channel resumed: {e}")

    @staticmethod
    async def log_error(client: Client, error_type: str, user_id: int, details: str):
        """Log errors and exceptions"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>❌ Error Occurred</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>Error Type:</b> <code>{error_type}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Details:</b> <code>{details}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging error: {e}")

    @staticmethod
    async def log_user_login(client: Client, user_id: int, user_name: str):
        """Log user login"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>🔐 User Login</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>User Name:</b> {user_name}
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging user login: {e}")

    @staticmethod
    async def log_user_logout(client: Client, user_id: int):
        """Log user logout"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>🚪 User Logout</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging user logout: {e}")

    @staticmethod
    async def log_stats(client: Client, total_users: int, active_channels: int, total_channels: int):
        """Log bot statistics"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>📊 Bot Statistics</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>Total Users:</b> <code>{total_users}</code>
<b>Active Channels:</b> <code>{active_channels}</code>
<b>Total Channels:</b> <code>{total_channels}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging stats: {e}")

logger = Logger()
ntervalrval:</b> <code>{interval}s</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging channel added: {e}")

    @staticmethod
    async def log_channel_stopped(client: Client, user_id: int, channel_id: int):
        """Log when a channel rotation is stopped"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>⏹️ Channel Stopped</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Channel ID:</b> <code>{channel_id}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging channel stopped: {e}")

    @staticmethod
    async def log_channel_resumed(client: Client, user_id: int, channel_id: int):
        """Log when a channel rotation is resumed"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>▶️ Channel Resumed</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Channel ID:</b> <code>{channel_id}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging channel resumed: {e}")

    @staticmethod
    async def log_error(client: Client, error_type: str, user_id: int, details: str):
        """Log errors and exceptions"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>❌ Error Occurred</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>Error Type:</b> <code>{error_type}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>Details:</b> <code>{details}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging error: {e}")

    @staticmethod
    async def log_user_login(client: Client, user_id: int, user_name: str):
        """Log user login"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>🔐 User Login</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
<b>User Name:</b> {user_name}
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging user login: {e}")

    @staticmethod
    async def log_user_logout(client: Client, user_id: int):
        """Log user logout"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>🚪 User Logout</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>User ID:</b> <code>{user_id}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging user logout: {e}")

    @staticmethod
    async def log_stats(client: Client, total_users: int, active_channels: int, total_channels: int):
        """Log bot statistics"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"""<b>📊 Bot Statistics</b>

<b>Timestamp:</b> <code>{timestamp}</code>
<b>Total Users:</b> <code>{total_users}</code>
<b>Active Channels:</b> <code>{active_channels}</code>
<b>Total Channels:</b> <code>{total_channels}</code>
"""
            await client.send_message(LOG_CHANNEL, message)
        except Exception as e:
            print(f"[v0] Error logging stats: {e}")

logger = Logger()
