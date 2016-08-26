import flask
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from shelljob import proc
import subprocess

app = Flask('party94', static_url_path='/static')

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route("/reports/<path:script>")
def reports(script):
    try:
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-H", "-f", "amazon-redshift-utils/src/AdminScripts/" + script] 
        status_code=200
        result = shell(cmd)

        header='<html><head><title>Report: ' + script + '</title><head><body>'
        header = header + '<form action="/query" method="get">Query ID: <input type="text" name="queryid"><input type="submit" value="Check a query ID"></form>'
        resp = header + result + '</body></html>'

    except Exception as e:
        resp=str(e)
        status_code=500

    return flask.Response( resp, status_code, mimetype= 'text/html' )


@app.route("/query")
def query():
    try:
        queryid = request.args.get('queryid')

        query = "SELECT query, userid, ((endtime - starttime)/ 1000000) + 1 as secs, starttime, endtime, aborted FROM STL_QUERY WHERE query = " + queryid 
        print "QUERY: " + query
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-H", "-c", query] 
        header='<html><head><title>Query: ' + queryid + '</title><head><body>'
        status_code=200
        result = shell(cmd)
        resp = header + result

        query = "SELECT querytxt FROM STL_QUERY WHERE query = " + queryid
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-H", "-c", query] 
        result = shell(cmd)
        resp = resp + result
        resp += '</body></html>'

    except Exception as e:
        resp=str(e)
        status_code=500

    return flask.Response( resp, status_code, mimetype= 'text/html' )

# untested
@app.route("/user/create/")
def user_create():
    try:
        user = request.args.get('user')
        password = request.args.get('password')
        # set up user with standard access: read-only everywhere except a few schemas
        query = "CREATE USER " + user + " WITH NOCREATEDB NOCREATEUSER "
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-c", query] 
        status_code=200
        result = shell(cmd)

        # ENCRYPTED?
        query = "ALTER USER " + user + " WITH PASSWORD '" + password + "'"
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-c", query] 
        status_code=200
        result = shell(cmd)

        header='<html><head><title>User setup</title><head><body>'
        resp = header + result + '</body></html>'

    except Exception as e:
        resp=str(e)
        status_code=500

    return flask.Response( resp, status_code, mimetype= 'text/html' )

@app.route("/user/read/")
def user_read():
    try:
        user = request.args.get('user')
        # set up user with standard access: read-only everywhere except a few schemas
        query = "create user '" + user + "'"
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-c", query] 
        status_code=200
        result = shell(cmd)

        header='<html><head><title>User setup</title><head><body>'
        resp = header + result + '</body></html>'

    except Exception as e:
        resp=str(e)
        status_code=500

    return flask.Response( resp, status_code, mimetype= 'text/html' )

@app.route("/user/write/")
def user_write():
    try:
        schema = request.args.get('schema')
        user = request.args.get('user')
        # User can write in this database
        query = ""
        cmd = ["/usr/bin/psql", "dev", "-h", "redshift-analytics.nodemodo.com", "-U", "root", "-p", "5439", "-c", query] 
        status_code=200
        result = shell(cmd)

        header='<html><head><title>User/Schema Setup</title><head><body>'

        resp = header + result + '</body></html>'

    except Exception as e:
        resp=str(e)
        status_code=500

    return flask.Response( resp, status_code, mimetype= 'text/html' )

def shell(cmd):
    try:
        print cmd
        # cmd = ["env"]
        g = proc.Group()
        p = g.run(cmd)
        status_code=200
        def read_process():
            result=''
            while g.is_pending():
                lines = g.readlines()
                for proc, line in lines:
                    result= result+line
                    print line
            return result
        resp = read_process()
        return resp

    except Exception as e:
        print(e)
        raise e



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
