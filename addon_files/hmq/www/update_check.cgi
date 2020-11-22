#!/usr/bin/env tclsh

set checkURL    "https://api.github.com/repos/twendt/ccu-addon-hmq/releases/latest"
set downloadURL "https://github.com/twendt/ccu-addon-hmq/releases/latest"

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname $val
    }
  }
}

if { [info exists cmd ] && $cmd == "download"} {
  puts -nonewline "Content-Type: text/html; charset=utf-8\r\n\r\n"
  puts "<html><head><meta http-equiv='refresh' content='0; url=$downloadURL' /></head></html>"
} else {
  catch {
    [regexp "tag_name\": \"(master-\[0-9\]\{8\}-\[a-f0-9\]\{7\}-?\[0-9\]*)" [ exec /usr/bin/env wget -qO- --no-check-certificate $checkURL ] dummy newversion]
  }
  if { [info exists newversion] } {
    puts -nonewline $newversion
  } else {
    puts -nonewline "n/a"
  }
}
