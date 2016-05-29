module.exports = function(grunt) {
	grunt.loadNpmTasks('grunt-contrib-cssmin');
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-copy');


grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
	//------- CSS Minify -------//
	cssmin: {
		combine: {
		  files: {
		    '../erehwon/static/styles/styles.css': ['styles/css/styles.css']
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
		  files: 'sass/styles.scss',
		  tasks: ['sass']
		}
	},
	jspaths: {
        src: {
                js: 'scripts/**/**.js'
            },
            dest: {
                jsMin: '../erehwon/static/scripts/erehwon.min.js'
            }
    },
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
	      {expand: true, src: ['img/*'], dest: '../erehwon/static/', filter: 'isFile'},
	    ],
	  },
	},

	});

	grunt.registerTask('default', ['sass', 'cssmin', 'uglify', 'copy:img']);

}