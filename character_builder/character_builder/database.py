"""Django database settings."""
import os

from django.conf import settings
from django.contrib.postgres.fields.jsonb import KeyTextTransform
from django.contrib.postgres.fields.jsonb import KeyTransform
from django.db.models import DecimalField
from django.db.models.aggregates import Func

from .env import ENVIRONMENT

# pylint: disable=invalid-name
engines = {
    "sqlite": "django.db.backends.sqlite3",
    "postgresql": "django.db.backends.postgresql",
    "mysql": "django.db.backends.mysql",
}


def _cert_config(db_config, database_cert):
    """Add certificate configuration as needed."""
    if database_cert:
        cert_file = "/etc/ssl/certs/server.pem"
        db_options = {"OPTIONS": {"sslmode": "verify-full", "sslrootcert": cert_file}}
        db_config.update(db_options)
    return db_config


def config():
    """Database config."""
    service_name = ENVIRONMENT.get_value("DATABASE_SERVICE_NAME", default="").upper().replace("-", "_")
    if service_name:
        engine = engines.get(ENVIRONMENT.get_value("DATABASE_ENGINE"), engines["postgresql"])
    else:
        engine = engines["postgresql"]

    name = ENVIRONMENT.get_value("DATABASE_NAME", default="postgres")

    if not name and engine == engines["sqlite"]:
        name = os.path.join(settings.BASE_DIR, "db.sqlite3")

    db_config = {
        "ENGINE": engine,
        "NAME": name,
        "USER": ENVIRONMENT.get_value("DATABASE_USER", default="postgres"),
        "PASSWORD": ENVIRONMENT.get_value("DATABASE_PASSWORD", default="postgres"),
        "HOST": ENVIRONMENT.get_value(f"{service_name}_SERVICE_HOST", default="localhost"),
        "PORT": ENVIRONMENT.get_value(f"{service_name}_SERVICE_PORT", default=15432),
    }

    database_cert = ENVIRONMENT.get_value("DATABASE_SERVICE_CERT", default=None)
    return _cert_config(db_config, database_cert)

