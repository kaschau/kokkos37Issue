#ifndef __thtrdat__H__
#define __thtrdat__H__

#include "Kokkos_Core.hpp"

using exec_space = Kokkos::Serial;
using view_space = Kokkos::HostSpace;
using layout = Kokkos::LayoutRight;
static const std::string KokkosLocation = "Serial";

using oneDview = Kokkos::View<double *, layout, view_space>;

//--------------------------------------------------------------------------------------//
//
//        C++ struct
//
//--------------------------------------------------------------------------------------//

struct thtrdat_ {
  oneDview MW;
};

#endif
