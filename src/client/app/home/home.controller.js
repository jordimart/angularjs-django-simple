(function() {
    'use strict';

    angular
        .module('app.home')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['logger', '$translatePartialLoader', 'dataservice'];

    function HomeController(logger, $translatePartialLoader, dataservice) {
        var vm = this;
        vm.title = 'Home';

        $translatePartialLoader.addPart('home');

        activate();

        function activate() {
            logger.info('Activated Home View');
            dataservice.localCall().then(function(response) {
                console.log(response);
            });
        }
    }
})();