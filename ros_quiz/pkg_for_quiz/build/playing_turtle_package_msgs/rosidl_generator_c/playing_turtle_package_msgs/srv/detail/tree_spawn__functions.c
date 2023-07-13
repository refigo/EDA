// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from playing_turtle_package_msgs:srv/TreeSpawn.idl
// generated code does not contain a copyright notice
#include "playing_turtle_package_msgs/srv/detail/tree_spawn__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
playing_turtle_package_msgs__srv__TreeSpawn_Request__init(playing_turtle_package_msgs__srv__TreeSpawn_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Request__fini(playing_turtle_package_msgs__srv__TreeSpawn_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Request__are_equal(const playing_turtle_package_msgs__srv__TreeSpawn_Request * lhs, const playing_turtle_package_msgs__srv__TreeSpawn_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Request__copy(
  const playing_turtle_package_msgs__srv__TreeSpawn_Request * input,
  playing_turtle_package_msgs__srv__TreeSpawn_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

playing_turtle_package_msgs__srv__TreeSpawn_Request *
playing_turtle_package_msgs__srv__TreeSpawn_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  playing_turtle_package_msgs__srv__TreeSpawn_Request * msg = (playing_turtle_package_msgs__srv__TreeSpawn_Request *)allocator.allocate(sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Request));
  bool success = playing_turtle_package_msgs__srv__TreeSpawn_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Request__destroy(playing_turtle_package_msgs__srv__TreeSpawn_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    playing_turtle_package_msgs__srv__TreeSpawn_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__init(playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  playing_turtle_package_msgs__srv__TreeSpawn_Request * data = NULL;

  if (size) {
    data = (playing_turtle_package_msgs__srv__TreeSpawn_Request *)allocator.zero_allocate(size, sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = playing_turtle_package_msgs__srv__TreeSpawn_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        playing_turtle_package_msgs__srv__TreeSpawn_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__fini(playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      playing_turtle_package_msgs__srv__TreeSpawn_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence *
playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * array = (playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence *)allocator.allocate(sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__destroy(playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__are_equal(const playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * lhs, const playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!playing_turtle_package_msgs__srv__TreeSpawn_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence__copy(
  const playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * input,
  playing_turtle_package_msgs__srv__TreeSpawn_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    playing_turtle_package_msgs__srv__TreeSpawn_Request * data =
      (playing_turtle_package_msgs__srv__TreeSpawn_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!playing_turtle_package_msgs__srv__TreeSpawn_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          playing_turtle_package_msgs__srv__TreeSpawn_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!playing_turtle_package_msgs__srv__TreeSpawn_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `x`
// Member `y`
// Member `theta`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
playing_turtle_package_msgs__srv__TreeSpawn_Response__init(playing_turtle_package_msgs__srv__TreeSpawn_Response * msg)
{
  if (!msg) {
    return false;
  }
  // x
  if (!rosidl_runtime_c__double__Sequence__init(&msg->x, 0)) {
    playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(msg);
    return false;
  }
  // y
  if (!rosidl_runtime_c__double__Sequence__init(&msg->y, 0)) {
    playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(msg);
    return false;
  }
  // theta
  if (!rosidl_runtime_c__double__Sequence__init(&msg->theta, 0)) {
    playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(msg);
    return false;
  }
  return true;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(playing_turtle_package_msgs__srv__TreeSpawn_Response * msg)
{
  if (!msg) {
    return;
  }
  // x
  rosidl_runtime_c__double__Sequence__fini(&msg->x);
  // y
  rosidl_runtime_c__double__Sequence__fini(&msg->y);
  // theta
  rosidl_runtime_c__double__Sequence__fini(&msg->theta);
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Response__are_equal(const playing_turtle_package_msgs__srv__TreeSpawn_Response * lhs, const playing_turtle_package_msgs__srv__TreeSpawn_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->x), &(rhs->x)))
  {
    return false;
  }
  // y
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->y), &(rhs->y)))
  {
    return false;
  }
  // theta
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->theta), &(rhs->theta)))
  {
    return false;
  }
  return true;
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Response__copy(
  const playing_turtle_package_msgs__srv__TreeSpawn_Response * input,
  playing_turtle_package_msgs__srv__TreeSpawn_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // x
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->x), &(output->x)))
  {
    return false;
  }
  // y
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->y), &(output->y)))
  {
    return false;
  }
  // theta
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->theta), &(output->theta)))
  {
    return false;
  }
  return true;
}

playing_turtle_package_msgs__srv__TreeSpawn_Response *
playing_turtle_package_msgs__srv__TreeSpawn_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  playing_turtle_package_msgs__srv__TreeSpawn_Response * msg = (playing_turtle_package_msgs__srv__TreeSpawn_Response *)allocator.allocate(sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Response));
  bool success = playing_turtle_package_msgs__srv__TreeSpawn_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Response__destroy(playing_turtle_package_msgs__srv__TreeSpawn_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__init(playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  playing_turtle_package_msgs__srv__TreeSpawn_Response * data = NULL;

  if (size) {
    data = (playing_turtle_package_msgs__srv__TreeSpawn_Response *)allocator.zero_allocate(size, sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = playing_turtle_package_msgs__srv__TreeSpawn_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__fini(playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence *
playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * array = (playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence *)allocator.allocate(sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__destroy(playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__are_equal(const playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * lhs, const playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!playing_turtle_package_msgs__srv__TreeSpawn_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence__copy(
  const playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * input,
  playing_turtle_package_msgs__srv__TreeSpawn_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(playing_turtle_package_msgs__srv__TreeSpawn_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    playing_turtle_package_msgs__srv__TreeSpawn_Response * data =
      (playing_turtle_package_msgs__srv__TreeSpawn_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!playing_turtle_package_msgs__srv__TreeSpawn_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          playing_turtle_package_msgs__srv__TreeSpawn_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!playing_turtle_package_msgs__srv__TreeSpawn_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
