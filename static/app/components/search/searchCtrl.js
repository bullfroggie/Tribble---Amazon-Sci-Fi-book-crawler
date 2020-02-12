(function(angular) {
    let app = angular.module("app");

    app.controller("SearchCtrl", [
        "$http",
        "$state",
        function($http, $state) {
            let that = this;

            this.searched = null;
            this.deals = [];
            this.top_three = [];

            // this.search = function() {
            //     if (that.searched == null || that.searched == "") {
            //         return;
            //     }

            //     if ($state.current.url == "deals") {
            //         that.getDeals();
            //         return;
            //     }

            //     $state.go("search.result");
            // };

            this.getDeals = function() {
                $http.get("api/search/deals/" + that.searched).then(
                    function(response) {
                        that.deals = response.data;

                        console.log(that.deals);

                        if (that.deals.length == 1) {
                            that.top_three.push(that.deals[0]);
                            return;
                        } else if (that.deals.length >= 3) {
                            that.top_three.push(that.deals[0]);
                            that.top_three.push(that.deals[1]);
                            that.top_three.push(that.deals[2]);
                            return;
                        } else {
                            return;
                        }
                    },
                    function(reason) {
                        console.log(reason);
                    }
                );
            };

            $state.go("search.result");
            this.getDeals();
        }
    ]);
})(angular);
