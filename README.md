# Pipeline setup script

The zero level pipeline needs a simple setup script to run a job. This will change when the final infrastructure is in place.

This script reads in a jinja2 template, and given a set of command line arguments spits out a final run script, either to stdout or if the `-o/--output` flag is given, a file.

The main executable is `render-pipelinescript.py`

## <a name="installation"></a>Installation

* Clone the directory `git clone https://github.com/NGTS/pipeline-setup-script`
* Install the python requirements `pip install -r requirements.txt`
* Install the package (in development mode perhaps?) `pip install -e .`


## Running

```
usage: render-pipelinescript.py [-h] --date DATE -b BIAS [BIAS ...] -d DARK
                                [DARK ...] -f FLAT [FLAT ...] -s SCIENCE
                                [SCIENCE ...] [--sha SHA] --planet PLANET -c
                                CAMERA_ID [-o [OUTPUT]]

optional arguments:
  -h, --help            show this help message and exit
  --date DATE
  -b BIAS [BIAS ...], --bias BIAS [BIAS ...]
  -d DARK [DARK ...], --dark DARK [DARK ...]
  -f FLAT [FLAT ...], --flat FLAT [FLAT ...]
  -s SCIENCE [SCIENCE ...], --science SCIENCE [SCIENCE ...]
  --sha SHA
  --planet PLANET
  -c CAMERA_ID, --camera_id CAMERA_ID
  -o [OUTPUT], --output [OUTPUT]
```

## Development

* Install the package as [above](#installation), in development mode
* run the test runner `py.test`

## Required inputs

* date | 2014/11/05
* actions to analyse | {
  "bias": 101141,
  "dark": 101143,
  "flat": 101126,
  "science": 101140,
}
* pipeline sha | 59aa1ec756657430048c45beea8093ed724f5ea2
* planetname | wasp18b
* camera id | 804
