%define module openapi-core
%define oname openapi_core

Name:		python-openapi-core
Version:	0.23.1
Release:	1
Summary:	client-side and server-side support for the OpenAPI Specification v3
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/openapi-core
Source0:	https://files.pythonhosted.org/packages/source/o/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:tomcli
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
client-side and server-side support for the OpenAPI Specification v3

%prep -a
# Relax the dependency version upper bounds as while some openapi packages
# have syncronised releases, some do not including this one.
tomcli set pyproject.toml str 'tool.poetry.dependencies.openapi-schema-validator' '>=0.8.0 <0.10'
tomcli set pyproject.toml str 'tool.poetry.dependencies.openapi-spec-validator' '>=0.8.0 <0.10'
tomcli set pyproject.toml str 'tool.poetry.dependencies.jsonschema-path' '>=0.4.5 <0.6.0'


%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
