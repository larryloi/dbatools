from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

class Db():

    def dbconn(conf, sql_trace=False):
        host=str(conf['host'])
        username=str(conf['username'])
        password=str(conf['password'])
        charset=str(conf['charset'])
        port=str(conf['port'])
        db_name=str(conf['db_name'])
        #conn = create_engine('mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_name + '?auth_plugin=mysql_native_password', echo=False).connect()
        engine = create_engine('mysql+mysqlconnector://' + username + ':' + password + '@' + host + ':' + port  +'/' + db_name + '?auth_plugin=mysql_native_password', echo=sql_trace, connect_args={'use_pure': True})
        return engine
    #    SysConfig = Base.classes.sys_config
    #    rows = session.query(SysConfig).all()
    #    for row in rows:
    #      log(row.value)

