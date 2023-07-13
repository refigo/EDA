// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from playing_turtle_package_msgs:srv/TreeSpawn.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "playing_turtle_package_msgs/srv/detail/tree_spawn__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace playing_turtle_package_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void TreeSpawn_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) playing_turtle_package_msgs::srv::TreeSpawn_Request(_init);
}

void TreeSpawn_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<playing_turtle_package_msgs::srv::TreeSpawn_Request *>(message_memory);
  typed_message->~TreeSpawn_Request();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TreeSpawn_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(playing_turtle_package_msgs::srv::TreeSpawn_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TreeSpawn_Request_message_members = {
  "playing_turtle_package_msgs::srv",  // message namespace
  "TreeSpawn_Request",  // message name
  1,  // number of fields
  sizeof(playing_turtle_package_msgs::srv::TreeSpawn_Request),
  TreeSpawn_Request_message_member_array,  // message members
  TreeSpawn_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  TreeSpawn_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TreeSpawn_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TreeSpawn_Request_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace playing_turtle_package_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<playing_turtle_package_msgs::srv::TreeSpawn_Request>()
{
  return &::playing_turtle_package_msgs::srv::rosidl_typesupport_introspection_cpp::TreeSpawn_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, playing_turtle_package_msgs, srv, TreeSpawn_Request)() {
  return &::playing_turtle_package_msgs::srv::rosidl_typesupport_introspection_cpp::TreeSpawn_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "playing_turtle_package_msgs/srv/detail/tree_spawn__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace playing_turtle_package_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void TreeSpawn_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) playing_turtle_package_msgs::srv::TreeSpawn_Response(_init);
}

void TreeSpawn_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<playing_turtle_package_msgs::srv::TreeSpawn_Response *>(message_memory);
  typed_message->~TreeSpawn_Response();
}

size_t size_function__TreeSpawn_Response__x(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TreeSpawn_Response__x(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__TreeSpawn_Response__x(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__TreeSpawn_Response__x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__TreeSpawn_Response__x(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__TreeSpawn_Response__x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__TreeSpawn_Response__x(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__TreeSpawn_Response__x(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__TreeSpawn_Response__y(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TreeSpawn_Response__y(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__TreeSpawn_Response__y(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__TreeSpawn_Response__y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__TreeSpawn_Response__y(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__TreeSpawn_Response__y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__TreeSpawn_Response__y(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__TreeSpawn_Response__y(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__TreeSpawn_Response__theta(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TreeSpawn_Response__theta(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__TreeSpawn_Response__theta(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__TreeSpawn_Response__theta(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__TreeSpawn_Response__theta(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__TreeSpawn_Response__theta(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__TreeSpawn_Response__theta(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__TreeSpawn_Response__theta(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TreeSpawn_Response_message_member_array[3] = {
  {
    "x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(playing_turtle_package_msgs::srv::TreeSpawn_Response, x),  // bytes offset in struct
    nullptr,  // default value
    size_function__TreeSpawn_Response__x,  // size() function pointer
    get_const_function__TreeSpawn_Response__x,  // get_const(index) function pointer
    get_function__TreeSpawn_Response__x,  // get(index) function pointer
    fetch_function__TreeSpawn_Response__x,  // fetch(index, &value) function pointer
    assign_function__TreeSpawn_Response__x,  // assign(index, value) function pointer
    resize_function__TreeSpawn_Response__x  // resize(index) function pointer
  },
  {
    "y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(playing_turtle_package_msgs::srv::TreeSpawn_Response, y),  // bytes offset in struct
    nullptr,  // default value
    size_function__TreeSpawn_Response__y,  // size() function pointer
    get_const_function__TreeSpawn_Response__y,  // get_const(index) function pointer
    get_function__TreeSpawn_Response__y,  // get(index) function pointer
    fetch_function__TreeSpawn_Response__y,  // fetch(index, &value) function pointer
    assign_function__TreeSpawn_Response__y,  // assign(index, value) function pointer
    resize_function__TreeSpawn_Response__y  // resize(index) function pointer
  },
  {
    "theta",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(playing_turtle_package_msgs::srv::TreeSpawn_Response, theta),  // bytes offset in struct
    nullptr,  // default value
    size_function__TreeSpawn_Response__theta,  // size() function pointer
    get_const_function__TreeSpawn_Response__theta,  // get_const(index) function pointer
    get_function__TreeSpawn_Response__theta,  // get(index) function pointer
    fetch_function__TreeSpawn_Response__theta,  // fetch(index, &value) function pointer
    assign_function__TreeSpawn_Response__theta,  // assign(index, value) function pointer
    resize_function__TreeSpawn_Response__theta  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TreeSpawn_Response_message_members = {
  "playing_turtle_package_msgs::srv",  // message namespace
  "TreeSpawn_Response",  // message name
  3,  // number of fields
  sizeof(playing_turtle_package_msgs::srv::TreeSpawn_Response),
  TreeSpawn_Response_message_member_array,  // message members
  TreeSpawn_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  TreeSpawn_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TreeSpawn_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TreeSpawn_Response_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace playing_turtle_package_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<playing_turtle_package_msgs::srv::TreeSpawn_Response>()
{
  return &::playing_turtle_package_msgs::srv::rosidl_typesupport_introspection_cpp::TreeSpawn_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, playing_turtle_package_msgs, srv, TreeSpawn_Response)() {
  return &::playing_turtle_package_msgs::srv::rosidl_typesupport_introspection_cpp::TreeSpawn_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "playing_turtle_package_msgs/srv/detail/tree_spawn__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace playing_turtle_package_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers TreeSpawn_service_members = {
  "playing_turtle_package_msgs::srv",  // service namespace
  "TreeSpawn",  // service name
  // these two fields are initialized below on the first access
  // see get_service_type_support_handle<playing_turtle_package_msgs::srv::TreeSpawn>()
  nullptr,  // request message
  nullptr  // response message
};

static const rosidl_service_type_support_t TreeSpawn_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TreeSpawn_service_members,
  get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace playing_turtle_package_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<playing_turtle_package_msgs::srv::TreeSpawn>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::playing_turtle_package_msgs::srv::rosidl_typesupport_introspection_cpp::TreeSpawn_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure that both the request_members_ and the response_members_ are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::playing_turtle_package_msgs::srv::TreeSpawn_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::playing_turtle_package_msgs::srv::TreeSpawn_Response
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, playing_turtle_package_msgs, srv, TreeSpawn)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<playing_turtle_package_msgs::srv::TreeSpawn>();
}

#ifdef __cplusplus
}
#endif
