(function() {
    'use strict';

    angular
        .module('app.core')
        .factory('dataservice', dataservice);

    dataservice.$inject = ['$http', '$q', 'exception', 'logger'];
    /* @ngInject */
    function dataservice($http, $q, exception, logger) {
        var service = {
            localCall: localCall
        };

        return service;

        function localCall() {
            return $http.get('http://localhost:8000/admin/')
                .then(success)
                .catch(fail);

            function success(response) {

                return response;
            }

            function fail(e) {

                return exception.catcher('XHR Failed for socialSignin')(e);
            }
        }
    }

})();