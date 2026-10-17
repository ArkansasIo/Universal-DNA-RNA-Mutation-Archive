"""Environment-backed configuration for local and container deployments."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    """Runtime settings; secrets are read from environment variables only."""

    archive_path: str = "data/examples/variants.json"
    host: str = "127.0.0.1"
    port: int = 8080
    mysql_host: str = "127.0.0.1"
    mysql_port: int = 3306
    mysql_database: str = "mutation_archive"
    mysql_user: str = "mutation_archive"
    mysql_password: str | None = None

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            archive_path=os.getenv("MUTATION_ARCHIVE_PATH", cls.archive_path),
            host=os.getenv("MUTATION_ARCHIVE_HOST", cls.host),
            port=int(os.getenv("MUTATION_ARCHIVE_PORT", str(cls.port))),
            mysql_host=os.getenv("MYSQL_HOST", cls.mysql_host),
            mysql_port=int(os.getenv("MYSQL_PORT", str(cls.mysql_port))),
            mysql_database=os.getenv("MYSQL_DATABASE", cls.mysql_database),
            mysql_user=os.getenv("MYSQL_USER", cls.mysql_user),
            mysql_password=os.getenv("MYSQL_PASSWORD"),
        )
