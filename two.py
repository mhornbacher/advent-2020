from lib.inputs import get_all_inputs
import re

def follows_policy_1(min, max, letter, password):
    count = 0
    for char in password:
        if char == letter:
            count += 1
    return count >= min and count <= max

def follows_policy_2(pos1, pos2, letter, password):
    match1 = password[pos1 - 1] == letter
    match2 = password[pos2 - 1] == letter
    return match1 != match2


if __name__ == "__main__":
    print('Enter passwords:')
    inputs = get_all_inputs()
    # Pattern for input. min-max letter: password
    regex = re.compile('(\d+)-(\d+) (.): (.+)')
    inputs = [regex.match(x) for x in inputs]

    policy_1 = [
        x.group(4) for x in inputs
        if follows_policy_1(int(x.group(1)), int(x.group(2)), x.group(3), x.group(4))
    ]

    policy_2 = [
        x.group(4) for x in inputs
        if follows_policy_2(int(x.group(1)), int(x.group(2)), x.group(3), x.group(4))
    ]

    print(len(policy_1))
    print(len(policy_2))