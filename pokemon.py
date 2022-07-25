from utils import calculate_multiplier


def main():
    print('Insert attack type: ')
    attack_type = input()
    print('Insert pokemon types delimited by single space: ')
    pokemon_types = list(input().split(' '))

    print(calculate_multiplier(attack_type, pokemon_types))


if __name__ == "__main__":
    main()
