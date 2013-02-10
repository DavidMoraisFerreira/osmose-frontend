#! /usr/bin/env python
#-*- coding: utf-8 -*-

###########################################################################
##                                                                       ##
## Copyrights Etienne Chové <chove@crans.org> 2009                       ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from bottle import route, response
from tools import utils


def _items(db, lang):
    sql = """
    SELECT
        item,
        menu
    FROM
        dynpoi_item
    ORDER BY
        item
    """
    db.execute(sql)
    return db.fetchall()


@route('/api/0.2/meta/items')
def items(db, lang):
    return {"items": _items(db, lang)}


def _countries(db, lang):
    sql = """
    SELECT DISTINCT
        (string_to_array(comment,'-'))[array_upper(string_to_array(comment,'-'), 1)] AS country
    FROM
        dynpoi_source
    ORDER BY
        country
    """
    db.execute(sql)
    return db.fetchall()


@route('/api/0.2/meta/countries')
def items(db, lang):
    return {"countries": map(lambda x: x[0], _countries(db, lang))}
