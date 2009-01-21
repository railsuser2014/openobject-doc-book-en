
Server and Client Installation on Mac OS X
""""""""""""""""""""""""""""""""""""""""""

The mentioned sources worked for me but might not be the newest anymore.
Feel free to download and install newer versions (and keep this Howto up to date).

Preparations
^^^^^^^^^^^^

::

  mkdir /Installation

bash profile file at /etc/profile
#################################

::

  -- add path to the DarwinPort ../bin and ../man files
  -- add path to the PostgreSQL ../bin and ../man files
  -- define the DISPLAY variable for X11 apps

  sudo pico /etc/profile

add the following lines to the respective sections

::

  export PATH=${PATH}:/opt/local/bin:/opt/local/sbin -> export PATH=${PATH}:/usr/local/pgsql/bin
  export MANPATH=${MANPATH}:/opt/local/man export MANPATH=${MANPATH}:/usr/local/pgsql/man
  export DISPLAY=":0.0"

restart the Terminal

Create PostgreSQL User & Group
##############################

::

  niutil -create . /groups/postgres
  niutil -createprop . /groups/postgres gid 201
  niutil -createprop . /groups/postgres realname "PostgreSQL Users"
  niutil -createprop . /groups/postgres name postgres
  niutil -createprop . /groups/postgres passwd "*"

  niutil -create . /users/postgres
  niutil -createprop . /users/postgres uid 201
  niutil -createprop . /users/postgres gid 201
  niutil -createprop . /users/postgres name postgres
  niutil -createprop . /users/postgres realname "PostgreSQL User"
  niutil -createprop . /users/postgres shell /bin/sh
  niutil -createprop . /users/postgres home /usr/local/tinyerp-server
  niutil -createprop . /users/postgres passwd "*"
  niutil -createprop . /users/postgres expire 0
  niutil -createprop . /users/postgres change 0

.. *

DarwinPorts Download & Installation (for GTK2 Installation)
###########################################################

::

  cd /Installation
  curl -O "http://svn.macosforge.org/repository/macports/downloads/DarwinPorts-1.3.2/DarwinPorts-1.3.2.tar.gz"
  tar --no-same-owner -xzf DarwinPorts-1.3.2.tar.gz
  cd DarwinPorts-1.3.2
  ./configure
  make
  make install
  port selfupdate
  port install py-gtk2
  cd /opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4
  mv site-packages/README /opt/local/lib/python2.4/site-packages
  rm -r site-packages
  ln -s /opt/local/lib/python2.4/site-packages
  ln -s /opt/local/Library/Frameworks/Python.framework/Versions/2.4/bin/python2.4 /usr/bin/python2.4
  ln -fs /usr/bin/python2.4 /usr/bin/python

PostgreSQL 8.2 Download and Installation
########################################

::

  curl -L "http://wwwmaster.postgresql.org/redir?ftp%3A%2F%2Fftp.hk.postgresql.org%2Fpostgresql%2Fsource%2Fv8.2%2Fpostgresql-8.2.0.tar.gz" -o postgresql-8.2.tar.gz
  tar --no-same-owner -xzf postgresql-8.2.tar.gz
  cd postgresql-8.2.0
  ./configure --enable-thread-safety --with-bonjour --with-openssl --with-perl --with-python
  make
  make install
  cd ..

Create the PostgreSQL enveloping data directory
###############################################

::

  mkdir -p /var/pgsql
  chown postgres:postgres /var/pgsql
  chmod 700 /var/pgsql

Create the database cluster
###########################

::

  sudo -u postgres /usr/local/pgsql/bin/initdb -A md5 -E UTF8 -W -D /var/pgsql/data

there will be a dialog which asks for the password, enter the postgres master PASSWORD there

start PostgreSQL
################

::

  sudo -u postgres /usr/local/pgsql/bin/postmaster -i -D /var/pgsql/data &
  sudo -u postgres createuser --no-createdb --no-adduser terp

enter yes and the postgres master PASSWORD

libxml2 Download and Installation
#################################

::

  curl -O "ftp://ftp.gnome.org/pub/GNOME/sources/libxml2/2.6/libxml2-2.6.23.tar.gz"
  tar --no-same-owner -xzf libxml2-2.6.23.tar.gz
  ./configure --with-python=/opt/local
  cd libxml2-2.6.23
  make
  make install
  cd python
  /opt/local/bin/python2.4 setup.py build
  /opt/local/bin/python2.4 setup.py install
  cd ../../

libxslt-python Download and Installation
########################################

::

  cd /Installation
  curl -O "ftp://ftp.gnome.org/pub/GNOME/sources/libxslt/1.1/libxslt-1.1.15.tar.gz"
  tar --no-same-owner -xzf libxslt-1.1.15.tar.gz
  cd libxslt-1.1.15
  ./configure --with-libxml-prefix=/opt/local --with-python=/opt/local
  make
  make install
  cd python
  cp libx*.py /opt/local/lib/python2.4/site-packages/
  cd ../../

.. *

mxTime & psycopg Download & Installation
########################################

::

  cd /Installation
  curl -LO "http://www.egenix.com/files/python/egenix-mx-base-2.0.6.tar.gz"
  tar --no-same-owner -xzf egenix-mx-base-2.0.6.tar.gz
  cd egenix-mx-base-2.0.6
  /opt/local/bin/python2.4 setup.py install
  cd ..
  curl -O "http://initd.org/pub/software/psycopg/psycopg-1.1.21.tar.gz"
  tar --no-same-owner -xzf psycopg-1.1.21.tar.gz
  cd psycopg-1.1.21
  export MACOSX_DEPLOYMENT_TARGET=10.4
  ./configure --with-python=/opt/local/bin/python2.4 --with-postgres-libraries=/usr/local/pgsql/lib \
  --with-postgres-includes=/usr/local/pgsql/include --with-mxdatetime-includes=/opt/local/lib/python2.4/site-packages/mx/DateTime/mxDateTime
  make
  make install
  cd ..

Python Imaging Library Download & Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  curl -LO "http://effbot.org/downloads/Imaging-1.1.6.tar.gz"
  tar --no-same-owner -xzf Imaging-1.1.6.tar.gz
  cd Imaging-1.1.6
  python setup.py install
  cd ..

ReportLab Toolkit Version 1 Download & Installation
###################################################

::

  cd /Installation
  curl -O "http://www.reportlab.org/ftp/ReportLab_1_21_1.tgz"
  tar --no-same-owner -xzf ReportLab_1_21_1.tgz
  cd ReportLab_1_21_1
  chown -R root:wheel reportlab
  mv reportlab /opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/reportlab
  /opt/local/bin/python2.4
  /opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/compileall.py
  /opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/reportlab
  cd ..

.. xxx

OpenERP 4.0.2 Server Download & Installation
############################################

::

  cd /Installation
  curl -L "http://tinyerp.org/download/old/tinyerp-server-4.0.2.tar.gz" -o tinyerp-server-4.0.2.tar.gz
  tar --no-same-owner -xzf tinyerp-server-4.0.2.tar.gz
  mv tinyerp-server-4.0.2 /usr/local/tinyerp-server-4.0.2
  chown -R postgres:postgres /usr/local/tinyerp-server-4.0.2
  ln -fs /usr/local/tinyerp-server-4.0.2 /usr/local/tinyerp-server
  ln -fs /usr/local/tinyerp-server/man/tinyerp-server.1 /usr/local/man/man1/tinyerp-server.1

First Start of the OpenERP-Server
#################################

::

  cd /usr/local
  sudo -u postgres /opt/local/bin/python2.4 /usr/local/tinyerp-server/bin/tinyerp-server.py

Installation and First Start of the OpenERP 4.0.2 Client
########################################################

::

  cd /Installation
  curl -L "http://tinyerp.org/download/old/tinyerp-client-4.0.2.tar.gz" -o tinyerp-client-4.0.2.tar.gz
  tar --no-same-owner -xzf tinyerp-client-4.0.2.tar.gz
  mv tinyerp-client-4.0.2 /Applications/TinyERP-Client

Create a Desktop-Icon
#####################

copy & paste the next 3 lines all at once together into the Terminal

::

  echo '#!/bin/sh
  /usr/bin/open /Applications/Utilities/X11.app
  export DISPLAY=":0.0"

::

  cd /Applications/TinyERP-Client/bin
  /opt/local/bin/python2.4 tinyerp-client.py
  exit 0' > ~/Desktop/TinyERP-Client.sh
  chmod ugo+x ~/Desktop/TinyERP-Client.sh

Launch Deamons for PostgreSQL and Openerp Server
################################################

::

  pico [=/Library=]/LaunchDeamons/org.postgresql.postmaster.plist

put this into the file:

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple$
  <plist version="1.0">
    <dict>
      <key>Label</key>
      <string>org.postgresql.postmaster</string>
      <key>OnDemand</key>
      <false/>
      <key>ProgramArguments</key>
      <array>
            <string>/usr/local/pgsql/bin/postgres</string>
            <string>-D</string>
            <string>/var/pgsql/data</string>
            <string>-i</string>
      </array>
      <key>ServiceDescription</key>
      <string>PostgreSQL Server</string>
      <key>UserName</key>
      <string>postgres</string>
      </array>
      <key>ServiceDescription</key>
      <string>PostgreSQL Server</string>
      <key>UserName</key>
      <string>postgres</string>
    </dict>
  </plist>

::

  pico [=/Library=]/LaunchDeamons/org.tinyerp.server.plist

put this into the file:

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://  www.apple$
  <plist version="1.0">
    <dict>
      <key>Label</key>
      <string>org.tinyerp.server</string>
      <key>OnDemand</key>
      <false/>
      <key>ProgramArguments</key>
      <array>
            <string>/opt/local/bin/python2.4</string>
            <string>/usr/local/tinyerp-server/bin/tinyerp-server.py</string>
      </array>
      <key>ServiceDescription</key>
      <string>TinyERP Server</string>
      <key>UserName</key>
      <string>postgres</string>
    </dict>
  </plist>

