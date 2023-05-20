# Python Clean Architecture
Criando um projeto python usando clean architecture


# Criando o Banco
> from src.infra.config import *

> db_conn = DBConnectionHandler()

> engine = db_conn.get_engine()

> Base.metadata.create_all(engine)
