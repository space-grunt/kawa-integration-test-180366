import logging
import datetime

from kywy.client.kawa_client import KawaClient
from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(outputs={
    'key': str,
    'business_date': datetime.date,
    'product_master_id': float,
    'price': float,
    'abs_quantity': float
})
def execute_new_decorator(kawa: KawaClient, data_preview=False, append=False):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Python etl example with computation')
    columns = [
        kawa.col('key').first(),
        kawa.col('business_date').first(),
        kawa.col('product_master_id').first(),
        kawa.col('price').first(),
        kawa.col('abs_quantity').sum(),
    ]

    # in case of data data_preview or append, we only load the last three days
    if data_preview or append:
        from_ = datetime.date.today() - datetime.timedelta(days=4)
        to_ = datetime.date.today()
        script_logger.info(f'Incremental or preview, loading data between : {from_} / {to_}')
        date_filter = (kawa
                       .col('business_date')
                       .date_range(from_inclusive=from_,
                                       to_inclusive=to_)
                       )

        return (kawa.sheet(sheet_id='2994')
                .select(*columns)
                .group_by('key')
                .filter(date_filter)
                .limit(-1)
                .compute())

    script_logger.info(f'Full load')
    return (kawa.sheet(sheet_id='2994')
            .select(*columns)
            .group_by('key')
            .limit(-1)
            .compute())
