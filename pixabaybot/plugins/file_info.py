from pixabaybot import pixabaybot
from pixabaybot.plugins.helpers import dynamic_data_filter
from pixabaybot.plugins.inline import message_cache

@pixabaybot.on_callback_query(dynamic_data_filter('file_info'))
async def file_info_callback(client, query):
    try:
        await client.answer_callback_query(query.id, message_cache[query.from_user.id], show_alert=True)
    except KeyError:
        await client.answer_callback_query(query.id, 'Error: This messsage is too old or you are not the author of the message', show_alert=True)