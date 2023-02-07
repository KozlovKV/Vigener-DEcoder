from sys import argv

from vigener import VigenerCryptographer as VCrypt


def main():
    if argv.count("-j") > 0:
        json_path = argv[argv.index("-j")+1]
        # Read data from JSON
    else:
        pass  # Read data from cmd args


if __name__ == "__main__":
    main()