import logging

from .client import ActiveIQClient

__version__ = "0.0.1dev"

logging.getLogger(__name__).addHandler(logging.NullHandler())
