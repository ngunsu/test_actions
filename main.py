import click


@click.command()
@click.argument('name')
def main(name):
    print(name)


if __name__ == "__main__":
    main()
