# Contributing

Contributions are welcome. Here's how:

## Development

```bash
git clone https://github.com/kuroko9021/technocore-id.git
cd technocore-id
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Testing

```bash
python technocore_id.py --version
python technocore_id.py init  # create test identity
python technocore_id.py did   # verify DID generation
```

## Code Style

- Keep it minimal
- No external dependencies beyond `cryptography`
- Python 3.11+ only
- Type hints encouraged

## Pull Requests

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## Issues

Found a bug? Have an idea? Open an issue.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
