# generated from rosidl_generator_py/resource/_idl.py.em
# with input from yolo_inference:msg/InferenceResult.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InferenceResult(type):
    """Metaclass of message 'InferenceResult'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('yolo_inference')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'yolo_inference.msg.InferenceResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__inference_result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__inference_result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__inference_result
            cls._TYPE_SUPPORT = module.type_support_msg__msg__inference_result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__inference_result

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class InferenceResult(metaclass=Metaclass_InferenceResult):
    """Message class 'InferenceResult'."""

    __slots__ = [
        '_label',
        '_top',
        '_top_left',
        '_bottom',
        '_bottom_right',
        '_conf',
    ]

    _fields_and_field_types = {
        'label': 'string',
        'top': 'int64',
        'top_left': 'int64',
        'bottom': 'int64',
        'bottom_right': 'int64',
        'conf': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.label = kwargs.get('label', str())
        self.top = kwargs.get('top', int())
        self.top_left = kwargs.get('top_left', int())
        self.bottom = kwargs.get('bottom', int())
        self.bottom_right = kwargs.get('bottom_right', int())
        self.conf = kwargs.get('conf', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.label != other.label:
            return False
        if self.top != other.top:
            return False
        if self.top_left != other.top_left:
            return False
        if self.bottom != other.bottom:
            return False
        if self.bottom_right != other.bottom_right:
            return False
        if self.conf != other.conf:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def label(self):
        """Message field 'label'."""
        return self._label

    @label.setter
    def label(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'label' field must be of type 'str'"
        self._label = value

    @builtins.property
    def top(self):
        """Message field 'top'."""
        return self._top

    @top.setter
    def top(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'top' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'top' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._top = value

    @builtins.property
    def top_left(self):
        """Message field 'top_left'."""
        return self._top_left

    @top_left.setter
    def top_left(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'top_left' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'top_left' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._top_left = value

    @builtins.property
    def bottom(self):
        """Message field 'bottom'."""
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'bottom' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'bottom' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._bottom = value

    @builtins.property
    def bottom_right(self):
        """Message field 'bottom_right'."""
        return self._bottom_right

    @bottom_right.setter
    def bottom_right(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'bottom_right' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'bottom_right' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._bottom_right = value

    @builtins.property
    def conf(self):
        """Message field 'conf'."""
        return self._conf

    @conf.setter
    def conf(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'conf' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'conf' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._conf = value
