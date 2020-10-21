from pyrogram import filters


def dynamic_data_filter(data):
    async def func(flt, _, query):
        return flt.data == query.data
    # "data" kwarg is accessed with "flt.data" above
    return filters.create(func, data=data)


async def text_parser(item):
    text = f'**ID**: `{item["id"]}`\n'
    text += f'👁️`{item["views"]}`   🌟`{item["favorites"]}`   👍`{item["likes"]}   `💬`{item["comments"]}   `⬇️`{item["downloads"]}`\n'
    text += f'**Tags**: `{item["tags"]}`'
    return text