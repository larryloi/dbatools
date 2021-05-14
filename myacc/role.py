import db
from log import log

class Role():

    def create(conf, engine):
        sql = f"CREATE ROLE '{conf['name']}'"
        result = engine.execute(sql)
