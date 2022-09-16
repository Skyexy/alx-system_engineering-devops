# Using Puppet, install flask from pip3.

package { 'flask':
      require  => Package['flask'],
      name     => 'flask',
      ensure   => '2.1.0',
      provider => 'pip3',
}
