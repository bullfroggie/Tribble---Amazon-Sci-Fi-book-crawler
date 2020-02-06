(function(angular) {
    let app = angular.module("app");

    app.controller("SearchCtrl", [
        "$http",
        function($http) {
            let that = this;

            this.search = null;
        }
    ]);
    
})(angular);
