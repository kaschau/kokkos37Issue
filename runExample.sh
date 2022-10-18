git clone https://github.com/pybind/pybind11.git
cd pybind11
git checkout stable
cd ../
mkdir build
cd build
cmake ../
make -j
cp example* ../
cd ../
python3 test.py
