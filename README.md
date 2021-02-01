# UX_Interview_Analysis

**TL;DR An almost universal user experience interview transcribe analysis tool.**

This is a tool created to analyze the interview transcribes to improve user
experience in products.

- [UX_Interview_Analysis](#ux-interview-analysis)
  * [Getting Started](#getting-started)
    + [Prerequisite](#prerequisite)
      - [System and Python](#system-and-python)
      - [Dependency Installation](#dependency-installation)
    + [Running the Tests](#running-the-tests)
    + [Deployment](#deployment)
    + [Running the Program](#running-the-program)
- [License](#license)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Getting Started

### Prerequisite

#### System and Python

This application was built on a Linux system, the Python version was 3.7.9.
[Pyenv](https://github.com/pyenv/pyenv) is recommended for Python version management.
Here is a good [tutorial](https://realpython.com/intro-to-pyenv/) on how to install
Pyenv on your system.

[Pipenv](https://github.com/pypa/pipenv) was used to manage the Python dependencies,
here is a good [tutorial](https://realpython.com/pipenv-guide/) on how to install
and use Pipenv.

#### Dependency Installation

To install the dependencies, use `pipenv install` to install from Pipfile. If you
want to install by importing the `requirement.txt`, use
`pipenv install -r path/to/requirements.txt` to install.

### Running the Tests

Use `pipenv run test` to test the application. The test files are under `test/`
directory. The bash script is `scripts/test.sh`.

### Deployment

After setting up the system, some modules need to be installed.

### Running the Program

To run the program, use `pipenv run run` to execute `run.sh` from `scripts` directory.
Before running the program, you should specify the path of the directory that contains
text files to be analyzed. The ms-dos file is the only format supported at the moment.
The path should be put in `"dir_path"` at `scripts/config.json`.

If prompted
`Error: the command ./scripts/run.sh (from run) could not be found within PATH.`,
 you should use `chmod +x run.sh` to make the file executable.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE)
file for details.
