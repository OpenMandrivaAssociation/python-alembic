Name:		python-alembic
Version:	1.20.0
Release:	1
Summary:	Database migration tool for SQLAlchemy
License:	MIT
Group:		Development/Python
URL:		https://alembic.sqlalchemy.org
Source0:	https://files.pythonhosted.org/packages/source/a/alembic/alembic-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sqlalchemy)
BuildRequires:	python%{pyver}dist(mako)

%description
Alembic is a lightweight database migration tool for SQLAlchemy.
ComfyUI uses it for its local application database.

%files
%doc README.rst
%license LICENSE
%{_bindir}/alembic
%{py_sitedir}/alembic
%{py_sitedir}/alembic-*.*-info
