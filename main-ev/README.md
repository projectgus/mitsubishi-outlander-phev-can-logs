# Main & EV Can logs

Logger channel 0 is the main "C" bus (the one with the diagnostic connector), channel 1 is the EV-CAN bus.

These logs were done with a video to timestamp events. "TS XYZ" is the SavvyCAN file timestamp from the GVRET file (in seconds) manually taken from the video, so not 100% accurate.

## 202109061515-steering-lock-to-lock

Turning car to ready, turning steering wheel back and forth

* TS 235 corresponds to 0:00
* TS 239 Power on to Ready 0:04
* TS 244 Start turning wheel to right 0:09
* TS 247 Let go of wheel for a second then keep turning 0:12
* (few stops and starts while turning the wheel)
* TS 260 Hard lock to the right 0:25
* TS 261 Start turning to the left 0:26
* TS 270 Hard lock to the left, start turning back 0:35
* TS 275 Back to centre, I think 0:40

## 202109061517-parking-brake

Car is already in Ready when this capture starts, parking brake on.

* TS 356 corresponds to 0:00
* TS 370 Parking brake off 0:14
* TS 371 Parking brake on 0:15
* TS 373 Parking brake off 0:17
* TS 375 Parking brake on 0:19
* TS 377 Parking brake off 0:21
* TS 379 Parking brake on 0:23
* TS 381 Parking brake off 0:25
* TS 383 Parking brake on 0:27
* TS 385 Parking brake off 0:29
* TS 388 Parking brake on 0:32
* TS 390 Parking brake off 0:34
* TS 392 Parking brake on 0:36


## 202109091700-ac-on-no-refrigerant

Turning on the AC after the system has been degassed. There is a capture of the AC properly running in the ev-bmu directory.

* TS 110 corresponds to 0:00
* TS 116 Power on to Ready, climate is set to 18C with Air Conditioning off 0:06
* TS 131 Turn on AC 0:21
* TS 143 Put drive window down 0:33
* TS 151 Start turning fan up from minimum 0:41
* TS 154 Fan reaches max 0:44
* TS 161 Turn off climate control (including AC) 0:51

