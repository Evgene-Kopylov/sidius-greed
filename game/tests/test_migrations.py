import os

# import pytest
import unittest

from pathlib import Path

from alembic.config import Config
from alembic import command

ini_path = Path().absolute().__str__() + r"\alembic_test.ini"
test_db_path = Path().absolute().__str__() + r"\test_db.sqlite"
alembic_cfg = Config(ini_path)


class TestAlembicMigrations(unittest.TestCase):
    def tearDown(self) -> None:
        os.remove(test_db_path)

    def test_last_revision(self):
        command.upgrade(alembic_cfg, "head")
        command.downgrade(alembic_cfg, '-1')
        command.upgrade(alembic_cfg, "head")
