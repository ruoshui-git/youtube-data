# %%
from names.diligence import SPECIAL, MEMBERS_20210228_1
checkin = [
    '龙波南',
    '曾令建',
    '李涛惠',
    '宋伟平',
    '李则安',
    '梁文蔼',
    '郭福华',
    '许东梅',
    '文芳',
    '姚学军',
    '杨帆',
    '龚洪良',
    '范先枝',
    '宋友厉',
    '巫立霞',
    '胡学文',
    '毛若水',
    '姜瑞',
    '白小娟',
    '魏慧明',
    '韦宜芳',
    '孟毅',
    '孟依淼',
    '孟存慧',
]

report_set = set(checkin)
no_report = set(MEMBERS_20210228_1) - report_set - SPECIAL
print(f'报到{len(report_set)}人')
print('精进群{}人4:00前未报到：{}'.format(len(no_report), '  '.join(no_report)))

# 杨朝
vparts = [
    '宋伟平',
    '姜瑞',
    '毛若水',
    '杨帆',
    '范先枝',
    '姚学军',
    '孟毅',
    '梁文蔼',
    '宋友厉',
    '李涛惠',
    '魏慧明',
    '韦宜芳',
    '郭福华',
]

tparts = [
    '曾令建'
]

useless = [
    '胡学文',
    '许东梅',
    '李则安',
    '白小娟',
]

to_note = [
    ('魏慧明', '已经起单，不能发言，以后应注意')
]

other = set(MEMBERS_20210228_1) - set(vparts) - set(useless) - set(SPECIAL)

print('{}人上麦发言：{}'.format(len(vparts), '\t'.join(vparts)))
print('{}人文字发言（300字以上）：{}'.format(len(tparts), '\t'.join(tparts)))
print('{}人发言无效：{}'.format(len(useless), '\t'.join(useless)))
print('{}人未发言：{}'.format(len(other), '\t'.join(other)))
print('注意：')
for name, note in to_note:
    print('{}：{}'.format(name, note))

# %%
