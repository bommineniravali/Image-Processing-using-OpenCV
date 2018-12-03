cmake_minimum_required(VERSION 2.6)
project( gray )
find_package( OpenCV REQUIRED )
add_executable( grayimage GrayScale.cpp )
target_link_libraries( grayimage ${OpenCV_LIBS} )

