# test_bot.py
from unittest import mock
from unittest.mock import MagicMock

from telebot.types import Chat, Message, User

from bot import send_welcome

mock_chat = Chat(id=123, type="")

mock_message = Message(
    message_id=123,
    from_user=User(123, False, "name"),
    date=None,
    chat=mock_chat,
    content_type="text",
    options=[],
    json_string=None,
)


def test_send_welcome():
    bot = MagicMock()

    with mock.patch("bot.bot", new=bot):
        send_welcome(mock_message)

    bot.reply_to.assert_called_once_with(
        mock_message,
        """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""",
    )
