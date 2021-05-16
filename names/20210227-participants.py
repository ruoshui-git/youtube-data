
# 20210227 participants
# 毛若水
# 宋伟平
# 刘素芳
# 魏慧明
# 贾妮
# 文芳
# 刘国凤
# 范先枝
# 李涛惠
# 白小娟
# 张建涛
# 梁文蔼
# 龙波南
# 舒建伟
# 孟存慧
# 许东梅
# 宋友厉
# 胡尧
# 姚学军
# 李则安
# 孟依淼
# 韦宜芳
# 郭福华
# 孟毅
# 胡学文


# joined later:
# 云宏成
# 程根水
# 程水妹

# %%
from names.diligence import MEMBERS_20210227, SPECIAL
participated = [
    '毛若水',
    '宋伟平',
    '刘素芳',
    '魏慧明',
    '贾妮',
    '文芳',
    '刘国凤',
    '范先枝',
    '李涛惠',
    '白小娟',
    '张建涛',
    '梁文蔼',
    '龙波南',
    '舒建伟',
    '孟存慧',
    '许东梅',
    '宋友厉',
    '胡尧',
    '姚学军',
    '李则安',
    '孟依淼',
    '韦宜芳',
    '郭福华',
    '孟毅',
    '胡学文',
    '杨朝',
    '杨帆']


others = [p for p in MEMBERS_20210227 if p not in participated and p not in SPECIAL]
other_set = set(MEMBERS_20210227) - set(participated) - SPECIAL
print('   '.join(others))
print(f'Participated: {len(participated)}')
print(f'Didn\'t participate: {len(others)}')
# %%
