'''
Created on Dec 4, 2013

@author: mahesh
'''
import _mysql;
import sys

try:
    con = _mysql.connect ('localhost', 'mahesh', 'mahesh', 'cricstatsdb');
    con.query ("SELECT VERSION()");
    result = con.use_result();
    
    print "MYSQL VERSION: %s" % result.fetch_row()[0];
    
except _mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1]);
    sys.exit(1);
    
finally:
    if con:
        con.close();