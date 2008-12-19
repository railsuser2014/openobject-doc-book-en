
FreeBSD
"""""""

If you installed ``python`` from *port*, please check that threading support is enabled: ::

  %> ldd /usr/local/bin/python

  /usr/local/bin/python:
    libutil.so.5 => /lib/libutil.so.5 (0x28119000)
    libstdc++.so.5 => /usr/lib/libstdc++.so.5 (0x28125000)
    libm.so.4 => /lib/libm.so.4 (0x281f8000)
    libpthread.so.2 => /usr/lib/libpthread.so.2 (0x2820f000)
    libc.so.6 => /lib/libc.so.6 (0x28236000)

If you see a line with **libpthread.so.2** line, it's ok.

If it's not the case, this command should do the trick: ::

  $sudo pkg_add -r py24-imaging py24-libxml2 py24-libxslt py24-mx-base py24-parsing py24-psycopg py24-reportlab

Launch the server as usual but don't forget to have a pgsql database up and running.

