module.exports = function(grunt) {
	grunt.loadNpmTasks('grunt-contrib-cssmin');
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-ng-annotate');


grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
	//------- CSS Minify -------//
	cssmin: {
		combine: {
		  files: {
		    '../erehwon/erehwon/static/styles/styles.css': ['css/styles.css']
		  }
		}
	},
	//------- SASS -------//
	sass: {
		dist: {
			files: {
				'css/styles.css': 'styles/styles.scss'
			}
		}
	},
	//------- Watch SASS -> CSS -------//
	watch: {
		sass: {
		  files: 'styles/**/*.scss',
		  tasks: ['sass','cssmin']
		}
	},
	jspaths: {
        src: {
               js: ['scripts/**/**.js']
            },
            dest: {
                jsMin: '../erehwon/erehwon/static/scripts/erehwon.min.js'
            }
    },

		//--------- JS Minify -------//
    uglify: {
        options: {
            compress: true,
            mangle: true,
            sourceMap: true
        },
        target: {
            src: '<%= jspaths.src.js %>',
            dest: '<%= jspaths.dest.jsMin %>'
        }
    },
    copy: {
	  img: {
	  	files: [
	    // includes files within path
	    {expand: true, src: ['img/*'], dest: '../erehwon/erehwon/static/', filter: 'isFile'},
	    ],
	  },
	},
	ngAnnotate: {
	    options: {
	        singleQuotes: true
	    },
	    app: {
	        files: {
	        	'app/min-safe-app.js':['app/app.js'],
	       	}
	    }
	},
});


	grunt.registerTask('default', ['ngAnnotate', 'sass', 'cssmin', 'uglify', 'copy:img']);
}
