from multiprocessing import cpu_count
from psycogreen.gevent import patch_psycopg


def post_fork(server, worker):
    patch_psycopg()
    worker.log.debug("Made Psycopg2 Green")


worker_class = 'gevent'
workers = 2 * cpu_count() + 1
