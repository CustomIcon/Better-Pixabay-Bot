def lister():
    ava = ""
    j = 1
    for i in table_list:
        if j == 2:
            ava += "|  `{:<10}`  \n".format(i)
            j = 0
        else:
            ava += "|  `{:<10}`  ".format(i)
        j += 1
    return ava

table_list = ['fashion', 'backgrounds', 'nature', 'science', 'education', 'feelings','health',
'people', 'religion', 'places', 'animals', 'industry', 'computer', 'food', 'sports',
'transportation', 'travel', 'buildings','business', 'music']

helptext = "With [BetterPixabaybot], you can scrap wallpapers from pixabay website to take wherever you go."

helptext1 = """
**📖 Help (1 of 2)**

You can only use this bot as how it is via inline, Check next page to find more about inline.
"""

helptext2 = """
**📖 Help (2 of 2)**

You can send me query via inline, like this one:
`@betterpixabaybot catagory search_query`

Accepted values:
`+============+============+`
{table}
`+============+============+`
""".format(table=lister())

tiptext1 = """
**💡 Tip (1 of 1)**

you must pat @notmynamae in order to keep this bot alive! trust me.
"""

default_inline = """
**BetterPixabayBot**\nA Project based on @OpenPixabayBot by [Naipofo](https://github.com/naipofo)
written in pyrogram by [pokurt](https://github.com/pokurt)
"""