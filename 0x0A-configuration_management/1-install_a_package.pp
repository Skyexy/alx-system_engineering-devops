# Using Puppet, install flask from pip3.

package { 'flask':
      require  => Package['flask'],
      ensure   => 'installed'
      provider => 'pip3',
      version  => '2.1.0'
}
