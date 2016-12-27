#!/bin/bash

# Source: https://snikt.net/blog/2012/11/11/howto-change-table-owners-in-postgres/

# test that there are two arguments
if test $# -lt 2; then
  echo "usage: $0 <database> <new-owner>"
  exit 0
fi

database=$1
new_owner=$2

tables=`psql -qAt -c "SELECT tablename FROM pg_tables WHERE schemaname = 'public';" ${database}`

psql -c "ALTER DATABASE $database OWNER TO $new_owner;";

for tbl in ${tables} ; do
  psql -c "ALTER TABLE $tbl OWNER TO $new_owner" ${database} ;
done
