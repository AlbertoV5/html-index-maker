from argparse import ArgumentParser, Namespace


def main(argv: Namespace):
    print("Hello", argv.name)


if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("name")
    main(args.parse_args())
