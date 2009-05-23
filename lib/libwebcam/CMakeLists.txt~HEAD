#
# GENERAL
#

# Require CMake 2.4.4 because of FindLibXml2.cmake
CMAKE_MINIMUM_REQUIRED (VERSION 2.4.4)

# The name of our project is "LIBWEBCAM".
# CMakeLists files in this project can refer to the root source directory of
# the project as ${LIBWEBCAM_SOURCE_DIR} and to the root binary directory of
# the project as ${LIBWEBCAM_BINARY_DIR}.
PROJECT (LIBWEBCAM)


#
# PACKAGING
#

SET (CPACK_GENERATOR					"TGZ")
SET (CPACK_PACKAGE_DESCRIPTION_SUMMARY	"Webcam Library")
SET (CPACK_PACKAGE_VENDOR				"Logitech")
SET (CPACK_PACKAGE_VERSION_MAJOR		"0")
SET (CPACK_PACKAGE_VERSION_MINOR		"1")
SET (CPACK_PACKAGE_VERSION_PATCH		"1")
SET (CPACK_PACKAGE_FILE_NAME			"libwebcam-${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH}-linux-i686")

SET (CPACK_RESOURCE_FILE_README			"${LIBWEBCAM_SOURCE_DIR}/README")
SET (CPACK_RESOURCE_FILE_LICENSE		"${LIBWEBCAM_SOURCE_DIR}/Libs/libwebcam/COPYING")

SET (CPACK_SOURCE_GENERATOR				"TGZ;TBZ2")
SET (CPACK_SOURCE_PACKAGE_FILE_NAME		"libwebcam-${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH}")
# The following is a list of semicolon separate regexp patterns of files and
# directories to ignore. Regexp anchors like ^ and $ can be used but because
# CPack matches entire paths ^ won't work for file matching. We can use / on
# the left-hand side instead. Also note that backslashes need to be double-
# escaped (i.e. \\\\). Therefore Perl's \. to match a dot becomes \\\\. here.
SET (CPACK_SOURCE_IGNORE_FILES			"/\\\\.svn/"					# Subversion directories
										"/\\\\..+$"						# Hidden files and directories
										"/Common/include/uvc.*\\\\.h"	# uvcvideo headers
										"uninstall.sh"
										"makedoc.sh"
										"/doxygen\\\\.*/"
										"build"							# The build directory
)

INCLUDE (CPack)


#
# SUBDIRECTORIES
#

ADD_SUBDIRECTORY (Libs)
ADD_SUBDIRECTORY (Apps)
