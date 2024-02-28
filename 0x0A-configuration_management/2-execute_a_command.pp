# Create a manifest that kills a process 'killmenow' using puppet
# use exec and pkill

exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0,1]
}
