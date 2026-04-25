#! /usr/bin/env python
# coding=utf-8
from easydict import EasyDict as edict

cfg = edict()

cfg.COMPANY            = 'AI'
cfg.TOOL_NAME          = 'Angelo翻译工具'
cfg.TITLE              = cfg.TOOL_NAME + ' V1.0'
cfg.CONFIGINI          = 'AI.ini'

# ==================== 文言 ====================
cfg.CHOOSE_PROJECT     = '选择工程目录'
cfg.CHOOSE_FILE        = '选择翻译文件'
cfg.TRANSLATE_LANGUAGE = '翻译语言'
cfg.BASE_LANGUAGE      = '参照语言'
cfg.LOG_RECORD         = '日志记录'
cfg.BE_READY           = '当前进度'
cfg.QUICK_TRANSLATE    = '一键翻译'
cfg.OLD_TRANSLATE      = '旧文言'
cfg.NEW_TRANSLATE      = '新文言'
cfg.TRANSLATE_DIFF     = '翻译差异表'
cfg.TRANSLATE_SAME     = '翻译重复表'
cfg.EXCEL_PAGE         = 'Excel页面'
cfg.NO_CONTENT         = '空记录'
cfg.APP_FROM           = '来源应用'
cfg.TRANSLATE_LOSS     = '文言缺失表'

# ==================== 参照语言（仅中文和英文）===================
cfg.BASE_COLUMNS = {
    'zh': '中文',
    'en': '英文'
}

# ==================== 所有支持的语言列 ====================
cfg.LANGUAGES_COLUMNS = {
    'zh-cn': '中文(简体)',
    'en': '英文',
    'zh-tw': '中文(繁体-台湾)',
    'zh-hk': '中文(繁体-香港)',
    'th': '泰语',
    'de': '德语',
    'fr': '法语',
    'es': '西班牙语',
    'es-MX': '西班牙语(墨西哥)',
    'es-CL': '西班牙语(智利)',
    'nl': '荷兰语',
    'no': '挪威语',
    'da': '丹麦语',
    'sv': '瑞典语',
    'it': '意大利语',
    'pt': '葡萄牙语',
    'pt-BR': '葡萄牙语(巴西)',
    'el': '希腊语',
    'ar': '阿拉伯语',
    'tr': '土耳其语',
    'fi': '芬兰语',
    'pl': '波兰语',
    'uk': '乌克兰语',
    'ro': '罗马尼亚语',
    'cs': '捷克语',
    'hu': '匈牙利语',
    'sk': '斯洛伐克语',
    'sl': '斯洛文尼亚语',
    'hr': '克罗地亚语',
    'he': '希伯来语',
    'vi': '越南语',
    'ru': '俄语',
    'sr': '塞尔维亚语',
    'bg': '保加利亚语',
    'et': '爱沙尼亚语',
    'lv': '拉脱维亚语',
    'lt': '立陶宛语',
    'kk': '哈萨克语',
    'ja': '日语',
    'fa': '波斯语',
    'tl': '菲律宾语',
}

# ==================== 语言别名（最重要修复）===================
cfg.LANGUAGE_ALIASES = {
    'zh': [
        '中文', 'zh', 'Chinese', '简体中文', '中文(简体)',
        'zh-cn', 'zhcn', 'Chinese Simplified', 'zh-cn-Chinese', '参照'
    ],
    'en': [
        '英语', '英文', '英', 'eng', 'English', 'Eng', 'en-English',
        'en', 'English (United States)', 'English (UK)'
    ],
    'zh-tw': ['中文(繁体)', '繁体中文(台湾)', '台湾繁体', 'zhtw', 'Chinese Traditional TW', 'zh-tw-Traditional Chinese', '繁中', '台繁'],
    'zh-hk': ['中文(繁体)', '繁体中文(香港)', '香港繁体', 'zhhk', 'Chinese Traditional HK', 'zh-hk-Traditional Chinese', '港繁'],
    'th': ['泰语', '泰国语', '泰', 'Thai', 'Th', 'th-Thai'],
    'de': ['德语', '德国语', '德', 'German', 'De', 'de-German'],
    'fr': ['法语', '法国语', '法', 'French', 'Fr', 'fr-French'],
    'es': ['西班牙语', '西语', '西班牙文', 'Spanish', 'Esp', 'es-Spanish'],
    'es-MX': ['西班牙语(墨西哥)', '墨西哥西班牙语', '墨西西语', 'Spanish Mexican', 'es-MX-Mexican Spanish', 'es-MX'],
    'es-CL': ['西班牙语(智利)', '智利西班牙语', '智西语', 'Spanish Chilean', 'es-CL-Chilean Spanish', 'es-CL'],
    'nl': ['荷兰语', '荷兰文', '荷', 'Dutch', 'Nl', 'nl-Dutch'],
    'no': ['挪威语', '挪威文', '挪', 'Norwegian', 'No', 'no-Norwegian'],
    'da': ['丹麦语', '丹麦文', '丹', 'Danish', 'Da', 'da-Danish'],
    'sv': ['瑞典语', '瑞典文', '瑞', 'Swedish', 'Sv', 'sv-Swedish'],
    'it': ['意大利语', '意大利文', '意', 'Italian', 'It', 'it-Italian'],
    'pt': ['葡萄牙语', '葡语', '葡萄牙文', 'Portuguese', 'Pt', 'pt-Portuguese'],
    'pt-BR': ['葡萄牙语(巴西)', '巴西葡语', '葡语(巴西)', 'Portuguese Brazilian', 'pt-BR-Brazilian Portuguese', 'pt-BR'],
    'el': ['希腊语', '希腊文', '希', 'Greek', 'El', 'el-Greek'],
    'ar': ['阿拉伯语', '阿语', '阿拉伯文', 'Arabic', 'Ar', 'ar-Arabic'],
    'tr': ['土耳其语', '土耳其文', '土', 'Turkish', 'Tr', 'tr-Turkish'],
    'fi': ['芬兰语', '芬兰文', '芬', 'Finnish', 'Fi', 'fi-Finnish'],
    'pl': ['波兰语', '波兰文', '波', 'Polish', 'Pl', 'pl-Polish'],
    'uk': ['乌克兰语', '乌克兰文', '乌', 'Ukrainian', 'Uk', 'uk-Ukrainian'],
    'ro': ['罗马尼亚语', '罗马尼亚文', '罗', 'Romanian', 'Ro', 'ro-Romanian'],
    'cs': ['捷克语', '捷克文', '捷', 'Czech', 'Cs', 'cs-Czech'],
    'hu': ['匈牙利语', '匈牙利文', '匈', 'Hungarian', 'Hu', 'hu-Hungarian'],
    'sk': ['斯洛伐克语', '斯洛伐克文', '斯伐', 'Slovak', 'Sk', 'sk-Slovak'],
    'sl': ['斯洛文尼亚语', '斯洛文尼亚文', '斯文', 'Slovenian', 'Sl', 'sl-Slovenian'],
    'hr': ['克罗地亚语', '克罗地亚文', '克', 'Croatian', 'Hr', 'hr-Croatian'],
    'he': ['希伯来语', '希伯来文', '以', 'Hebrew', 'He', 'he-Hebrew'],
    'vi': ['越南语', '越南文', '越', 'Vietnamese', 'Vi', 'vi-Vietnamese'],
    'ru': ['俄语', '俄罗斯语', '俄文', 'Russian', 'Ru', 'ru-Russian'],
    'sr': ['塞尔维亚语', '塞尔维亚文', '塞', 'Serbian', 'Sr', 'sr-Serbian'],
    'bg': ['保加利亚语', '保加利亚文', '保', 'Bulgarian', 'Bg', 'bg-Bulgarian'],
    'et': ['爱沙尼亚语', '爱沙尼亚文', '爱', 'Estonian', 'Et', 'et-Estonian'],
    'lv': ['拉脱维亚语', '拉脱维亚文', '拉', 'Latvian', 'Lv', 'lv-Latvian'],
    'lt': ['立陶宛语', '立陶宛文', '立', 'Lithuanian', 'Lt', 'lt-Lithuanian'],
    'kk': ['哈萨克语', '哈萨克文', '哈', 'Kazakh', 'Kk', 'kk-Kazakh'],
    'ja': ['日语', '日本语', '日', 'Japanese', 'Ja', 'ja-Japanese'],
    'fa': ['波斯语', '波斯文', '伊朗语', 'Farsi', 'Persian', 'fa-Persian', 'fa'],
    'tl': ['菲律宾语', '菲律宾文', '他加禄语', 'Filipino', 'Tagalog', 'tl-Filipino', 'tl']
}

# ==================== 文件夹变体 ====================
cfg.LANGUAGE_VARIANTS_INSIDE = {
    'en': ['values-en-rUS', 'values-en', 'values-en-rGB'],
    'zh-cn': ['values-zh-rCN', 'values-zh'],
    'zh-tw': ['values-zh-rTW'],
    'zh-hk': ['values-zh-rHK'],
    'th': ['values-th-rTH'],
    'de': ['values-de-rDE', 'values-de'],
    'fr': ['values-fr-rFR'],
    'es': ['values-es-rES', 'values-es'],
    'es-MX': ['values-es-rMX'],
    'es-CL': ['values-es-rCL'],
    'nl': ['values-nl-rNL'],
    'no': ['values-no-rNO'],
    'da': ['values-da-rDK'],
    'sv': ['values-sv-rSE'],
    'it': ['values-it'],
    'pt': ['values-pt-rPT'],
    'pt-BR': ['values-pt-rBR'],
    'el': ['values-el-rGR'],
    'ar': ['values-ar-rAE', 'values-ar', 'values-ar-rSA'],
    'tr': ['values-tr-rTR'],
    'fi': ['values-fi-rFI'],
    'pl': ['values-pl-rPL'],
    'uk': ['values-uk-rUA'],
    'ro': ['values-ro-rRO'],
    'cs': ['values-cs-rCZ'],
    'hu': ['values-hu-rHU'],
    'sk': ['values-sk-rSK'],
    'sl': ['values-sl-rSI'],
    'hr': ['values-hr-rHR'],
    'he': ['values-he-rIL'],
    'vi': ['values-vi-rVN'],
    'ru': ['values-ru-rRU', 'values-ru'],
    'sr': ['values-sr-rRS'],
    'bg': ['values-bg-rBG'],
    'et': ['values-et-rEE'],
    'lv': ['values-lv-rLV'],
    'lt': ['values-lt-rLT'],
    'kk': ['values-kk-rKZ'],
    'ja': ['values-ja-rJP'],
    'fa': ['values-fa', 'values-fa-rIR'],
    'tl': ['values-tl-rPH']
}

# Excel 相关
cfg.ENGLISH = ['values-en', 'values-en-rUS', 'values-en-rGB']
cfg.CHINESE = ['values-zh-rCN', 'values-zh']
