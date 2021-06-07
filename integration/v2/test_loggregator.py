import unittest
import logging
from config_test import build_client_from_configuration

_logger = logging.getLogger(__name__)


class TestLoggregator(unittest.TestCase):
    def test_recent(self):
        client = build_client_from_configuration()
        cpt = 0
        for log_message in client.loggregator.get_recent(client.log_app_guid):
            cpt += 1
            _logger.debug("read %s", str(log_message))
        _logger.debug("read %d", cpt)
