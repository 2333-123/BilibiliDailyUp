'''
Author: ForMemRs
Date: 2022-06-19 17:41:19
LastEditors: ForMemRS
LastEditTime: 2022-08-15 10:06:27
FilePath: /bilibili_daily_up/config.py
Blog: https://www.52pojie.cn/?1507943
Copyright (c) 2022 by ForMemRs, All Rights Reserved.
'''

COIN_OR_NOT = True
# 是否投币
# 开启后如果硬币数量小于5默认也会跳过


SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币


STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md
# 新华网 人民日报 央视频  王冰冰 英雄联盟赛事

COOKIE_LIST = ['sid=7g9u4fnx; DedeUserID=325636191; DedeUserID__ckMd5=9a80ef2ba1f6f6bb; SESSDATA=411fe845%2C1675512532%2C004ca*81; bili_jct=69777ed52171e36020f130a9cf1783ee; buvid3=7B8DEA2D-F526-0F6E-443A-989D647E7D0338604infoc; i-wanna-go-back=-1; b_ut=5; _uuid=5FAD1176-11F9-DFF4-14E1-22910695DED5257160infoc; buvid4=739BD274-54FA-F1BA-8C2B-A11E9481A69F19603-022012119-RSY0y6c/4STOPLtHpmFe0A%3D%3D; LIVE_BUVID=AUTO6816599606642390; buvid_fp=0a271cab2379f604f3861935cca06769; CURRENT_FNVAL=4048; fingerprint3=3408ac9a7c570f46c1a30ad18b016364; fingerprint=7a0a0df05db8e07847293d178dc1feae; PVID=4']
# Bilibili的COOKIE获取的方法见README.md
# 支持多账号，需要多账号请在列表中添加多个COOKIE

PUSH_OR_NOT = True
# 是否推送消息
TOKEN = '4617cfdc6c0342e388d8552a56b340af'
# PUSH PLUS的TOKEN 官网为 https://www.pushplus.plus
