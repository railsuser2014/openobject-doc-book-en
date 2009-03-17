Shutting down the server 
======================== 

The easiest way the shut down the server on a Linux type system is to send the SIG INT signal to the server.

    * Find the Process ID.
          - # ps ax | grep -i tiny 
    * Use the kill comand with the PID.
          - # kill -2 pid 

