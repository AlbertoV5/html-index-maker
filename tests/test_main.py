import subprocess
import logging
import json


log = logging.getLogger(__name__)


def test_file():
    command = [
        "poetry",
        "run",
        "python",
        "-m",
        "html-index-maker",
        "-i",
        "./resources/17/ml.html",
        "-o",
        "./data.json",
        "-f",
        ".html",
    ]
    log.debug(command)
    subprocess.run(command)
    with open("./data.json", "r") as json_file:
        data = json.loads(json_file.read())
    first_header = {
        "tag": "h2",
        "id": "machine-learning",
        "text": "1. Machine Learning",
    }
    second_header = {
        "tag": "h3",
        "id": "supervised-learning",
        "text": "1.1. Supervised Learning",
    }
    assert data[0]["headers"][0] == first_header
    assert data[0]["headers"][1] == second_header


def test_directory():
    command = [
        "poetry",
        "run",
        "python",
        "-m",
        "html-index-maker",
        "-i",
        "./resources",
        "-o",
        "./data.json",
    ]
    log.debug(command)
    subprocess.run(command)
    with open("./data.json", "r") as json_file:
        data = json.loads(json_file.read())
    for file in data:
        if "/unsupervised-ml.html" in file["file"]:
            assert file["headers"][0]["id"] == "unsupervised-machine-learning"
            assert file["headers"][1]["id"] == "clustering"
        if "/ml.html" in file["file"]:
            assert file["headers"][0]["id"] == "machine-learning"
            assert file["headers"][1]["id"] == "supervised-learning"
        if "/deeplearning.html" in file["file"]:
            assert file["headers"][0]["id"] == "deep-learning"
            assert file["headers"][1]["id"] == "neural-networks"
