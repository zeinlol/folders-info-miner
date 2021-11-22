# folders-info-miner
Get info about all data in folder with json output


## Usage
```angular2html
usage: finder.py [-h] [-p PATH] [-o OUTPUT] [-j]
                 [-i BLACKLIST [BLACKLIST ...]] [-d DEPTH]

Get info about all data in folder with json output

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Target directory.
  -o OUTPUT, --output OUTPUT
                        Output file.
  -j, --json            Make output as json.
  -i BLACKLIST [BLACKLIST ...], --ignore BLACKLIST [BLACKLIST ...]
                        File extensions to ignore.
  -d DEPTH, -depth DEPTH
                        Depth for sub-folders (top-level is 0).
```

## Output
### CLI

size in bytes
```angular2html
targets/
├── .dccache
├── .scannerwork/
│   ├── .sonar_lock
│   ├── css-bundle/
│   │   ├── bin/
│   │   │   └── server
│   │   ├── lib/
│   │   │   ├── src/
│   │   │   │   ├── server.d.ts
│   │   │   │   ├── server.js
│   │   │   │   └── server.js.map
│   │   │   └── tsconfig.tsbuildinfo
```
### JSON

```json
{
  "name": "helpers",
  "type": "folder",
  "size": 4096,
  "items": [
    {
      "name": "config-api.js",
      "type": ".js",
      "size": 2207,
      "items": []
    },
    {
      "name": "environment.js",
      "type": ".js",
      "size": 227,
      "items": []
    },
    {
      "name": "escape-regexp.js",
      "type": ".js",
      "size": 63,
      "items": []
    }
  ]
}
```