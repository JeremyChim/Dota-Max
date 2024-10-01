def tab_up(old_str: str):
    ls = []
    for i in old_str.split('\n'):
        i = '\t' + i
        ls.append(i)
    new_str = '\n'.join(ls)
    return new_str


def tab_down(old_str: str):
    ls = []
    for i in old_str.split('\n'):
        if len(i) != 0 and i[0] == '\t':
            ls.append(i[1:])
        else:
            ls.append(i)
    new_str = '\n'.join(ls)
    return new_str


if __name__ == '__main__':
    ex = '''\t"power"
\t{
\t\t"value"							"175 250 325 400"
\t\t"special_bonus_shard"			"+50%"
\t\t"special_bonus_scepter"			"+100%"
\t}
'''
    print(tab_up(ex))
    print(tab_down(ex))
