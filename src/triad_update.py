def triad_update(triads_update_dct: dict, triad: str, new_value: str) -> dict:
    if triad not in triads_update_dct.keys():
        triads_update_dct[triad] = {'zero': 0, 'one': 0}

    if new_value == '0':
        triads_update_dct[triad]['zero'] += 1
    else:
        triads_update_dct[triad]['one'] += 1

    return triads_update_dct


def triads_dct_update(current: dict, update: dict) -> dict:
    for update_key, values in update.items():
        current[update_key]['zero'] += values['zero']
        current[update_key]['one'] += values['one']

    return current
