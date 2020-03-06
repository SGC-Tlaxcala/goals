(function($){
  $(function(){
    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.datepicker').pickadate({
        selectYears: 3,
        monthsFull: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
        today: 'Hoy',
        clear: 'Borrar',
        close: 'Cerrar',
        format: 'dd/mm/yyyy',
        });
    $('select').not('.disabled').material_select();
    $('.tooltipped').tooltip({delay: 50});
  }); // end of document ready
})(jQuery); // end of jQuery name space