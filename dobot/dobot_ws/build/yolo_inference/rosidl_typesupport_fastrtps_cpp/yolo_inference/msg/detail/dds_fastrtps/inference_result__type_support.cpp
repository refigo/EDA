// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from yolo_inference:msg/InferenceResult.idl
// generated code does not contain a copyright notice
#include "yolo_inference/msg/detail/inference_result__rosidl_typesupport_fastrtps_cpp.hpp"
#include "yolo_inference/msg/detail/inference_result__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace yolo_inference
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolo_inference
cdr_serialize(
  const yolo_inference::msg::InferenceResult & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: label
  cdr << ros_message.label;
  // Member: top
  cdr << ros_message.top;
  // Member: top_left
  cdr << ros_message.top_left;
  // Member: bottom
  cdr << ros_message.bottom;
  // Member: bottom_right
  cdr << ros_message.bottom_right;
  // Member: conf
  cdr << ros_message.conf;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolo_inference
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  yolo_inference::msg::InferenceResult & ros_message)
{
  // Member: label
  cdr >> ros_message.label;

  // Member: top
  cdr >> ros_message.top;

  // Member: top_left
  cdr >> ros_message.top_left;

  // Member: bottom
  cdr >> ros_message.bottom;

  // Member: bottom_right
  cdr >> ros_message.bottom_right;

  // Member: conf
  cdr >> ros_message.conf;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolo_inference
get_serialized_size(
  const yolo_inference::msg::InferenceResult & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: label
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.label.size() + 1);
  // Member: top
  {
    size_t item_size = sizeof(ros_message.top);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: top_left
  {
    size_t item_size = sizeof(ros_message.top_left);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bottom
  {
    size_t item_size = sizeof(ros_message.bottom);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bottom_right
  {
    size_t item_size = sizeof(ros_message.bottom_right);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: conf
  {
    size_t item_size = sizeof(ros_message.conf);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolo_inference
max_serialized_size_InferenceResult(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: label
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: top
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: top_left
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: bottom
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: bottom_right
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: conf
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _InferenceResult__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const yolo_inference::msg::InferenceResult *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _InferenceResult__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<yolo_inference::msg::InferenceResult *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _InferenceResult__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const yolo_inference::msg::InferenceResult *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _InferenceResult__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_InferenceResult(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _InferenceResult__callbacks = {
  "yolo_inference::msg",
  "InferenceResult",
  _InferenceResult__cdr_serialize,
  _InferenceResult__cdr_deserialize,
  _InferenceResult__get_serialized_size,
  _InferenceResult__max_serialized_size
};

static rosidl_message_type_support_t _InferenceResult__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_InferenceResult__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace yolo_inference

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_yolo_inference
const rosidl_message_type_support_t *
get_message_type_support_handle<yolo_inference::msg::InferenceResult>()
{
  return &yolo_inference::msg::typesupport_fastrtps_cpp::_InferenceResult__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, yolo_inference, msg, InferenceResult)() {
  return &yolo_inference::msg::typesupport_fastrtps_cpp::_InferenceResult__handle;
}

#ifdef __cplusplus
}
#endif
