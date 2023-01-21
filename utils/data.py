import pandas as pd
import numpy as np
from clickhouse_driver import Client

from config import SERVER, CONFIG


def get_default_data() -> tuple[pd.DataFrame, pd.DataFrame, list[int], list[int], str]:
    quotes_df = pd.DataFrame(
        {
            "block_number": np.arange(11000000, 16400000, 1000),
            "native_quote": np.ones_like(np.arange(11000000, 16400000, 1000)),
        }
    )

    pnl_df = pd.DataFrame(
        {
            "block_number": np.arange(11000000, 16400000, 1000),
            "pnl": np.ones_like(np.arange(11000000, 16400000, 1000)),
        }
    )

    return quotes_df, pnl_df, [], [], "NOT DEFINED"


def get_data(
    token_address: str,
    wallet_address: str,
) -> tuple[pd.DataFrame, pd.DataFrame, list[int], list[int], str]:
    """
    The function extracts data from clickhouse database and constructs
    1. pd.DataFrame `quotes_df`
    2. pd.DataFrame `pnl_df`
    3. list[int] of block numbers of all `in_transfers` to `wallet_address`
    4. list[int] of block numbers of all `out_transfers` from `wallet_address`
    5. token symbol of `token_address`

    What you should do is to implement the function.

    You need to extract data from clickhouse database via sql queries
    ```
    client.execute(f"SELECT ... FROM ... WHERE ... LIMIT {CONFIG.limit_rows}")
    ```
    It is reasonable to LIMIT your sql query with predefined number of rows to prevent both
    server's and your PC's overload.

    When selecting from quotes table use the following query
    ```
    client.execute(f"SELECT ... FROM quotes WHERE block_number % 100 = 0 LIMIT {CONFIG.limit_rows}")
    ```
    and use the data for `quotes_df` as is. For pnl calculation you can assume that the quote between
    block_from, block_to where block_from and block_to are divisible by 100 equals to quote as of block_from.

    Args:
        token_address (str): token address
        wallet_address (str): wallet_address

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, list[int], list[int], str]:
            tuple(quotes_df, pnl_df, in_transers, out_transfers, token_symbol)
    """
    SERVER.start()
    client = Client.from_url(
        f"clickhouse://localhost:{SERVER.local_bind_port}/ethereum"
    )

    # YOUR CODE GOES HERE

    # quotes_df = ...
    # pnl_df = ...
    # in_transers = ...
    # out_transfers = ...
    # token_symbol = ...

    # Uncomment the line below and delete `return get_default_data()`
    # return quotes_df, pnl_df, in_transers, out_transfers, token_symbol

    # Do not delete the line
    SERVER.close()

    return get_default_data()
