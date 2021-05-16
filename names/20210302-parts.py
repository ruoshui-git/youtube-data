from names.diligence import MEMBERS_20210228_1, SPECIAL

rep = [
'宋伟平',
'曾令建',
'李涛惠',
'范先枝',
'李则安',
'郭福华',
'许东梅',
'姚学军',
'文芳',
'宋友厉',
'杨帆',
'魏慧明',
'姜瑞',
'胡学文',
'龚洪良',
'毛若水',
'孟依淼',
'孟存慧',
'巫立霞',
'韦宜芳',
'孟毅',
'白小娟',
'龙波南',
]

report_set = set(rep)
no_report = set(MEMBERS_20210228_1) - report_set - SPECIAL

print('精进群{}人4:00前未报到：{}'.format(len(no_report), '  '.join(no_report)))
print(f'报到{len(report_set)}人')
