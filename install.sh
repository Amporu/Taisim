
python3 setup.py sdist bdist_wheel
twine upload dist/taisim-0.0.5.tar.gz dist/taisim-0.0.5-py3-none-any.whl
sudo pip3 uninstall taisim
sudo pip3 install taisim

##python3 -m pip install -U dist/taisim-0.0.3.tar.gz
python3 tests/example1.py
    
