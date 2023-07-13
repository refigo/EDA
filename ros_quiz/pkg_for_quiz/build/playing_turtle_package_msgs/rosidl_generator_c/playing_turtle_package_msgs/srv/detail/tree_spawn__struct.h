// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from playing_turtle_package_msgs:srv/TreeSpawn.idl
// generated code does not contain a copyright notice

#ifndef PLAYING_TURTLE_PACKAGE_MSGS__SRV__DETAIL__TREE_SPAWN__STRUCT_H_
#define PLAYING_TURTLE_PACKAGE_MSGS__SRV__DETAIL__TREE_SPAWN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/TreeSpawn in the package playing_turtle_package_msgs.
typedef struct playing_turtle_package_msgs__srv__TreeSpawn_Request
{
  uint8_t structure_needs_at_least_one_member;
} playing_turtle_package_msgs__srv__TreeSpawn_Request;

// Struct for a sequence of playing_turtle_package_msgs__srv__TreeSpawn_Request.
typedef struct playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence
{
  playing_turtle_package_msgs__srv__TreeSpawn_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'x'
// Member 'y'
// Member 'theta'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/TreeSpawn in the package playing_turtle_package_msgs.
typedef struct playing_turtle_package_msgs__srv__TreeSpawn_Response
{
  rosidl_runtime_c__double__Sequence x;
  rosidl_runtime_c__double__Sequence y;
  rosidl_runtime_c__double__Sequence theta;
} playing_turtle_package_msgs__srv__TreeSpawn_Response;

// Struct for a sequence of playing_turtle_package_msgs__srv__TreeSpawn_Response.
typedef struct playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence
{
  playing_turtle_package_msgs__srv__TreeSpawn_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLAYING_TURTLE_PACKAGE_MSGS__SRV__DETAIL__TREE_SPAWN__STRUCT_H_
