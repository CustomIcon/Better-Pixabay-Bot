from pyrogram import filters


def dynamic_data_filter(data):
    async def func(flt, _, query):
        return flt.data == query.data
    # "data" kwarg is accessed with "flt.data" above
    return filters.create(func, data=data)


async def text_parser(item):
    text = f'**Post ID**: `{item["id"]}`\n'
    text += f'**Views:** `{item["views"]}`\n'
    text += f'**Favourites:** `{item["favorites"]}`\n'
    text += f'**Likes:** `{item["likes"]}`\n'
    text += f'**Comments:** `{item["comments"]}`'
    return text