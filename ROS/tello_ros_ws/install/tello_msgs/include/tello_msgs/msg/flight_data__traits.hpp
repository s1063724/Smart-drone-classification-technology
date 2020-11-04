// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tello_msgs:msg/FlightData.idl
// generated code does not contain a copyright notice

#ifndef TELLO_MSGS__MSG__FLIGHT_DATA__TRAITS_HPP_
#define TELLO_MSGS__MSG__FLIGHT_DATA__TRAITS_HPP_

#include "tello_msgs/msg/flight_data__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<tello_msgs::msg::FlightData>()
{
  return "tello_msgs::msg::FlightData";
}

template<>
struct has_fixed_size<tello_msgs::msg::FlightData>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<tello_msgs::msg::FlightData>
  : std::integral_constant<bool, false> {};

}  // namespace rosidl_generator_traits

#endif  // TELLO_MSGS__MSG__FLIGHT_DATA__TRAITS_HPP_
