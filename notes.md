### Adjust screen brightness in Powershell

```sh
# Command
(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,<Brightness Level>)

# Substitute <Brightness Level> in the command above with 0 to 100 brightness level percentage you want.
# For example with 75% brightness level:
(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,75)

```

### Adjust screen brightness in Commad Prompt

```bash
# Command
powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,<Brightness Level>)

# Substitute <Brightness Level> in the command above with 0 to 100 brightness level percentage you want.
# For example with 75% brightness level:
powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,75)

```
