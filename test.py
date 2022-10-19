import kokkos
from example import thtrdat_


# This is the python class that inherits the c++ class
# defined in thtrdat_.hpp that holds kokkos arrays
class thtrdat(thtrdat_):
    def __init__(self):
        thtrdat_.__init__(self)


def simulate():

    # Initialize the python class
    test = thtrdat()

    # Set the MW attribute defined in thtrdat_.hpp with a 1D
    # kokkos array. It will fail here with kokkos 3.7
    test.MW = kokkos.array(
        "MW",
        shape=(10,),
        layout=kokkos.LayoutRight,
        dtype=kokkos.double,
        space=kokkos.HostSpace,
        dynamic=False,
    )


if __name__ == "__main__":
    try:
        kokkos.initialize()
        simulate()
        kokkos.finalize()

    except Exception as e:
        import sys
        import traceback

        print(f"{e}")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        sys.exit(1)
