// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tello_msgs:msg/TelloResponse.idl
// generated code does not contain a copyright notice

#ifndef TELLO_MSGS__MSG__TELLO_RESPONSE__STRUCT_HPP_
#define TELLO_MSGS__MSG__TELLO_RESPONSE__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

#ifndef _WIN32
# define DEPRECATED__tello_msgs__msg__TelloResponse __attribute__((deprecated))
#else
# define DEPRECATED__tello_msgs__msg__TelloResponse __declspec(deprecated)
#endif

namespace tello_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TelloResponse_
{
  using Type = TelloResponse_<ContainerAllocator>;

  explicit TelloResponse_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->rc = 0;
      this->str = "";
    }
  }

  explicit TelloResponse_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : str(_alloc)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->rc = 0;
      this->str = "";
    }
  }

  // field types and members
  using _rc_type =
    uint8_t;
  _rc_type rc;
  using _str_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _str_type str;

  // setters for named parameter idiom
  Type & set__rc(
    const uint8_t & _arg)
  {
    this->rc = _arg;
    return *this;
  }
  Type & set__str(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->str = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t OK =
    1u;
  static constexpr uint8_t ERROR =
    2u;
  static constexpr uint8_t TIMEOUT =
    3u;

  // pointer types
  using RawPtr =
    tello_msgs::msg::TelloResponse_<ContainerAllocator> *;
  using ConstRawPtr =
    const tello_msgs::msg::TelloResponse_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tello_msgs::msg::TelloResponse_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tello_msgs::msg::TelloResponse_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tello_msgs__msg__TelloResponse
    std::shared_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tello_msgs__msg__TelloResponse
    std::shared_ptr<tello_msgs::msg::TelloResponse_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TelloResponse_ & other) const
  {
    if (this->rc != other.rc) {
      return false;
    }
    if (this->str != other.str) {
      return false;
    }
    return true;
  }
  bool operator!=(const TelloResponse_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TelloResponse_

// alias to use template instance with default allocator
using TelloResponse =
  tello_msgs::msg::TelloResponse_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t TelloResponse_<ContainerAllocator>::OK;
template<typename ContainerAllocator>
constexpr uint8_t TelloResponse_<ContainerAllocator>::ERROR;
template<typename ContainerAllocator>
constexpr uint8_t TelloResponse_<ContainerAllocator>::TIMEOUT;

}  // namespace msg

}  // namespace tello_msgs

#endif  // TELLO_MSGS__MSG__TELLO_RESPONSE__STRUCT_HPP_
