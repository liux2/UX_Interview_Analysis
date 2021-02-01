# UX_Interview_Analysis

**TL;DR An almost universal user experience interview transcribe analysis tool.**

This is a tool created to analyze the interview transcribes to improve user
experience in products.

## Getting Started

### Prerequisite

#### System and Python

This application was built on Linux system, the Python version was 3.7.9.
[Pyenv](https://github.com/pyenv/pyenv) is recommended for Python version management.
Here is a good [tutorial](https://realpython.com/intro-to-pyenv/) on how to install
Pyenv on your system.

[Pipenv](https://github.com/pypa/pipenv) was used to manage the Python dependencies,
here is a good [tutorial](https://realpython.com/pipenv-guide/) on how to install
and use Pipenv.

#### Dependency Installation

To install the dependencies, use `pipenv install` to install from Pipfile. If you
want to install by importing the `requirement.txt`, use
`pipenv install -r path/to/requirements. txt` to install.

### Running the Tests

Use `pipenv run test` to test the application. The test files are under `test/`
directory. The bash script is `scripts/test.sh`.

### Deployment

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE)
file for details.
