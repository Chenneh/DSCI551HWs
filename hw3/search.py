import sys
import mysql.connector

hostGlobal = '127.0.0.1'
userGlobal = 'dsci551'
passwordGlobal = 'Dsci-551'
databaseGlobal = 'sakila'


def connectMysql(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )


def doQuery(query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def processRes(r):
    film_id = r[0]
    film_title = r[1].title()
    actors = r[2].split(',')
    actors = list(map(lambda x: x.title(), actors))
    s = actors[0]
    for a in actors[1:]:
        s += ' and ' + a
    s += ' play'
    s += 's ' if len(actors) == 1 else ' '
    s += film_title + '(' + str(film_id) + ')'
    return s


def printRes(queryRes):
    print(str(len(queryRes)) + ' films total.' + '\n')
    for r in queryRes:
        print(processRes(r))


if __name__ == '__main__':
    connection = connectMysql(hostGlobal, userGlobal, passwordGlobal, databaseGlobal)
    query = "select FID, title, group_concat(concat(a.first_name, ' ', a.last_name)) as actor_list " \
            "from nicer_but_slower_film_list nb " \
            "inner join film_actor fa on fa.film_id=nb.FID " \
            "inner join actor a on a.actor_id=fa.actor_id " \
            "where a.first_name='Temple' || a.last_name='Temple' " \
            "group by title " \
            "order by FID asc;"
    queryRes = doQuery(query)

    # processRes(queryRes[9])
    printRes(queryRes)
