// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from playing_turtle_package_msgs:srv/TreeSpawn.idl
// generated code does not contain a copyright notice

#ifndef PLAYING_TURTLE_PACKAGE_MSGS__SRV__DETAIL__TREE_SPAWN__BUILDER_HPP_
#define PLAYING_TURTLE_PACKAGE_MSGS__SRV__DETAIL__TREE_SPAWN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "playing_turtle_package_msgs/srv/detail/tree_spawn__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace playing_turtle_package_msgs
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::playing_turtle_package_msgs::srv::TreeSpawn_Request>()
{
  return ::playing_turtle_package_msgs::srv::TreeSpawn_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace playing_turtle_package_msgs


namespace playing_turtle_package_msgs
{

namespace srv
{

namespace builder
{

class Init_TreeSpawn_Response_theta
{
public:
  explicit Init_TreeSpawn_Response_theta(::playing_turtle_package_msgs::srv::TreeSpawn_Response & msg)
  : msg_(msg)
  {}
  ::playing_turtle_package_msgs::srv::TreeSpawn_Response theta(::playing_turtle_package_msgs::srv::TreeSpawn_Response::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::playing_turtle_package_msgs::srv::TreeSpawn_Response msg_;
};

class Init_TreeSpawn_Response_y
{
public:
  explicit Init_TreeSpawn_Response_y(::playing_turtle_package_msgs::srv::TreeSpawn_Response & msg)
  : msg_(msg)
  {}
  Init_TreeSpawn_Response_theta y(::playing_turtle_package_msgs::srv::TreeSpawn_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_TreeSpawn_Response_theta(msg_);
  }

private:
  ::playing_turtle_package_msgs::srv::TreeSpawn_Response msg_;
};

class Init_TreeSpawn_Response_x
{
public:
  Init_TreeSpawn_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TreeSpawn_Response_y x(::playing_turtle_package_msgs::srv::TreeSpawn_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_TreeSpawn_Response_y(msg_);
  }

private:
  ::playing_turtle_package_msgs::srv::TreeSpawn_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::playing_turtle_package_msgs::srv::TreeSpawn_Response>()
{
  return playing_turtle_package_msgs::srv::builder::Init_TreeSpawn_Response_x();
}

}  // namespace playing_turtle_package_msgs

#endif  // PLAYING_TURTLE_PACKAGE_MSGS__SRV__DETAIL__TREE_SPAWN__BUILDER_HPP_
