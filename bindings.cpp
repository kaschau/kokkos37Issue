#include "thtrdat_.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;
PYBIND11_MODULE(example, m) {

  py::class_<thtrdat_>(m, "thtrdat_", py::dynamic_attr())
      .def(py::init<>())
      .def_readwrite("MW", &thtrdat_::MW);
};
