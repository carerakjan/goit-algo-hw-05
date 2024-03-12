from decimal import Decimal
from typing import Generator, Any, Callable


def generator_numbers(text: str):
    for word in text.split():
        if word.replace('.', '', 1).isdigit():
            yield Decimal(word).quantize(Decimal('0.00'))


def sum_profit(txt: str, gen_func: Callable[[str], Generator[Decimal, Any, None]]):
    return sum(gen_func(txt))


def main():
    text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений "
            "додатковими надходженнями 27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()
