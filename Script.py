class script(object):
    START_TXT = """š š·š“š»š¾ {mention}\n\nš¼š š½š°š¼š“ šøš {bot_name},\nšø š²š°š½ šæšš¾ššøš³š“ š¼š¾ššøš“š, š¹ššš š°š³š³ š¼š“ šš¾ šš¾šš š¶šš¾ššæ š°š½š³ š¼š°šŗš“ š¼š“ š°š³š¼šøš½..."""

    HELP_TXT = """š·š“š {}
š·š“šš“ šøš š¼š š·š“š»šæ š²š¾š¼š¼š°š½š³š."""

    ABOUT_TXT = """āÆ š¼š š½š°š¼š“ : {bot_name}
āÆ š²šš“š°šš¾š : <a href=https://t.me/mr_MKN>š¼š.š¼šŗš½ šš¶</a>
āÆ ššæš³š°šš“š : <a href=https://t.me/mkn_bots_updates>š¼šŗš½ š±š¾šš</a>
āÆ š»šøš±šš°šš : šæššš¾š¶šš°š¼
āÆ š»š°š½š¶šš°š¶š“ : šæššš·š¾š½ š¹
āÆ š³š°šš° š±š°šš“ : š¼š¾š½š¶š¾-š³š±
āÆ š±š¾š šš“ššš“š : š·š“šš¾šŗš
āÆ š±ššøš»š³ ššš°ššš : š1.0.43 [š¼š°š¹š¾š]"""

    SOURCE_TXT = """<b>NOTE:</b>
- This is a Eva Mari clone Project
- šš¾ššš²š“ š²š¾š³š“ š²š»šøš²šŗ š·š“š š :<a href=https://github.com/MrMKN/Doctor_Strange-BOT>Doctor_Strange-BOT</a>

<b>DEVS:</b>
- š³šš 1<a href=https://t.me/mr_MKN>š¼š.š¼šŗš½ šš¶</a>
- š³šš 2"""

    FILE_TXT = """ā¤ ššš„š©: šš¢š„š šš­šØš«š ššØšš®š„š../

<b>š±š šššøš½š¶ šš·šøš š¼š¾š³šš»š“ šš¾š š²š°š½ ššš¾šš“ šµšøš»š“š šøš½ š¼š š³š°šš°š±š°šš“ š°š½š³ šø ššøš»š» š¶šøšš“ šš¾š š° šæš“šš¼š°š½š“š½š š»šøš½šŗ  šš¾ š°š²š²š“šš šš·š“ šš°šš“š³ šµšøš»š“š.šøšµ šš¾š šš°š½š šš¾ š°š³š³ šµšøš»š“š šµšš¾š¼ š° šæšš±š»šøš² š²š·š°š½š½š“š» šš“š½š³ šš·š“ šµšøš»š š»šøš½šŗ š¾š½š»š  š¾š šš¾š šš°š½š šš¾ š°š³š³ šµšøš»š“š šµšš¾š¼ š°  šæššøšš°šš“ š²š·š°š½š½š“š» šš¾š š¼ššš š¼š°šŗš“ š¼š“ š°š³š¼šøš½ š¾š½ šš·š“ š²š·š°š½š½š“š» šš¾ š°š²š²š“šš šµšøš»š“š...//</b>

āŖ¼ ššØš¦š¦šš§šš¬ šš§š šš¬šš š āŗ

āŖ /plink āŗāŗ <b>šš“šæš»š šš¾ š°š½š š¼š“š³šøš° šš¾ š¶š“š š»šøš½šŗ.</b>
āŖ /pbatch āŗāŗ <b>ššš“ šš¾šš š¼š“š³šøš° š»šøš½šŗ ššøšš· šš·šøš š²š¾š¼š¼š°š½š³.</b>
āŖ /batch āŗāŗ <b>šš¾ š²šš“š°šš“ š»šøš½šŗ šµš¾š š¼šš»ššøšæš»š“ šµšøš»š“š.</b>

āŖ¼ šš±šš¦š©š„š āŗ

<code>/batch https://t.me/mkn_bots_updates https://t.me/mkn_bots_updates</code>

š²šš“š³šøšš āŗāŗ <a href=https://t.me/mkn_bots_updates><b>š¼šŗš½ š±š¾šš</b></a>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and į©įį©į­  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
 
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """**š°ššš¾ šµšøš»šš“š š¾š½/š¾šµšµ š¼š¾š³šš»š“..
<u>USE THIS COMMAND ON YOUR GROUP</u>

ā¢ /autofilter on - autofilter enable in yor chat
ā¢ /autofilter off - autofilter disable in your chat 

š°ššš¾ šµšøš»šš“š šøš šš·š“ šµš“š°šššš“ šš¾ šµšøš»šš“š š°š½š³ šš°šš“  šš·š“ šµšøš»š“š š°ššš¾š¼š°ššøš²š°š»š»š šµšš¾š¼ š²š·š°š½š½š“š» šš¾ š¶šš¾ššæ. šš¾š š²š°š½ ššš“ šš·š“ šµš¾š»š»š¾ššøš½š¶ š²š¾š¼š¼š°š½š³š šš¾ š¾š½ š°š½š³ š¾šµšµ šš·š“ š°ššš¾šµšøš»šš“š šøš½ šš¾šš š¶šš¾ššæ../

š²š¾š¼š¼š°š½š³š :-
āŗāŗ /set_template - šš“š š²šššš¾š¼ šøš¼š³š± šš“š¼šæš»š°šš“ šµš¾š š°ššš¾ šµšøš»šš“š. 
āŗāŗ /get_template - š¶š“š š²šššš“š½š šøš¼š³š± šš“š¼šæš»š°šš“ š¾šµ š°ššš¾ šµšøš»šš“š.

š²šš“š³šøšš :- <a href=https://t.me/mr_MKN>Mr.MKN TG</a>**"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specifed user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban_user  - <code>to ban a user.</code>
ā¢ /unban_user  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """<b>įāŗ šš¾šš°š» šµšøš»š“š: <code>{}</code></b>
<b>įāŗ šš¾šš°š» ššš“šš: <code>{}</code></b>
<b>įāŗ šš¾šš°š» š²š·š°šš: <code>{}</code></b>
<b>įāŗ ššš“š³ ššš¾šš°š¶š“: <code>{}</code> š¼š±</b>
<b>įāŗ šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> š¼š±</b>"""

    LOG_TEXT_G = """#ššš°šš«šØš®š©
    
<b>įāŗ šš«šØš®š© āŖ¼ {}(<code>{}</code>)</b>
<b>įāŗ š šš āŖ¼ @{}
<b>įāŗ ššØš­šš„ ššš¦ššš«š¬ āŖ¼ {}</b>
<b>įāŗ ššššš šš² āŖ¼ {}</b>

By @{}
"""
    LOG_TEXT_P = """#ššš°šš¬šš«
    
<b>įāŗ šš - <code>{}</code></b>
<b>įāŗ ššš¦š - {}</b>
<b>įāŗ šš - @{}</b>

By @{}
"""

    CREATOR_REQUIRED = """ā<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "ā **Arguments Required**"
      
    KICKED = """āļø Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """š® Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """ā<b>ą“ą“Øąµą“Øąµ Admin ą“ą“ąµą“ą“¤ąµą“¤ ą“øąµą“„ą“²ą“¤ąµą“¤ąµ ą“ą“¾ąµ» ą“Øą“æą“ąµą“ą“æą“²ąµą“² ą“Ŗąµą“ąµą“µą“¾ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """āļø Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ą“ą“Ŗąµą“Ŗąµ ą“ą“²ąµą“²ą“¾ą“ ą“ą“ą“æą“ąµą“ąµą“®ą“¾ą“±ąµą“±ą“æ ą“¤ą“°ą“¾ą“...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
   
