# apply-discount-function

A small Python module that calculates the final price after applying a percentage discount. It exposes a single reusable function, `apply_discount`, which validates its inputs and returns either the discounted price or a human-readable error message.

## Contents

| File           | Description                                                     |
| -------------- | --------------------------------------------------------------- |
| `main.py`      | Defines the `apply_discount` function.                          |
| `LICENSE`      | CC0 1.0 Universal public domain dedication.                     |
| `.gitignore`   | Standard Python ignore rules for version control.               |

## Getting started

1. Make sure you have Python 3 installed.
2. Import and call the function from your own code, or test it directly:

   ```bash
   python -c "from main import apply_discount; print(apply_discount(100, 20))"
   ```

## How it works

The `apply_discount` function takes a `price` and a `discount` (both expected to
be numbers) and returns the final price after the discount is applied.

```python
def apply_discount(price, discount):

    if type(price) not in [int, float]:
        return "The price should be a number"

    if type(discount) not in [int, float]:
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price
```

### Validation rules

Before computing anything, the function checks the inputs and returns an error
string when a rule is violated:

- `price` must be an `int` or `float`, otherwise `"The price should be a number"`.
- `discount` must be an `int` or `float`, otherwise
  `"The discount should be a number"`.
- `price` must be greater than `0`, otherwise
  `"The price should be greater than 0"`.
- `discount` must be between `0` and `100` inclusive, otherwise
  `"The discount should be between 0 and 100"`.

When all checks pass, it computes `discount_amount = price * (discount / 100)`
and returns `final_price = price - discount_amount`.

### Example usage

```python
from main import apply_discount

print(apply_discount(100, 20))        # 80.0
print(apply_discount(50, 10))         # 45.0
print(apply_discount(100, 0))         # 100.0
print(apply_discount(100, 100))       # 0.0
print(apply_discount("100", 20))      # The price should be a number
print(apply_discount(100, 150))       # The discount should be between 0 and 100
```

> Note: the module itself only defines the function — it has no top-level
> `print` calls, so running `python main.py` produces no output. Import it as
> shown above to use it.

## Key concepts

- Define a function with parameters and a `return` value.
- Validate inputs with guard clauses that `return` early on bad data.
- Use `type()` and a list membership check (`in [...]`) to accept multiple
  numeric types.
- Compute a percentage-based discount and return a clean result.

## License

Released under [CC0 1.0](LICENSE), placing the work in the public domain.
