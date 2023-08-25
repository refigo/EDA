// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from yolo_inference:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__STRUCT_HPP_
#define YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__yolo_inference__msg__InferenceResult __attribute__((deprecated))
#else
# define DEPRECATED__yolo_inference__msg__InferenceResult __declspec(deprecated)
#endif

namespace yolo_inference
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InferenceResult_
{
  using Type = InferenceResult_<ContainerAllocator>;

  explicit InferenceResult_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->label = "";
      this->top = 0ll;
      this->top_left = 0ll;
      this->bottom = 0ll;
      this->bottom_right = 0ll;
      this->conf = 0.0;
    }
  }

  explicit InferenceResult_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : label(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->label = "";
      this->top = 0ll;
      this->top_left = 0ll;
      this->bottom = 0ll;
      this->bottom_right = 0ll;
      this->conf = 0.0;
    }
  }

  // field types and members
  using _label_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _label_type label;
  using _top_type =
    int64_t;
  _top_type top;
  using _top_left_type =
    int64_t;
  _top_left_type top_left;
  using _bottom_type =
    int64_t;
  _bottom_type bottom;
  using _bottom_right_type =
    int64_t;
  _bottom_right_type bottom_right;
  using _conf_type =
    double;
  _conf_type conf;

  // setters for named parameter idiom
  Type & set__label(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->label = _arg;
    return *this;
  }
  Type & set__top(
    const int64_t & _arg)
  {
    this->top = _arg;
    return *this;
  }
  Type & set__top_left(
    const int64_t & _arg)
  {
    this->top_left = _arg;
    return *this;
  }
  Type & set__bottom(
    const int64_t & _arg)
  {
    this->bottom = _arg;
    return *this;
  }
  Type & set__bottom_right(
    const int64_t & _arg)
  {
    this->bottom_right = _arg;
    return *this;
  }
  Type & set__conf(
    const double & _arg)
  {
    this->conf = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    yolo_inference::msg::InferenceResult_<ContainerAllocator> *;
  using ConstRawPtr =
    const yolo_inference::msg::InferenceResult_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      yolo_inference::msg::InferenceResult_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      yolo_inference::msg::InferenceResult_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__yolo_inference__msg__InferenceResult
    std::shared_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__yolo_inference__msg__InferenceResult
    std::shared_ptr<yolo_inference::msg::InferenceResult_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InferenceResult_ & other) const
  {
    if (this->label != other.label) {
      return false;
    }
    if (this->top != other.top) {
      return false;
    }
    if (this->top_left != other.top_left) {
      return false;
    }
    if (this->bottom != other.bottom) {
      return false;
    }
    if (this->bottom_right != other.bottom_right) {
      return false;
    }
    if (this->conf != other.conf) {
      return false;
    }
    return true;
  }
  bool operator!=(const InferenceResult_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InferenceResult_

// alias to use template instance with default allocator
using InferenceResult =
  yolo_inference::msg::InferenceResult_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace yolo_inference

#endif  // YOLO_INFERENCE__MSG__DETAIL__INFERENCE_RESULT__STRUCT_HPP_
