def calculate_tax_total(product_prices_list, tax_rate):
    total_price = 0
    for product_price in product_prices_list:
        math_price = float(product_price)
        total_price = total_price + math_price

    tax_total = "{0:.2F}".format(total_price * tax_rate)
    return tax_total
