var casper = require('casper').create({
    verbose: true
});

casper.start("http://www.ingresso.com.br/br/cinema/porfilme.asp?T_PARCERIA=CINEMARK&T_IDCIDADE=00000021&Busca=1&ParceriaBusca=CINEMARK&IdEspetaculoBusca=00023819&DataBusca=11/07/2012&IdGrupoBusca=00000309&IdCidadeCompra=00000021", function() {
    this.echo(this.evaluate(function () {
        return document.getElementById('selData').length;
    }));
    this.echo(this.evaluate(function () {
        return document.getElementsByClassName('f-blink')[0].innerHTML;
    }));
});

casper.run();
