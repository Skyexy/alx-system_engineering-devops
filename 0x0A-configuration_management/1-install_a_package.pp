# Using Puppet, install flask from pip3.
include pip

pip::install { 'flask':
  package        => 'flask',
  version        => '2.1.0',
  ensure         => present,
}

#package { 'pip':
#require  => Package['python-pip'],
#ensure   => 'installed'
#provider => 'pip',
#name     => 'flask',
#version  => '2.1.0'}
