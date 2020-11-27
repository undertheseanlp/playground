import logging
import mmap

logger = logging.getLogger("underthesea")


def load_big_file(f: str) -> mmap.mmap:
    r"""
    Workaround for loading a big pickle file. Files over 2GB cause pickle errors on certin Mac and Windows distributions.
    Source: flairNLP
    """
    logger.info(f"loading file {f}")
    with open(f, "rb") as f_in:
        # mmap seems to be much more memory efficient
        bf = mmap.mmap(f_in.fileno(), 0, access=mmap.ACCESS_READ)
        f_in.close()
    return bf
