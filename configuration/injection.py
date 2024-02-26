from dependency_injector import providers, containers

from source import apis
from configuration.configuration import data_base_config
from source.database.database_helpers import Database
from source.queries.sales_queries import SalesCrud
from source.services.sales_service import SaleService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[apis])

    db = providers.Singleton(
        Database,
        db_url=f"postgresql://{data_base_config.DB_USER}:{data_base_config.DB_PASSWORD}@{data_base_config.DB_HOST}:{data_base_config.DB_PORT}/{data_base_config.DB_NAME}"
    )
    sales_crud = providers.Factory(
        SalesCrud,
        session_factory=db.provided.session
    )

    sales_service = providers.Factory(
        SaleService,
        sale_crude=sales_crud
    )
