# TDKR Pre-Screening Checker


Checks whether Cinemark has opened a pre-screening for The Dark Knight Rises.

[CasperJS](http://casperjs.org/) is used to fetch [the ticket buying website](http://www.ingresso.com.br/br/cinema/porfilme.asp?T_PARCERIA=CINEMARK&T_IDCIDADE=00000021&Busca=1&ParceriaBusca=CINEMARK&IdEspetaculoBusca=00023819&DataBusca=11/07/2012&IdGrupoBusca=00000309&IdCidadeCompra=00000021), which is the official hub for Cinemark's tickets in Brazil.

`checker.js` is the script responsible for looking for a pre-screening. This is done by entering the webpage and looking for the dates in a selection box and also by a message which tells the first screening available. This information is fetched based upon the `ids` and `classes` of their given HTML entities.

`py_checker.py` is a python script responsible for comparing the information fetched to the one which was present on the website when this script was built. Then, it sends and email if it finds a date which is different from the one previously stored. To do so, it uses [ssmtp](http://linux.die.net/man/8/ssmtp), so it must be installed and properly configured. Below is a sample configuration for Gmail, present on the file `/etc/ssmtp/ssmtp.conf`:


    Root=example@gmail.com
    Mailhub=smtp.gmail.com:465
    RewriteDomain=gmail.com
    AuthUser=example
    AuthPass=mypassword
    FromLineOverride=Yes
    UseTLS=Yes

The python script also relies on some local configuration, the sender email address (the one configured in `ssmtp`) and the receiver email address. Based upon `email_to_send.py.template`, customize it to your needs:

    $ cp email_to_send.py.template email_to_send.py

It makes sense to run this script as a cron task. To run the script every 10 minutes, insert the following line in the `/etc/crontab` file:

    */10 * * * * root cd /path/to/the/project/ && python py_checker.py

