/*var app;
app = angular.module('example.app.basic', []);
app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.stars = [];
    return $http.get('/api/stars/?format=json').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.stars.push(item);
      });
    });
  }
]);*/

/*
var app;
app = angular.module('example.app.static', []);
app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    return $scope.posts = [
      {
        name:'Joe',
   
        newses : [
		{

        		header: 'This is the first sample post',
			text : 'THis is Text',
			url : 'https://en.wikipedia.org/wiki/Zlatan_Ibrahimovi%25C4%2587',

		}
	]
      }
    ];
  }
]);*/
/*(function(){
	var app;
	app = angular.module('example.api', ['ngResource']);
	app.factory('User', [
  	'$resource', function($resource) {
    return $resource('/api/users/:username', {
      username: '@username'
    });
  }
]);
app.factory('Post', [
  '$resource', function($resource) {
    return $resource('/api/posts/:id', {
      id: '@id'
    });
  }
]);
app.factory('Photo', [
  '$resource', function($resource) {
    return $resource('/api/photos/:id', {
      id: '@id'
    });
  }
]);
})()*/
var app;
app = angular.module('example.app.static', []);
app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.posts = [];
 
     return $http.get('/api/stars/?format=json').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.posts.push(item);
      });
    });
  }
]);
