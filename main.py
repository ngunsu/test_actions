import click


@click.command()
@click.argument('name')
def main(name):
    print(name)


def validate_rut(rut):
    return True


if __name__ == "__main__":
    main()
