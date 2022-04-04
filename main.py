import click
from rut_chile import rut_chile


@click.command()
@click.argument('name')
def main(name):
    print(name)


def validate_rut(rut):
    return rut_chile.is_valid_rut(rut)


if __name__ == "__main__":
    main()
