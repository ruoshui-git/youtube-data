# %%
from names.diligence import MEMBERS_20210228, SPECIAL
participated = [
    '贾妮',
    '巫立霞',
    '姜瑞',
    '刘素芳',
    '李涛惠',
    '许东梅',
    '梁金英',
    # '姜瑞',
    '毛若水',
    '宋友厉',
    '文芳',
    '李则安',
    '许东梅', # Repeat
    '龙波南',
    '范先枝',
    '孟依淼',
    '白小娟',
    '杨帆',
    '宋伟平',
    '韦宜芳',
    '郭福华',
    '梁文蔼',
    '魏慧明'
]

part_set = set(participated)
others = set(MEMBERS_20210228) - part_set - SPECIAL

print('{} 人发未留言: {}'.format(
    len(others), "\t".join(others)))
print('{} 人留言: {}'.format(
    len(part_set), "\t".join(part_set)))


# %% [markdown]
# # 2021-02-28 早晨删除人员
# 共36人：李青松	吴涵水	彭立英	闫丽娜	相里小莉	李靓	姜山水	谭诚	刘玮琦	赵洁	陈小君	李爱娟	姜双锋	李思瑶	姜增水	程根水	赵云青	杨三峰	顾志芳	周友琴	魏建军	何兴国	侯尚琛	侯会涛	朱红斌	王世英	程水妹	李菊花	崔於	李向水	史文燕	胡伶俐	熊明成	李南京	许根生	王哲媛

# 新加入3人：梁金英	巫立霞	段洪斌
# %%
#
from names.diligence import MEMBERS

deleted = (set(MEMBERS['2021-02-27']) - set(MEMBERS['2021-02-28']))
print('{} people deleted: {}'.format(len(deleted), '\t'.join(deleted)))
joined = set(MEMBERS['2021-02-28']) - set(MEMBERS['2021-02-27'])
print('{} people joined: {}'.format(len(joined), '\t'.join(joined)))
