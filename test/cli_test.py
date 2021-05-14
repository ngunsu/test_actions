from click.testing import CliRunner
from main import main


def test_app_cli():
    runner = CliRunner()
    result = runner.invoke(main, ['Cristhian'])
    print(result)
    assert result.exit_code == 0
