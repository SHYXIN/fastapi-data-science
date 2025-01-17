from loguru import logger

def is_even(n) -> bool:
    logger.debug("Check if {n} is even", n=n)
    if not isinstance(n, int):
        logger.error("{n} is not an integer", n=n)
        raise TypeError()
    return n % 2 == 0

if __name__ == "__main__":
    is_even(2)
    is_even("hello")
