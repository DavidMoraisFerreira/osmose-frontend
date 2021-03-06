#! /bin/bash

item=$1
cl=$2

echo -n "$item - $cl "
psql -d osmose_frontend --tuples-only -c "SELECT count(*) FROM marker WHERE item = '$item' and class='$cl'"

echo "confirm?"
read ln

psql -d osmose_frontend -c  "DELETE FROM marker where item = '$item' and class='$cl'"
psql -d osmose_frontend -c  "DELETE FROM dynpoi_class where item = '$item' and class='$cl'"
psql -d osmose_frontend -c  "DELETE FROM class where item = '$item' and class='$cl'"
