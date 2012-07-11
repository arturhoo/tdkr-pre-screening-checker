# TDKR Pre-Screening Checker


Checks whether Cinemark has opened a pre-screening for The Dark Knight Rises.

[CasperJS](http://casperjs.org/) is used to fetch [the ticket buying website](http://www.ingresso.com.br/br/cinema/porfilme.asp?T_PARCERIA=CINEMARK&T_IDCIDADE=00000021&Busca=1&ParceriaBusca=CINEMARK&IdEspetaculoBusca=00023819&DataBusca=11/07/2012&IdGrupoBusca=00000309&IdCidadeCompra=00000021), which is the official hub for Cinemark's tickets in Brazil.

A pre-screening is looked for by entering the webpage and looking for the dates in a selection box and also by a message which tells the first screening available. This information is fetched based upon the `ids` and `classes` of their given HTML entities. The information fetched is compared to the ones which were on the website when this script was built.

The script sends and email when it finds a date which is different from the one previously stored. To do so, it uses [ssmtp](http://linux.die.net/man/8/ssmtp), so it must be installed and properly configured. Below is a sample configuration for Gmail, present on the file `/etc/ssmtp/ssmtp.conf`:


    Root=example@gmail.com
    Mailhub=smtp.gmail.com:465
    RewriteDomain=gmail.com
    AuthUser=example
    AuthPass=mypassword
    FromLineOverride=Yes
    UseTLS=Yes

It makes sense to run this script as a cron task. To run the script every 10 minutes, insert the following line in the `/etc/crontab` file:

    */10 * * * * root cd /path/to/the/project/ && python py_checker.py

