#
# TARGETS
#

ADD_EXECUTABLE (uvcdynctrl main.c controls.c cmdline.c)

SET_TARGET_PROPERTIES (uvcdynctrl PROPERTIES VERSION 0.2)


#
# SPECIAL FILES
#

# gengetopt for command line parsing
ADD_CUSTOM_COMMAND (
	OUTPUT		${CMAKE_CURRENT_SOURCE_DIR}/cmdline.c ${CMAKE_CURRENT_SOURCE_DIR}/cmdline.h
	COMMAND		gengetopt ARGS -i ${CMAKE_CURRENT_SOURCE_DIR}/uvcdynctrl.ggo --output-dir ${CMAKE_CURRENT_SOURCE_DIR} --unamed-opts=VALUES
	DEPENDS 	${CMAKE_CURRENT_SOURCE_DIR}/uvcdynctrl.ggo
	COMMENT		"Generating getopt parser code (cmdline.*) ..."
	VERBATIM
)

# config.h
# Note how we define HAVE_CONFIG_H. This will let gengetopt pick up
# the VERSION constant from config.h.
GET_TARGET_PROPERTY (UVCDYNCTRL_VERSION uvcdynctrl VERSION)
CONFIGURE_FILE (${CMAKE_CURRENT_SOURCE_DIR}/config.h.cmake ${CMAKE_CURRENT_BINARY_DIR}/config.h)
ADD_DEFINITIONS (-DHAVE_CONFIG_H)



#
# COMPILATION AND LINKING
#

ADD_DEFINITIONS (-Wall --std=gnu99)

INCLUDE_DIRECTORIES (${LIBWEBCAM_SOURCE_DIR}/Common/include)
INCLUDE_DIRECTORIES (${CMAKE_CURRENT_BINARY_DIR})
LINK_DIRECTORIES (${LIBWEBCAM_BINARY_DIR}/webcam)

TARGET_LINK_LIBRARIES (uvcdynctrl webcam)


#
# INSTALLATION
#

# Tool
INSTALL (
	TARGETS		uvcdynctrl
	RUNTIME DESTINATION	bin
)

# udev rules, script, and data
# Default permissions for DIRECTORY files: rw-r--r--
# Default permissions for PROGRAMS files:  rwxr-xr-x
INSTALL (
	DIRECTORY	udev/rules/
	DESTINATION /etc/udev/rules.d
	PATTERN ".svn" EXCLUDE
)
INSTALL (
	PROGRAMS	udev/scripts/uvcdynctrl
	DESTINATION	/lib/udev
)
INSTALL (
	DIRECTORY	data
	DESTINATION /etc/udev
	PATTERN ".svn" EXCLUDE
)
