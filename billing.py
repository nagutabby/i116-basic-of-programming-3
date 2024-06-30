def norm_cart(cart: list[tuple[str, int]]) -> list[tuple[str, int]]:
    tc: list[tuple[str, int]] = []
    flag: bool = True
    for i in range(len(cart)):
        for j in range(len(tc)):
            if (cart[i])[0] == (tc[j])[0]:
                tc[j] = ((tc[j])[0], (cart[i])[1] + (tc[j])[1])
                flag = False
                break

        if flag:
            tc = tc + [cart[i]]
        flag = True
    return tc

def make_bill_item_list(catalog: dict[str, tuple[str, int]], cart: list[tuple[str, int]]) -> list[tuple[str, int, int]]:
    bill_item_list: list[tuple[str, int, int]] = []
    for i in range(len(cart)):
        try:
            ip = catalog[(cart[i])[0]]
            bill_item_list = bill_item_list + [(ip[0], (cart[i])[1], ip[1] * (cart[i])[1])]
        except KeyError:
            return []

    return bill_item_list

def make_bill(catalog: dict[str, tuple[str, int]], cart: list[tuple[str, int]]) -> tuple[list[tuple[str, int, int]], int]:
    bill_item_list: list[tuple[str, int, int]] = make_bill_item_list(catalog, norm_cart(cart))
    ttl: int = 0
    for bill_item in bill_item_list:
        ttl = ttl + bill_item[2]
    return (bill_item_list, ttl)

def print_bill(bll: tuple[list[tuple[str, int, int]], int]) -> None:
    bill_item_list: list[tuple[str, int, int]] = bll[0]
    ttl: int = bll[1]
    print('************** Billing **************')
    print('item ordered\t#items\tsub‐total')
    for bill_item in bill_item_list:
        print(bill_item[0], '\t', bill_item[1], '\t', bill_item[2])
    print('*********** total amount ***********')
    print(f'{ttl} Japanese Yen')

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
print(make_bill_item_list(catalog, norm_cart(cart)))
print(make_bill(catalog, cart))
print_bill(make_bill(catalog, cart))
