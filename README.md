# my-todoist

This repository contains scripts to automate and manage my Todoist tasks.

## Setup

1. Copy `.env.example` to `.env` and add the API token
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

### Nix

You can use the provided `flake.nix` to get a reproducible Python development environment:

```sh
nix develop
```

This will provide Python, pip, and all required tools for local development.

## Automation

Automation is handled by GitHub Actions, which runs the scripts on an hourly schedule.

## License

This project is licensed under the terms of the GPL v3.0 license. Check [LICENSE](LICENSE) for details.
