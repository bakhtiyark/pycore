from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    result = {}
    if num == 0:
        return {}
    else:
        for i in range(num+1):
            if i == 0:
                pass
            else:
                result.update({i: i*i})
    return result


print(generate_squares(0))
