# Primary Monitor Toggle

This python script was put together quickly for a very specific use-case, and
that is to toggle which monitor is set to be the "primary" monitor.

![Demo GIF of toggling the primary monitor](demo-toggle-monitor.gif)

## How it works
Under the hood, it uses xrandr to get the list of active monitors, and
if there are two active monitors, it collects the names (IDs?) into a list.
Then, for each monitor, it determines whether that monitor is currently set to
primary by parsing the output of
`xrandr --listmonitors | grep {monitor_id}` (where `{monitor_id}` represents
the current monitor beeing iterated over in the loop). With that, the script
discovers which monitor is primary. If the current iterated monitor *is not*
set to primary (i.e. this monitor *needs to be set primary*, since we want
to *toggle* it), then the script sets that monitor ID to a previously set 
variable. The last line of the script uses that variable as input to the command:
`xrandr --output {ID} --primary`, which is what actually does the work of setting
the monitor to be primary. And then, Bob's your uncle.

This might actually be over-engineered for such a simple task, but I couldn't
find a better way to do it with my limited Bash scripting expertise.

### TL;DR
This toggles which monitor is primary. It currently works only if there are
*two* active monitors. The main idea with this script is to make a desktop icon that will be allowed
to execute upon clicking it, as well as to create a keyboard shortcut that
achieves the same thing.

### Why is this needed?
Because I am lazy. I overload my biggest monitor for other devices by changing
the input (e.g. game consoles). When I do that, I want my smaller monitor to be set as primary 
so that when I want to intermittently do computer things, I can use the
smaller monitor while still seeing things like the search GUI, the top bar
(using GNOME, but this applies to other environments too), and see which
windows I'm cycling over when using Alt+Tab. It's convenient for my specific
use-case, and I couldn't find anything online, so I decided to just make a
script for it.
