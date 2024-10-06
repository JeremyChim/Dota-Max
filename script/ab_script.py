def step_1(ab: str) -> tuple:
    ls = ab.split('"')
    abn, abv, tab = ls[1], ls[3], ls[0]  # name, value, tab
    return abn, abv, tab


def step_2(style: int, abn: str, abv: str) -> str:
    # 定义模板字典
    styles = {
        1: '''[tab]"ab_name"
[tab]{
[tab]\t"value"[tab]\t\t\t\t\t"ab_value"
[tab]\t__sa+__
[tab]\t__sp+__
[tab]}    
''',
        2: '''[tab]"ab_name"[tab]\t\t\t\t\t"ab_value"
[tab]__sa+__
[tab]__sp+__ 
'''
    }

    template = styles.get(style, styles[1])  # 默认使用样式1，除非明确指定样式2
    new_style = template.replace('ab_name', abn).replace('ab_value', abv)  # 替换模板中的占位符

    if abn == 'value' and style != 2:  # 特殊处理：如果abn是 value，则使用样式2
        new_style = styles[2].replace('ab_name', abn).replace('ab_value', abv)

    return new_style


def step_3(sa_enable: bool, sp_enable: bool, new_style: str) -> str:
    sa_mod = '''"special_bonus_shard"[tab]\t"sa_value"'''
    sp_mod = '''"special_bonus_scepter"[tab]\t"sp_value"'''

    sa_mod = sa_mod if sa_enable else ''
    sp_mod = sp_mod if sp_enable else ''

    return new_style.replace('__sa+__', sa_mod).replace('__sp+__', sp_mod)


def step_4(cd_enable: bool,
           sa_value: str,
           sp_value: str,
           sa_cd: str,
           sp_cd: str,
           new_mod: str,
           abn: str) -> str:
    if cd_enable:
        return new_mod.replace('sa_value', sa_cd).replace('sp_value', sp_cd)

    ls = ['Cooldown', 'CastPoint', 'ManaCost', 'Delay']
    for i in ls:
        if i.lower() in abn.lower():
            return new_mod.replace('sa_value', sa_cd).replace('sp_value', sp_cd)

    return new_mod.replace('sa_value', sa_value).replace('sp_value', sp_value)


def step_5(tab: str, new_mod2: str):
    return new_mod2.replace('[tab]', tab)


def ab_replace(style: int,
               cd_enable: bool,
               sa_enable: bool,
               sp_enable: bool,
               sa_value: str,
               sp_value: str,
               sa_cd: str,
               sp_cd: str,
               ab_old: str) -> str:

    abn, abv, tab = step_1(ab_old)  # 切片
    new_style = step_2(style, abn, abv)  # {} 或者 ""
    new_mod = step_3(sa_enable, sp_enable, new_style)  # 替换 sa字段；+sp字段；
    new_mod2 = step_4(cd_enable,
                      sa_value,
                      sp_value,
                      sa_cd,
                      sp_cd,
                      new_mod,
                      abn)  # 替换 sa值；sa值；sa_cd；sp_cd

    return step_5(tab, new_mod2)


if __name__ == '__main__':
    examples = {
        'ex1': '''\t\t"power"\t\t\t\t"175 250 325 400"''',
        'ex2': '''\t\t"value"\t\t\t\t"1.75 2.5 3.25 4"''',
        'ex3': '''\t\t"power"\t\t\t\t"1.75 2.50 3.25"''',
        'ex4': '''\t\t"value"\t\t\t\t"10 9 8 7"''',
        'ex5': '''\t\t"AbilityCooldown"\t\t\t\t"15 14 13 12"''',
        'ex6': '''\t\t"AbilityCastPoint"\t\t\t\t"0.15"''',
        'ex7': '''\t\t"AbilityManaCost"\t\t\t\t"50 60 70 80"''',
        'ex8': '''\t\t"value"\t\t\t\t"0.3 0.3 0.3 0.3"''',
        'ex9': '''\t\t"special_bonus_facet_windrunner_tailwind"\t\t\t\t"700"'''
    }

    args = {'style': 0,
            'cd_enable': False,
            'sa_enable': True,
            'sp_enable': True,
            'sa_value': '+25%',
            'sp_value': '+100%',
            'sa_cd': '-25%',
            'sp_cd': '-50%',
            'ab_old': examples.get('ex1')}

    result = ab_replace(**args)
    print(result)
