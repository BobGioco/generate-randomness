def balance_budget(correct: int, total: int) -> int:
    return correct - (total - correct)


def check_binary_string(s: str) -> bool:
    for character in s:
        if character != '0' and character != '1':
            return False
    return True
