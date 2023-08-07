// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from yolo_inference:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_
#define YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "yolo_inference/msg/detail/inference_result__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace yolo_inference
{

namespace msg
{

namespace builder
{

class Init_InferenceResult_conf
{
public:
  explicit Init_InferenceResult_conf(::yolo_inference::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  ::yolo_inference::msg::InferenceResult conf(::yolo_inference::msg::InferenceResult::_conf_type arg)
  {
    msg_.conf = std::move(arg);
    return std::move(msg_);
  }

private:
  ::yolo_inference::msg::InferenceResult msg_;
};

class Init_InferenceResult_bottom_right
{
public:
  explicit Init_InferenceResult_bottom_right(::yolo_inference::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_conf bottom_right(::yolo_inference::msg::InferenceResult::_bottom_right_type arg)
  {
    msg_.bottom_right = std::move(arg);
    return Init_InferenceResult_conf(msg_);
  }

private:
  ::yolo_inference::msg::InferenceResult msg_;
};

class Init_InferenceResult_bottom
{
public:
  explicit Init_InferenceResult_bottom(::yolo_inference::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_bottom_right bottom(::yolo_inference::msg::InferenceResult::_bottom_type arg)
  {
    msg_.bottom = std::move(arg);
    return Init_InferenceResult_bottom_right(msg_);
  }

private:
  ::yolo_inference::msg::InferenceResult msg_;
};

class Init_InferenceResult_top_left
{
public:
  explicit Init_InferenceResult_top_left(::yolo_inference::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_bottom top_left(::yolo_inference::msg::InferenceResult::_top_left_type arg)
  {
    msg_.top_left = std::move(arg);
    return Init_InferenceResult_bottom(msg_);
  }

private:
  ::yolo_inference::msg::InferenceResult msg_;
};

class Init_InferenceResult_top
{
public:
  explicit Init_InferenceResult_top(::yolo_inference::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_top_left top(::yolo_inference::msg::InferenceResult::_top_type arg)
  {
    msg_.top = std::move(arg);
    return Init_InferenceResult_top_left(msg_);
  }

private:
  ::yolo_inference::msg::InferenceResult msg_;
};

class Init_InferenceResult_label
{
public:
  Init_InferenceResult_label()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InferenceResult_top label(::yolo_inference::msg::InferenceResult::_label_type arg)
  {
    msg_.label = std::move(arg);
    return Init_InferenceResult_top(msg_);
  }

private:
  ::yolo_inference::msg::InferenceResult msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::yolo_inference::msg::InferenceResult>()
{
  return yolo_inference::msg::builder::Init_InferenceResult_label();
}

}  // namespace yolo_inference

#endif  // YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_
