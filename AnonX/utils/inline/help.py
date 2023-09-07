from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="💘ᴀᴅᴍɪɴ💘",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🌷ᴀᴜᴛʜ🌷",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="🌹ʙʟᴀᴄʟɪsᴛ🌹",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🌸ɢᴄᴀsᴛ🌸",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🍒ɢʙᴀɴ🍒",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🥰ʟʏʀɪᴄs🥰",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✨ᴘɪɴɢ✨",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="⚡ᴘʟᴀʏ⚡",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="🎄ᴘ-ʟɪsᴛ🎄",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💓ᴠ-ᴄᴀsᴛ💓",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="❤sᴛᴀʀᴛ❤",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="❣️sᴜᴅᴏ❣️",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🌹ᴛᴀɢɢᴇʀ🌹",
                    callback_data="help_callback hb13",
                
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⚡ ʜᴇʟᴘ ⚡",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
