Little site to run DBA utilities. Inspired by the -H option to psql.

Favicon courtesy of http://www.freefavicon.com/freefavicons/software/iconinfo/blue-database-152-190594.html - "GIMP Colorize" to red. That was damn easy!

* Build:
** in base: make build
***  Downloads all huge binaries
** in site:
*** Create site/omg/pgpass file - this is the psql .pgpass Postgres password file. Copied into Docker container.
*** make build
**** Assembles base, config files, flask files, pgpass and current github release of AWS tools.
*** make run - open http://localhost:5000 to see this minimalist marvel in action

