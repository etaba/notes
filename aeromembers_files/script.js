var app = angular.module('myApp', ['ngSanitize','ngCookies']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


app.controller('forumCtrl', ['$scope', '$http', '$sce', '$cookies', '$document', '$window', function($scope, $http, $sce, $cookies, $document, $window) {
    
    $http({
            url: "comments/",
            method: 'GET',
        }).then(function success(response){
            $scope.comments = response.data.comments
            $scope.threadId = response.data.threadId
            $scope.user = response.data.user
        },function error(){
            console.log("No comments found")
        })

    $scope.upvoteComment = function(comment){
        $http({
            url: "/upvotecomment/",
            method: 'POST',
            data: {'commentId':comment.id}
        }).then(function success(){
            comment.score = (parseInt(comment.score) + 1).toString()
        },function error(){
            console.log("This user has already upvoted")
        })
    }

    $scope.upvoteThread = function(threadId){
        $http({
            url: "/upvotepost/",
            method: 'POST',
            data: {'postId':threadId}
        }).then(function success(){
            var score = parseInt($document[0].getElementById("threadScore").textContent)
            score += 1
            $document[0].getElementById("threadScore").textContent = score.toString()
            $document[0].getElementById("threadScore").classList.add("upvoted")
        },function error(){
            console.log("This user has already upvoted")
        })
    }

    $scope.deleteComment = function(commentId){
        $window.location.href = 'deletepost/'+commentId;
    }


}]);

app.controller('checkoutCtrl', ['$scope','$http','$location',function($scope,$http,$location){
    var button = document.querySelector('#submit');
    /*$http({
            url: "/clienttoken/",
            method: 'GET'
        }).then(function success(response){
            braintree.dropin.create({
                  authorization: response.data,
                  container: '#dropin-container'
                }, function (createErr, instance) {
                  button.addEventListener('click', function () {
                    instance.requestPaymentMethod(function (err, payload) {
                      $http({
                        url: "/paymentnonce/",
                        method: 'POST',
                        data: {'paymentNonce':payload}
                      })
                    });
                  });
                });
        },function error(){
            console.log("Client token not received.")
        })

    $scope.purchaseSubscription = function(membershipType){
        $http({
            url: "/clienttoken/",
            method: 'GET'
        }).then(function success(response){
            braintree.dropin.create({
                  authorization: response.data,
                  container: '#subscribe-payment-container'
                }, function (createErr, instance) {
                  button.addEventListener('click', function () {
                    instance.requestPaymentMethod(function (err, payload) {
                      $http({
                        url: "/subscribeuser/",
                        method: 'POST',
                        data: {'paymentNonce':payload.nonce,
                                'membership':$scope.membershipSelected}
                      }).then(function success(response){
                        console.log("Payment was successful")
                      },function error(){
                        console.log("Error processing your payment")
                      })
                    });

                  });
                });
        },function error(){
            console.log("Client token not received.")
        })
    }
    */


    $scope.orderAndCheckout = function(item){
        $http({
            url: "/addOrderLine/",
            method: 'POST',
            data: {'item':item}
        }).then(function success(response){
            $location.href = '/checkout'
        },function error(){
            console.log("Client token not received.")
        })
    };


    loadPaymentMethods = function(){
        $http({
            url: "/clienttoken/",
            method: 'GET'
        }).then(function success(response){
            $scope.showAddPaymentMethod = true
            braintree.dropin.create({
                  authorization: response.data,
                  container: '#braintree-dropin'
                }, function (createErr, instance) {
                    $scope.braintreeDropin = instance
                });
        },function error(){
            console.log("Client token not received.")
        })
    };

    loadOpenOrder = function(){
        $http({
            url: "getorder/",
            method: 'GET',
        }).then(function success(response){
            $scope.order = response.data.order
        },function error(){
            console.log("No order found")
        })
    }

    $scope.addPaymentMethod = function(){
        $scope.braintreeDropin.requestPaymentMethod(function (err, payload) {
              $http({
                url: "/addpaymentmethod/",
                method: 'POST',
                data: {'paymentNonce':payload.nonce}
              }).then(function success(response){
                $scope.paymentMethods['creditCard'].push(response.data['creditCard'])
                $scope.paymentMethods.paypal.push(response.data.paypal)
              },function error(){
                console.log("Error processing adding payment method")
              })
            });
    };

    $scope.pay = function () {
        $scope.braintreeDropin.requestPaymentMethod(function (err, payload) {
            $http({
                url: "/checkout/",
                method: 'POST',
                data: {'paymentNonce':payload.nonce,
                        'membership':$scope.plan}
            }).then(function success(response){
                console.log("Payment was successful")
            },function error(err){
                console.log("Error processing your payment")
            })
        })
    };

    loadPaymentMethods()
    
}]);