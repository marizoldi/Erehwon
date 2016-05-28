module.exports = function(grunt) {
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');


grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
	//------- SASS -------//
	sass: {
		dist: {
			files: {
				'styles/css/styles.css': 'styles/styles.scss'
			}
		}
	},
	//------- Watch SASS -> CSS -------//
	watch: {
		sass: {
		  files: 'styles/**/*.scss',
		  tasks: ['sass']
		}
	},

});

	grunt.registerTask('default', ['sass']);

}