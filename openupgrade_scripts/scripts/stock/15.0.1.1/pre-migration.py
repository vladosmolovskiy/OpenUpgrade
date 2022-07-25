from openupgradelib import openupgrade


def _create_column_for_avoiding_automatic_computing(env):
    openupgrade.logged_query(
        env.cr,
        """
            ALTER TABLE stock_move
                ADD COLUMN IF NOT EXISTS reservation_date date;
        """,
    )


def _fill_stock_quant_package_name_if_null(env):
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE stock_quant_package
            SET name = 'Unknown Pack'
