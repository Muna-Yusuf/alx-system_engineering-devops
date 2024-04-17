#Enable holberton user to login also open files without error.

#Increase hard file limit for holberton user.
exec { 'hard file':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

#Increase soft file limit for holberton user.
exec { 'soft file':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
