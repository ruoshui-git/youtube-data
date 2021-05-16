from names.diligence import MEMBERS_20210228_1, SPECIAL

CHECKED_IN = [
    '曾令建',
    '许东梅',
    '宋伟平',
    '胡学文',
    '李则安',
    '杨帆',
    '郭福华',
    '龙波南',
    '文芳',
    '姚学军',
    '宋友厉',
    '李涛惠',
    '梁文蔼',
    '魏慧明',
    '龚洪良',
    '杨朝',
    '姜瑞',
    '白小娟',
    '毛若水',
    '孟依淼',
    '孟存慧',
    '韦宜芳',
    '巫立霞',
    '孟毅',
]

rep_set = set(CHECKED_IN)
no_report = set(MEMBERS_20210228_1) - set(rep_set) - SPECIAL

print('精进群{}人4:00前未报到：{}'.format(len(no_report), '  '.join(no_report)))

# %%


has_vd_ref = [
    '宋伟平',
    '姜瑞',
    '龙波南',
    '文芳',
    '梁文蔼',
    '范先枝',
    '巫立霞',
    '毛若水',
    '白小娟',
    '李则安',
    '李涛惠',
    '韦宜芳',
    '宋友厉',
    '许东梅',
    '曾令建',
    '孟毅',
    '郭福华',
    '魏慧明',
    '孟依淼',
    '姚学军',
]

vd_ref_set = set(has_vd_ref)
no_ref = set(MEMBERS_20210228_1) - vd_ref_set - SPECIAL

print('2021年3月1日 {}人未写《金水弯弯》观后感：{}'.format(len(no_ref), '  '.join(no_ref)))
# %% [markdown]
# 连续三天没有发言
part = [
    '胡尧',
    '许东梅',
    '李则安',
    '郭福华',
    '曾令建',
    '宋友厉',
    '魏慧明',
    '姜瑞',
    '贾妮',
    '龙波南',
    '许东梅',
    '毛若水',
    '范先枝',
]

part_set = set(part)
no_part = set(MEMBERS_20210228_1) - part_set - SPECIAL
print('2-28 到 3-01，{}人连续三次未发言:{}'.format(len(no_part), '  '.join(no_part)))
