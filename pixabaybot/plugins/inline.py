from urllib.parse import unquote, urlparse
import re
from random import randint
from pixabay import Image

from pyrogram.types import (
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from pixabaybot import pixabaybot, config
from pixabaybot.plugins.helpers import text_parser
from pixabaybot.plugins.texts import default_inline

CACHE_TIME = 0

IMG = "https://cdn.pixabay.com/photo/2017/01/17/14/44/pixabay-1987090_960_720.png"

DEFAULT_RESULTS = [
    InlineQueryResultArticle(
        title="About BetterPixabayBot",
        input_message_content=InputTextMessageContent(
            default_inline
        ),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Help', url='https://t.me/betterpixabaybot?start=start'),
            InlineKeyboardButton('Search', switch_inline_query_current_chat='')]]),
        description="About @BetterPixabayBot",
        thumb_url=IMG,
    )
]


@pixabaybot.on_inline_query()
async def inline(client, query):
    results = []
    string = query.query.lower()
    if string == "":
        await query.answer(
            results=DEFAULT_RESULTS,
            cache_time=CACHE_TIME,
            switch_pm_text="How do I work",
            switch_pm_parameter="start",
        )

        return
    else:
        image = Image(config.get('api', 'key'))
        image.search()
        ims = image.search(q=string.split()[1],
                    lang='en',
                    image_type='photo',
                    orientation='horizontal',
                    category=string.split()[0],
                    safesearch='true',
                    order='latest',
                    page='backgrounds',
                    per_page=50)
        for item in ims['hits']:
            picture_url = item["largeImageURL"]
            text = await text_parser(item)
            buttons = [[
                InlineKeyboardButton('Link', url=f'{item["pageURL"]}'),
                InlineKeyboardButton('Author', url=f'https://pixabay.com/users/{item["user"]}-{item["user_id"]}/')
                ]]
            results.append(InlineQueryResultPhoto(
                photo_url=picture_url,
                title=f'Result:{item["id"]}',
                caption=text,
                description=f"Nothing",
                reply_markup=InlineKeyboardMarkup(buttons)))
    await client.answer_inline_query(
        query.id,
        results=results,
        is_gallery=True,
        cache_time=CACHE_TIME
    )
    return