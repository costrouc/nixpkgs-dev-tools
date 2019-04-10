import pytest

from nixpkgs_pytools.python_package_init import initialize_package


@pytest.mark.parametrize("package", [
    'Flask',
    'six',
    'dask'
])
@pytest.mark.xfail
def test_packages(tmp_path, package):
    filename = tmp_path / f"{package}.nix"

    initialize_package(package=package, version=None, filename=filename)

    print(open(filename).read())
