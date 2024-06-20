def norm_cart(cart: list[tuple[str, int]]) -> list[tuple[str, int]]:
    tc: list[tuple[str, int]] = []
    flg: bool = True
    for i in range(len(cart)):
        for j in range(len(tc)):
            if (cart[i])[0] == (tc[j])[0]:
                tc[j] = ((tc[j])[0], (cart[i])[1] + (tc[j])[1])
                flg = False
                break

        if flg:
            tc = tc + [cart[i]]
        flg = True
    return tc

def make_bill_item_list(catalog: dict[str, tuple[str, int]], cart: list[tuple[str, int]]) -> list[tuple[str, int, int]]:
    bill: list[tuple[str, int, int]] = []
    for i in range(len(cart)):
        try:
            ip = catalog[(cart[i])[0]]
            bill = bill + [(ip[0], (cart[i])[1], ip[1] * (cart[i])[1])]
        except KeyError:
            return []

    return bill

def make_bill(catalog: dict[str, tuple[str, int]], cart: list[tuple[str, int]]) -> tuple[list[tuple[str, int, int]], int]:
    bill: list[tuple[str, int, int]] = make_bill_item_list(catalog, norm_cart(cart))
    ttl: int = 0
    for bi in bill:
        ttl = ttl + bi[2]
    return (bill, ttl)

def print_bill(bll: tuple[list[tuple[str, int, int]], int]) -> None:
    bil: list[tuple[str, int, int]] = bll[0]
    ttl: int = bll[1]
    print('************** Billing **************')
    print('item ordered\t#items\tsub‐total')
    for bi in bil:
        print(bi[0], '\t', bi[1], '\t', bi[2])
    print('*********** total amount ***********')
    print(ttl, ' Japanese Yen')

catalog: dict[str, tuple[str, int]] = {
    'mp': ('MacPro', 5000000),
    'im': ('iMac', 400000),
    'mbp': ('MacBook Pro', 500000),
    'am': ('AirMac', 200000)
}

cart: list[tuple[str, int]] = [
    ('am', 4),
    ('mbp', 2),
    ('mp', 1),
    ('am', 3),
    ('mp', 1)
]

print(norm_cart(cart))
print(make_bill_item_list(catalog,norm_cart(cart)))
print(make_bill(catalog, cart))
print_bill(make_bill(catalog, cart))
