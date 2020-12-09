def get_all_inputs():
    inputs = []
    latest = input()
    while latest.strip() != '':
        inputs.append(latest.strip())
        latest = input()
    return inputs
