from dependency_injector import providers, containers

import source
from configuration.configuration import data_base_config
from source.database.database_helpers import Database


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[source])

    db = providers.Singleton(
        Database,
        db_url=f"postgresql://{data_base_config.DB_USER}:{data_base_config.DB_PASSWORD}@{data_base_config.DB_HOST}:{data_base_config.DB_PORT}/{data_base_config.DB_NAME}"
    )
