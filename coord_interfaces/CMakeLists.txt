cmake_minimum_required(VERSION 3.8)
project(coord_interfaces)
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RawDetection.msg"
  "msg/CoordTask.msg"
  "srv/GetStatus.srv"
  DEPENDENCIES geometry_msgs
)
ament_package()