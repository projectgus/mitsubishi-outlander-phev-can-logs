# EV & BMU Can logs

Logger channel 0 is the EV-CAN bus, channel 1 is the BMU-CAN bus.

These logs were done with a video to timestamp events. "TS XYZ" is the SavvyCAN file timestamp from the GVRET file (in seconds) manually taken from the video, so not 100% accurate.

## BMU Bus Message Notes

Most messages on this bus are documented in SimpBMS by @Tom-evnut: https://github.com/Tom-evnut/OutlanderPHEVBMS/blob/master/Decode%20BMS%20Canbus.pdf

### 0x3C2 - battery current flow

* Is the live battery current in/out which is very useful for correlating events on the other bus. See `battery-current.gdf` for a SavvyCAN graph definition.
* sent every 100 ms
* looks like first 4 bytes are a big-endian value representing current flow (units unknown?)
* 5th byte is C8 (status?) in all states
* Zero current seems to be 0x80000000
* over 0x80000000 corresponds to current sourced from battery
* under 0x80000000 corresponds to battery charge current

## EV Bus Message Notes

### 0x185 - something to do with heating or AC compressor?

Seems like it might correlate with both AC compressor and heater on/off...?

### 0x188

Might be the heater control message (maybe, this car doesn't have an electric heater installed...)

### 0x373

Looks like a sensor reading, maybe related to power usage??

### 0x388 - looks like AC compressor control signal (or could be status?)

* byte 0 - seen to be 01 -> 81 after compressor starts -> 82 after compressor stops (?)
* byte 1 - 00 most of the time, goes 00 -> 02 when first byte goes 81 -> 82 after compressor stops
* byte 2-5 - setpoint value. might be a sensor output, but seems very clean...
* byte 6 - often (always?) 00
* byte 7 - 02 when compressor is off, 06 when compressor is on

See battery-and-ac.gdf for a SavvyCAN definition.

### 0x389

Something to do with Ready mode? Value changes when going in and out.

### 0x38A

Some slow moving sensor reading

## 202108081125-normal-mode-gear-selection

Going into Ready Normal mode, selecting various gears (foot on brake whole time), then turning the car off.

* TS 965 corresponds to 0:00
* TS 977 CAN captures start (vehicle becoming Ready)
* TS 995 Into neutral 0:30
* TS 1001 Gearstick to D 0:36
* TS 1004 Gearstick to R 0:39
* TS 1008 Gearstick back to D 0:43
* TS 1012 Gearstick to R 0:47
* TS 1018 Gearstick to P 0:53
* TS 1025 Gearstick to N again 1:00
* TS 1030 Gearstick to P again 1:05
* TS 1040 Power off 1:15

## 202108081130-charge-mode

Putting the car into Charge mode.

* TS 1459 is approximately 0:00 in video
* TS 1469 CAN captures start (vehicle becoming Ready)
* TS 1481 enter charge mode @ 0:22
* TS 1541 sounds changes @1:21, car goes to different/normal idle?
* TS 1579 engine turned off @2:00

## 202108081706-driving-ev

Driving forward up and reversing back down the driveway in EV mode.

* TS 56 is approximately 0:00 in video
* TS 60 CAN captures start (vehicle becoming Ready) 0:04
* TS 90 gearstick to N 0:34
* TS 95 Change into EV Mode 0:39
* TS 106 gearstick to D 0:50
* TS 116 parking brake disengaged 1:00
* TS 123 car moving forward 1:07
* TS 137 car stops moving forward 1:21
* TS 141 gearstick to R 1:25
* TS 146 start moving in reverse 1:30
* TS 166 slowed almost to a stop 1:50
* TS 168 sped up again a bit (still in reverse) 1:52
* TS 174 stopped 1:58
* TS 176 moving again (still reverse) 2:00
* TS 178 stopped again 2:02
* TS 180 gearstick to D 2:04
* TS 189 gearstick to B3 2:13
* TS 190 gearstick to B5 2:14
* TS 201 moving forward 2:25
* TS 210 got to about 10km/h (fastest yet!) 2:34
* TS 216 stopped 2:40
* TS 222 gearstick to R 2:46
* TS 228 started moving backwards 2:52
* TS 246 stopped 3:10
* TS 247 gearstick to D 3:11
* TS 271 Switch to 4WD Lock Mode 3:35
* TS 277 moving forward 3:41
* TS 285 10km/h again! 3:49
* TS 288 almost 15km/h 3:52
* TS 292 stopped again 3:56
* TS 293 gearstick to R 3:57
* TS 295 moving backwards 3:59
* TS 313 stopped 4:17
* TS 314 gearstick to D 4:18
* TS 318 gearstick to B3 then B5 (still in 4WD Lock mode) 4:22
* TS 324 moving forwards 4:28
* TS 328 got to about 17km/h 4:32
* TS 337 stopped 4:41
* TS 338 gearstick to R 4:42
* TS 339 moving backwards 4:43
* TS 355 stopped 4:59
* TS 357 gearstick to P 5:01
* TS 363 parking brake on 5:07
* TS 370 power off 5:14

## 202108081212-ac-on-ev-mode

Running the air conditioner in EV mode.

* TS 223 is 0:00 in the video
* TS 239 Enter EV mode 0:16
* TS 248 Press AC button 0:25 (25C internal temp set)
* TS 254-259 Adjusting temp down to approx 18C @ 0:36
* TS 271 AC is "Blowing cold" 0:45
* TS 292 Compressor stops (AC still turned on) 1:09
* TS 310 Compressor starts 1:27
* TS 326 Compressor stops 1:43
* TS 346 Compressor on 2:03
* TS 357 Compressor off 2:14
* TS 399 Turned off the AC 2:56
* TS 410 Turned off the car 3:07

247.92380 - ID 0x388 - is the first 01 00 00 00 00 00 00 06 message
251.12 is first non-zero values in ID 0x388 bytes 2-3, probably compressor startup

Current draw timestamps (BMU message 0x3C2) on Channel 1 match the video and the values in ID 0x388 pretty much exactly

* current spikes show spikes at 233 (huge), 247 (small), 260 (midsize)
* something off 289.9
* on again 308.5, off 324.2,
* on 344, off 355.2,
* on 373.9, off 383.54

## 202108081224-heater-attempt-ev-mode

Trying to run the heater in EV mode, "auto" setting caused the AC to run for a bit as well.

This car doesn't have an electric heater. I didn't know this when capturing these logs(!), only found out because it never got hot and then I looked under the passenger seat. However the car doesn't seem to behave any different without the heater, maybe the heater control message is still being sent??

When "heater" is "on" in EV mode the heater coolant pump is running, but this might be all that is happening.

* TS 700 is video 0:00
* TS 710.422 is first CAN message, vehicle coming to Ready
* TS 718 Enter EV mode
* TS 732 Change heater mode to top vent
* TS 736 Fan on climate control at 26/23.5, no AC. Expect heating... 0:36
* TS 740 Changed climate to 25/25 0:40
* TS 759 Set CC to 26 on drivers side 0:59
* TS 825 Pressed "auto" climate button, AC came on 2:05
  - Current changes @ 825.628
  - Then really changes @ 828.760
  - Ramps up consumption all the way to peak @ 846.479
  - Slowly reduces until 853.2
  - Then suddenly turns off 853.215
* TS 875 Turned climate up to 30 2:55
* TS 885 Turned AC off manually 3:05
* TS 893 Turned fan up 3:13
* TS 1000 Started turning climate temperature down 5:36
* TS 1022 Got to 18C temp and AC turned itself back on 5:58
* TS 1065 Climate up to 22C 6:05
* TS 1075 Climate up to 25C 6:15
* TS 1089 Climate up to 30C 6:29
* TS 1100 Turned fan OFF 6:40
* TS 1114 Car off 6:54

## 202108091724-ev-heater-mode-maybe-again

Another misguided attempt to make the heater run in EV mode.

* TS 124 is video 0:00
* TS 128 CAN message start, car entering Ready 0:04
* TS 131 Select EV mode 0:07
* TS 140 turn fan on, climate is already set to 29C 0:16
* TS 207 fan off 1:23
* TS 218 fan on 1:34
* TS 242 fan off 1:58
* TS 244 fan on, select slightly higher fan setting 2:00
* TS 250 fan off 2:06
* TS 256 fan on 2:12
* TS 282 fan off 2:38

## 202108091520-long-charge-mode-novideo

Putting car into charge mode again while stationary. No timestamps for this one.

