(function(angular) {
    let app = angular.module("app");

    app.controller("SearchCtrl", [
        "$http",
        "$state",
        function($http, $state) {
            let that = this;

            this.searched = null;
            this.deals = [];

            this.search = function() {
                if (that.searched == null || that.searched == "") {
                    return;
                } else {
                    $http.get("api/search/" + that.searched).then(
                        function(response) {
                            console.log(response);
                            $state.go("search.result");
                        },
                        function(reason) {
                            console.log(reason);
                        }
                    );
                }
            };
        }
    ]);
})(angular);
