// Generated by gencpp from file om_aiv_util/Service3Request.msg
// DO NOT EDIT!


#ifndef OM_AIV_UTIL_MESSAGE_SERVICE3REQUEST_H
#define OM_AIV_UTIL_MESSAGE_SERVICE3REQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace om_aiv_util
{
template <class ContainerAllocator>
struct Service3Request_
{
  typedef Service3Request_<ContainerAllocator> Type;

  Service3Request_()
    : a()
    , b()
    , c()  {
    }
  Service3Request_(const ContainerAllocator& _alloc)
    : a(_alloc)
    , b(_alloc)
    , c(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _a_type;
  _a_type a;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _b_type;
  _b_type b;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _c_type;
  _c_type c;





  typedef boost::shared_ptr< ::om_aiv_util::Service3Request_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::om_aiv_util::Service3Request_<ContainerAllocator> const> ConstPtr;

}; // struct Service3Request_

typedef ::om_aiv_util::Service3Request_<std::allocator<void> > Service3Request;

typedef boost::shared_ptr< ::om_aiv_util::Service3Request > Service3RequestPtr;
typedef boost::shared_ptr< ::om_aiv_util::Service3Request const> Service3RequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::om_aiv_util::Service3Request_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::om_aiv_util::Service3Request_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace om_aiv_util

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'om_aiv_util': ['/home/tthmatt/ld_ROS/src/om_aiv_util/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::om_aiv_util::Service3Request_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::om_aiv_util::Service3Request_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::om_aiv_util::Service3Request_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::om_aiv_util::Service3Request_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::om_aiv_util::Service3Request_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::om_aiv_util::Service3Request_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::om_aiv_util::Service3Request_<ContainerAllocator> >
{
  static const char* value()
  {
    return "aedc855cb966317ef64c3818700a9db7";
  }

  static const char* value(const ::om_aiv_util::Service3Request_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xaedc855cb966317eULL;
  static const uint64_t static_value2 = 0xf64c3818700a9db7ULL;
};

template<class ContainerAllocator>
struct DataType< ::om_aiv_util::Service3Request_<ContainerAllocator> >
{
  static const char* value()
  {
    return "om_aiv_util/Service3Request";
  }

  static const char* value(const ::om_aiv_util::Service3Request_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::om_aiv_util::Service3Request_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string a\n"
"string b\n"
"string c\n"
;
  }

  static const char* value(const ::om_aiv_util::Service3Request_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::om_aiv_util::Service3Request_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
      stream.next(m.b);
      stream.next(m.c);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Service3Request_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::om_aiv_util::Service3Request_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::om_aiv_util::Service3Request_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.b);
    s << indent << "c: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.c);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OM_AIV_UTIL_MESSAGE_SERVICE3REQUEST_H
