from app.index import App
from app.utils.cli_manager import CliManager


app = App()
cli = CliManager()

args = cli.execute()

app.execute(args.data, args.id, args.action)
