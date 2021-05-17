from simpleurdf import __version__
from simpleurdf import UrdfParser


def test_version():
    assert __version__ == "0.1.113"


def test_loading_file():
    instance = UrdfParser()
    # instance.loadURDFFile("test")
