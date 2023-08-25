// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from yolo_inference:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__TRAITS_HPP_
#define YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "yolo_inference/msg/detail/inference_result__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace yolo_inference
{

namespace msg
{

inline void to_flow_style_yaml(
  const InferenceResult & msg,
  std::ostream & out)
{
  out << "{";
  // member: label
  {
    out << "label: ";
    rosidl_generator_traits::value_to_yaml(msg.label, out);
    out << ", ";
  }

  // member: top
  {
    out << "top: ";
    rosidl_generator_traits::value_to_yaml(msg.top, out);
    out << ", ";
  }

  // member: top_left
  {
    out << "top_left: ";
    rosidl_generator_traits::value_to_yaml(msg.top_left, out);
    out << ", ";
  }

  // member: bottom
  {
    out << "bottom: ";
    rosidl_generator_traits::value_to_yaml(msg.bottom, out);
    out << ", ";
  }

  // member: bottom_right
  {
    out << "bottom_right: ";
    rosidl_generator_traits::value_to_yaml(msg.bottom_right, out);
    out << ", ";
  }

  // member: conf
  {
    out << "conf: ";
    rosidl_generator_traits::value_to_yaml(msg.conf, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InferenceResult & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: label
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "label: ";
    rosidl_generator_traits::value_to_yaml(msg.label, out);
    out << "\n";
  }

  // member: top
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "top: ";
    rosidl_generator_traits::value_to_yaml(msg.top, out);
    out << "\n";
  }

  // member: top_left
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "top_left: ";
    rosidl_generator_traits::value_to_yaml(msg.top_left, out);
    out << "\n";
  }

  // member: bottom
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "bottom: ";
    rosidl_generator_traits::value_to_yaml(msg.bottom, out);
    out << "\n";
  }

  // member: bottom_right
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "bottom_right: ";
    rosidl_generator_traits::value_to_yaml(msg.bottom_right, out);
    out << "\n";
  }

  // member: conf
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "conf: ";
    rosidl_generator_traits::value_to_yaml(msg.conf, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InferenceResult & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace yolo_inference

namespace rosidl_generator_traits
{

[[deprecated("use yolo_inference::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const yolo_inference::msg::InferenceResult & msg,
  std::ostream & out, size_t indentation = 0)
{
  yolo_inference::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use yolo_inference::msg::to_yaml() instead")]]
inline std::string to_yaml(const yolo_inference::msg::InferenceResult & msg)
{
  return yolo_inference::msg::to_yaml(msg);
}

template<>
inline const char * data_type<yolo_inference::msg::InferenceResult>()
{
  return "yolo_inference::msg::InferenceResult";
}

template<>
inline const char * name<yolo_inference::msg::InferenceResult>()
{
  return "yolo_inference/msg/InferenceResult";
}

template<>
struct has_fixed_size<yolo_inference::msg::InferenceResult>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<yolo_inference::msg::InferenceResult>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<yolo_inference::msg::InferenceResult>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__TRAITS_HPP_
