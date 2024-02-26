# kill process killmenow

exec { 'pkill':command=>'/usr/bin/pkill killmenow',provider=>'shell',returns=>[0, 1],}
