def step_1(ab: str) -> tuple:
    ls = ab.split('"')
    abn, abv, tab = ls[1], ls[3], ls[0]  # name, value, tab
    return abn, abv, tab


def step_2(abn: str, abv: str, tab: str) -> str:
    mod_1 = '''__tab__"ab_name"__tab__\t\t\t\t\t"ab_value"
__tab__"special_bonus_shard"__tab__\t"sa_value"
__tab__"special_bonus_scepter"__tab__\t"sp_value"   
'''

    mod_2 = '''__tab__"ab_name"
__tab__{
__tab__\t"value"__tab__\t\t\t\t\t"ab_value"
__tab__\t"special_bonus_shard"__tab__\t"sa_value"
__tab__\t"special_bonus_scepter"__tab__\t"sp_value"
__tab__}    
'''

    match abn:
        case 'value':
            res = mod_1.replace('ab_name', abn) \
                .replace('ab_value', abv) \
                .replace('__tab__', tab) \
                .replace('sa_value', '+50%') \
                .replace('sp_value', '+100%')

        case 'AbilityCooldown' | 'AbilityCastPoint' | 'AbilityManaCost':
            res = mod_2.replace('ab_name', abn) \
                .replace('ab_value', abv) \
                .replace('__tab__', tab) \
                .replace('sa_value', '-50%') \
                .replace('sp_value', '-50%')

        case _:
            res = mod_2.replace('ab_name', abn) \
                .replace('ab_value', abv) \
                .replace('__tab__', tab) \
                .replace('sa_value', '+50%') \
                .replace('sp_value', '+100%')

    return res


def ab_replace(ab_old: str) -> str:
    return step_2(*step_1(ab_old))


if __name__ == '__main__':
    ex = '''\t\t"power"\t\t\t\t"175 250 325 400"'''
    # ex = '''\t\t"value"\t\t\t\t"1.75 2.5 3.25 4"'''
    # ex = '''\t\t"power"\t\t\t\t"1.75 2.50 3.25"'''
    # ex = '''\t\t"value"\t\t\t\t"10 9 8 7"'''
    # ex = '''\t\t"AbilityCooldown"\t\t\t\t"15 14 13 12"'''
    # ex = '''\t\t"AbilityCastPoint"\t\t\t\t"0.15"'''
    # ex = '''\t\t"AbilityManaCost"\t\t\t\t"50 60 70 80"'''
    # ex = '''\t\t"value"\t\t\t\t"0.3 0.3 0.3 0.3"'''
    # ex = '''\t\t"special_bonus_facet_windrunner_tailwind"\t\t\t\t"700"'''

    print(ab_replace(ex))
