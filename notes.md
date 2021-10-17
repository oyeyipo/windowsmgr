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

# Adjust screen brightness using python
https://stackoverflow.com/questions/36599375/control-screen-brightness-on-windows-10-with-python3-x
prerequisites: wmi, pywin32

`pip install wmi`

```python
import wmi

wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(<brightness>, 0)
```

where: brightness = 0..100
