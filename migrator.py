import os

import numpy as np
import pandas as pd
import unidecode
from sqlalchemy import create_engine

DATA_BASE_PATH: str = os.path.abspath('../data/1_datos')

engine = create_engine('sqlite:///IGAC/db.sqlite3')

FILES: list = [
    'BDL_DETALLADA/BDL_DETALLADA.csv',
    'BDP_DETALLADA/BDP_DETALLADA.csv',
    'BDP_GENERAL/BDP_GENERAL.csv',
    'COORDENADAS/COORDENADAS.csv'
]


def normalize_columns(columns):
    columns = [
        unidecode.unidecode(col) for col in columns
    ]

    columns = [
        f"_{col}" if col[0].isdigit() else col for col in columns
    ]
    return columns


for file in FILES:
    df = pd.read_csv(
        os.path.join(
            DATA_BASE_PATH,
            file
        )
    )

    name = file.split('/')[0].lower()

    df.columns = normalize_columns(df.columns)

    try:
        df.assign(
            id=np.arange(len(df)) + 1
        )[['id'] + df.columns.tolist()].to_sql(
            name,
            engine,
            index=False,
            if_exists='replace'
        )
    except ValueError:
        pass

    del df
