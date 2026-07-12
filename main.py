def apply_discount(price, discount):

    if type(price) not in [int, float]:
        return "The price should be a number"

    if type(discount) not in [int, float]:
        return "The discount should be a number"
