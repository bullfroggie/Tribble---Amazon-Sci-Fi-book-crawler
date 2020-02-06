(function(angular) {
    let app = angular.module("app", ["ui.router"]);

    app.config([
        "$stateProvider",
        "$urlRouterProvider",
        function($stateProvider, $urlRouterProvider) {
            $stateProvider
                .state("search", {
                    url: "/",
                    templateUrl: "app/components/search/search.tpl.html",
                    controller: "SearchCtrl",
                    controllerAs: "sctrl"
                })
                .state("search.result", {
                    url: "deals",
                    templateUrl: "app/components/result/result.tpl.html",
                    controller: "SearchCtrl",
                    controllerAs: "sctrl"
                });

            $urlRouterProvider.otherwise("/");
        }
    ]);
})(angular);
