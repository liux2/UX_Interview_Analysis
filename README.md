# UX Interview Analysis

**TL;DR An almost universal user experience interview transcribe analysis tool.**

This is a tool created to analyze the interview transcribes to improve user
experience in products.

- [UX Interview Analysis](#ux-interview-analysis)
  * [Getting Started](#getting-started)
    + [Prerequisite](#prerequisite)
      - [System and Python](#system-and-python)
      - [Dependency Installation](#dependency-installation)
      - [Interview Document Format](#interview-document-format)
    + [Running the Tests](#running-the-tests)
  * [Deployment](#deployment)
    + [Parameters](#parameters)
  * [Running the Program](#running-the-program)
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

#### Interview Document Format

The text used in this project has the format of:

```
TEXT # Settings, such as location and names.

START-TAG # The label (M) states the start of the interview.

TEXT # The main body of the interview, which contains questions and answers.
     # Has the format of Q: texts./nA: texts.

END-TAG # The label (numbers) states the end of the interview.
```

Please check out [Parameters](#parameters) for how to set your own tags.

### Running the Tests

Use `pipenv run test` to test the application. The test files are under `test/`
directory. The bash script is `scripts/test.sh`.

## Deployment

After setting up the system, some modules need to be installed.

### Parameters

**1. `"dir_path"`:** Before running the program, you should specify the path of the
directory that contains text files to be analyzed. The MS-DOC file is the only
format supported at the moment. The path should be put in `"dir_path"` at
`scripts/config.json`.

**2. `"start_tag"`:** The start tag indicates the start of the main text body. **You
must have a start tag for each piece of interview.**

**3. `"end_tag"`:** The end tag indicates the end of the main text body. **You must
have an end tag for each piece of interview.**

*The documents will be combined as a bag of words. A bag of words may contain
multiple interview pieces. That being said, the number of start tags should match
the number of end tags.*

**4. `"question_mark"`:** The question marks are the header of each question. In
the case of this project, "M" is the header of each question. As a sample shows:
`M: How is the weather today?`. The datatype of this field in JSON is a list. You
can put multiple marks in square parenthesis. Don't forget to separate them with a comma.
There is no need to identify the answer marks because the complement of the question
marks are answer mark.

## Running the Program

To run the program, use `pipenv run run` to execute `run.sh` from `scripts`
directory. If prompted
`Error: the command ./scripts/run.sh (from run) could not be found within PATH.`,
 you should use `chmod +x run.sh` to make the file executable.

 Note that the transcribe used are in Chinese, so the punctuation used in the
 process are mostly fullwidth.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE)
file for details.
