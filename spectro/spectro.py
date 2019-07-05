#/bin/env python3
import seabreeze
seabreeze.use("pyseabreeze")

import seabreeze.spectrometers as sb
spec = sb.Spectrometer.from_serial_number()
spec.integration_time_micros(20000)
spec.wavelengths()
