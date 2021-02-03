from text_import import intermediate_file, retain_main_body
import os
import json
import shutil
import argparse


def check_existance(any_path):
    """Check if directory or file exists."""
    # Return a boolean value
    return os.path.exists(any_path)


def tidy_repo(intermediate):
    """Clear extra temp files and directories before running analysis."""
    shutil.rmtree(intermediate, ignore_errors=True)


if __name__ == "__main__":
    # Parser for configrition
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-c", "--conf", required=True, help="path to the JSON configuration file"
    )
    args = vars(ap.parse_args())
    conf = json.load(open(args["conf"]))

    # Use with caution, the objact will be removed without confirmation.
    tidy_repo("intermediate")
    os.mkdir("intermediate")

    # Extract texts from user-specified directory to intermediate.
    if check_existance(conf["dir_path"]):
        intermediate_file(conf["dir_path"])
    # Dump everything else except the main body of the interview.
    retain_main_body(
        "intermediate/intermediate_file",
        conf["start_tag"],
        conf["end_tag"],
        conf["question_mark"],
    )
    # TODO: Pre-process
