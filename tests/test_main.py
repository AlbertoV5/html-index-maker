import subprocess
import logging

log = logging.getLogger(__name__)


def test_main():
    command = ["poetry", "run", "python", "-m", "html-index-maker", "Bob"]
    out = subprocess.check_output(command)
    assert out.decode("utf-8") == "Hello Bob\n"
    log.debug(out)
