# - Try to find HEIF
# Once done, this will define
#
#  HEIF_FOUND - system has HEIF
#  HEIF_INCLUDE_DIR - the HEIF include directories
#  HEIF_LIBRARY - link this to use HEIF

MESSAGE(STATUS "Try to find HEIF")

# Look for the header file.
FIND_PATH(HEIF_INCLUDE_DIR NAMES libheif/heif.h)

# Look for the library.
FIND_LIBRARY(HEIF_LIBRARY NAMES heif)
