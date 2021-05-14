import db
from log import log


class User():

    def create(conf, engine):
        sql = f"CREATE USER '{conf['name']}'@'{conf['host']}' IDENTIFIED WITH mysql_native_password BY '{conf['password']}'"
        result = engine.execute(sql)


    def exists(conf, engine):
        sql = f"SELECT user, host FROM mysql.user WHERE user='{conf['name']}' AND host='{conf['host']}'"
        #log(engine.execute(sql))
        result = engine.execute(sql)
        result_set = result.fetchall()
        return result_set

    def drop(conf, engine):
        sql = f"DROP USER '{conf['name']}'@'{conf['host']}' "
        result = engine.execute(sql)

    def grant_roles(conf, engine):
        for _role in conf['roles']:
          sql = f"GRANT {_role['role']} TO '{conf['name']}'@'{conf['host']}'"
          result = engine.execute(sql)
        sql = f"SET DEFAULT ROLE {conf['default_role']} TO '{conf['name']}'@'{conf['host']}'"
        result = engine.execute(sql)

    def show_grants(conf, engine):
        sql = f"SHOW GRANTS FOR '{conf['name']}'@'{conf['host']}'"
        result = engine.execute(sql)
        result_set = result.fetchall()
        return result_set

    def revoke(src, engine):
        for _src in src:
          old_sql=_src[0]
          #log(old_sql)
          if not ('USAGE') in old_sql:
            new_sql = old_sql.replace("GRANT ", "REVOKE ")
            new_sql = new_sql.replace(" TO ", " FROM ")
            engine.execute(new_sql)

    def grant_permissions(conf, engine):
        for _grant in conf['grants']:
          if _grant['grant']['db'] == '*' :
            sql = f"GRANT {', '.join(_grant['grant']['permissions'])} ON {_grant['grant']['db']}.* TO '{conf['name']}'@'{conf['host']}' "
          else :
            sql = f"GRANT {', '.join(_grant['grant']['permissions'])} ON `{_grant['grant']['db']}`.* TO '{conf['name']}'@'{conf['host']}' "
          engine.execute(sql)


    def passwd(conf, engine):
        sql = f"ALTER USER '{conf['name']}'@'{conf['host']}' IDENTIFIED WITH mysql_native_password AS '{conf['password']}'"
        result = engine.execute(sql)
