Name:		python-openapi-core
Version:	0.22.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/openapi_core/openapi_core-%{version}.tar.gz
Summary:	client-side and server-side support for the OpenAPI Specification v3
URL:		https://pypi.org/project/openapi-core/
License:	BSD-3-Clause
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
client-side and server-side support for the OpenAPI Specification v3

%files
%{py_sitedir}/openapi_core
%{py_sitedir}/openapi_core-*.*-info
