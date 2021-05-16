rep = [
    '曾令建',
    '宋伟平',
    '文芳',
    '龙波南',
    '姚学军',
    '李则安',
    '宋友厉',
    '李涛惠',
    '龚洪良',
    '许东梅',
    '范先枝',
    '杨帆',
    '姜瑞',
    '郭福华',
    '孟存慧',
    '胡学文',
    '孟依淼',
    '韦宜芳',
    '梁文蔼',
    '魏慧明',
    '杨朝',
    '毛若水',
    '巫立霞',
    '白小娟',
]

from names.diligence import MEMBERS_20210228_1, SPECIAL
report_set = set(rep)
no_report = set(MEMBERS_20210228_1) - report_set - SPECIAL
print(f'报到{len(report_set)}人')
print('精进群{}人4:00前未报到：{}'.format(len(no_report), '  '.join(no_report)))

# 孟毅迟到