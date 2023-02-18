import sqlite3

conn = sqlite3.connect("db.sqlite3")
with conn:
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "links" (
                "id"	INTEGER NOT NULL UNIQUE,
                "long"	TEXT NOT NULL CHECK(length(long) < 1024),
                "short"	TEXT NOT NULL UNIQUE CHECK(length(short) <= 50),
                PRIMARY KEY("id" AUTOINCREMENT)
                );
                ''')
    conn.commit()


def write_pair_link_to_db(long_link, short_link):
    create_pair_links_sql_query = '''
        INSERT INTO "links"
        ("long", "short")
        VALUES (?, ?);
        '''
    with conn:
        cur = conn.cursor()
        cur.execute(create_pair_links_sql_query, (long_link, short_link))
        conn.commit()


def get_short_link(long_link):
    with conn:
        cur = conn.cursor()
        cur.execute('''
                    SELECT "short"
                    FROM "links"
                    WHERE long=?;
                    ''',
                    (long_link,)
                    )
        return [elem[0] for elem in cur.fetchall()]


def get_long_link(short_link):
    with conn:
        cur = conn.cursor()
        cur.execute('''
                    SELECT "long"
                    FROM "links"
                    WHERE short=?;
                    ''',
                    (short_link,)
                    )
        long_link = cur.fetchall()
        if long_link:
            return long_link[0][0]
