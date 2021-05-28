"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
import unittest
from itertools import (
    starmap,
)
from pathlib import (
    Path,
)
from typing import (
    Any,
    NoReturn,
)
from uuid import (
    uuid4,
)

import aiopg

from .configuration import (
    MinosConfig,
)


class PostgresAsyncTestCase(unittest.IsolatedAsyncioTestCase):
    CONFIG_FILE_PATH: Path

    def setUp(self) -> None:
        self._uuid = uuid4()
        self._config = MinosConfig(self.CONFIG_FILE_PATH)

        self._meta_repository_db = self._config.repository._asdict()

        self._meta_events_queue_db = self._config.events.queue._asdict()
        self._meta_events_queue_db.pop("records")
        self._meta_events_queue_db.pop("retry")

        self._meta_commands_queue_db = self._config.commands.queue._asdict()
        self._meta_commands_queue_db.pop("records")
        self._meta_commands_queue_db.pop("retry")

        self._meta_saga_queue_db = self._config.saga.queue._asdict()
        self._meta_saga_queue_db.pop("records")
        self._meta_saga_queue_db.pop("retry")

        self._meta_snapshot_db = self._config.snapshot._asdict()

        self._test_db = {"database": f"test_db_{self._uuid.hex}", "user": f"test_user_{self._uuid.hex}"}

        self.repository_db = self._meta_repository_db | self._test_db
        self.events_queue_db = self._meta_events_queue_db | self._test_db
        self.commands_queue_db = self._meta_commands_queue_db | self._test_db
        self.saga_queue_db = self._meta_saga_queue_db | self._test_db
        self.snapshot_db = self._meta_snapshot_db | self._test_db

        self.config = MinosConfig(
            self.CONFIG_FILE_PATH,
            repository_database=self.repository_db["database"],
            repository_user=self.repository_db["user"],
            events_queue_database=self.events_queue_db["database"],
            events_queue_user=self.events_queue_db["user"],
            commands_queue_database=self.commands_queue_db["database"],
            commands_queue_user=self.commands_queue_db["user"],
            saga_queue_database=self.saga_queue_db["database"],
            saga_queue_user=self.saga_queue_db["user"],
            snapshot_database=self.snapshot_db["database"],
            snapshot_user=self.snapshot_db["user"],
        )

    async def asyncSetUp(self):
        pairs = self._drop_duplicates(
            [
                (self._meta_repository_db, self.repository_db),
                (self._meta_events_queue_db, self.events_queue_db),
                (self._meta_commands_queue_db, self.commands_queue_db),
                (self._meta_saga_queue_db, self.saga_queue_db),
                (self._meta_snapshot_db, self.snapshot_db),
            ]
        )
        for meta, test in pairs:
            await self._setup_database(dict(meta), dict(test))

    @staticmethod
    async def _setup_database(meta: dict[str, Any], test: dict[str, Any]) -> NoReturn:
        async with aiopg.connect(**meta) as connection:
            async with connection.cursor() as cursor:
                template = "DROP DATABASE IF EXISTS {database};"
                await cursor.execute(template.format(**test))

                template = "DROP ROLE IF EXISTS {user};"
                await cursor.execute(template.format(**test))

                template = "CREATE ROLE {user} WITH SUPERUSER CREATEDB LOGIN ENCRYPTED PASSWORD {password!r};"
                await cursor.execute(template.format(**test))

                template = "CREATE DATABASE {database} WITH OWNER = {user};"
                await cursor.execute(template.format(**test))

    async def asyncTearDown(self):
        pairs = self._drop_duplicates(
            [
                (self._meta_repository_db, self.repository_db),
                (self._meta_events_queue_db, self.events_queue_db),
                (self._meta_commands_queue_db, self.commands_queue_db),
                (self._meta_saga_queue_db, self.saga_queue_db),
            ]
        )

        for meta, test in pairs:
            await self._teardown_database(meta, test)

    @staticmethod
    def _drop_duplicates(items: list[(dict, dict)]):
        items = starmap(lambda a, b: (tuple(a.items()), tuple(b.items())), items)
        items = set(items)
        items = starmap(lambda a, b: (dict(a), dict(b)), items)
        items = list(items)
        return items

    @staticmethod
    async def _teardown_database(meta: dict[str, Any], test: dict[str, Any]) -> NoReturn:
        async with aiopg.connect(**meta) as connection:
            async with connection.cursor() as cursor:
                template = "DROP DATABASE IF EXISTS {database}"
                await cursor.execute(template.format(**test))
