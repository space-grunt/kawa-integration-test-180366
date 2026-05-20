import logging

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool()
def execute_new_decorator():
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Runnable test ok')
