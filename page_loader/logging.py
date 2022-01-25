import logging
import sys


def configure_logger():
    # root logger
    # root = logging.getLogger()
    # root.setLevel(logging.DEBUG)
    # formatter = logging.Formatter(
    #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # )
    #
    # # STDOUT Stream Handler (INFO)
    # stream_handler = logging.StreamHandler(sys.stdout)
    # stream_handler.setLevel(logging.INFO)
    # stream_handler.setFormatter(formatter)
    #
    # # STDERR Stream Handler (WARNING, ERROR, CRITICAL)
    # stream_err_handler = logging.StreamHandler()
    # stream_err_handler.setLevel(logging.WARNING)
    # stream_err_handler.setFormatter(formatter)
    #
    # # Adding handlers to root logger.
    # root.addHandler(stream_handler)
    # root.addHandler(stream_err_handler)

    # logger = logging.getLogger(__name__)
    # formatter = logging.Formatter('%(lineno)d:%(filename)s:%(message)s')
    # stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(formatter)
    # stream_handler.setLevel(logging.DEBUG)
    # user_handler = logging.StreamHandler(stream=sys.stdout)
    # user_handler.setLevel(logging.INFO)
    # logger.addHandler(stream_handler)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        )
    root = logging.getLogger(__name__)
    hdlr = root.handlers[0]
    fmt = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    hdlr.setFormatter(fmt)
