# Setup nginx server

package { 'nginx':
  ensure     => 'installed',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  line   => 'add_header X-Served-By $HOSTNAME;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
