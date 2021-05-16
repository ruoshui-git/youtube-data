# %%
from names.diligence import MEMBERS_20210228
from names.no_summer import NO_SUMMER_NY

common = set(MEMBERS_20210228) & set(NO_SUMMER_NY)
print('精进群 {} 人未参加暑期班：{}。胡尧参加暑期班，但未种上善根。'.format(len(common), '  '.join(common)))

# %% [markdown]
# # Results
# 精进群 7 人未参加暑期班：刘素芳  梁金英  段洪斌  张建涛  刘国凤  贾妮  舒建伟。胡尧参加暑期班，但未种上善根。