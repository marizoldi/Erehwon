var erehwonApp = angular.module('erehwonApp',[]);

erehwonApp.controller('DashboardController', function DashboardController($scope) {
	
});

erehwonApp.controller('ManageController', function ManageController($scope){
	$scope.showAdd = false;
	$scope.clickAdd = function() {
		$scope.showAdd = !$scope.showAdd;
	}
	$scope.addForm = {};
});